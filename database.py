"""
Módulo de gerenciamento do banco de dados SQLite
Responsável por criar e gerenciar tabelas e operações com o banco
"""

import sqlite3
import os
from datetime import datetime
from pathlib import Path


class Database:
    def __init__(self, db_path: str = "data/portfolio.db"):
        """Inicializa a conexão com o banco de dados"""
        self.db_path = db_path
        self.conn = None
        self.init_database()

    def init_database(self):
        """Cria o banco de dados e as tabelas se não existirem"""
        # Garante que o diretório existe
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        # check_same_thread=False permite uso em múltiplas threads (necessário para Streamlit)
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.cursor()

        # Tabela de Currículo
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS curriculum (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT,
                profissao TEXT NOT NULL,
                sobre TEXT,
                resumo TEXT,
                arquivo_path TEXT,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Tabela de Experiência
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS experiencia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curriculum_id INTEGER NOT NULL,
                titulo TEXT NOT NULL,
                empresa TEXT NOT NULL,
                descricao TEXT,
                data_inicio DATE,
                data_fim DATE,
                ativo BOOLEAN DEFAULT 1,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (curriculum_id) REFERENCES curriculum (id)
            )
        """)

        # Tabela de Educação/Cursos
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS educacao (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curriculum_id INTEGER NOT NULL,
                titulo TEXT NOT NULL,
                instituicao TEXT NOT NULL,
                data_inicio DATE,
                data_conclusao DATE,
                descricao TEXT,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (curriculum_id) REFERENCES curriculum (id)
            )
        """)

        # Tabela de Certificados
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS certificados (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curriculum_id INTEGER NOT NULL,
                titulo TEXT NOT NULL,
                issuer TEXT,
                data_obtencao DATE,
                validade_fim DATE,
                arquivo_path TEXT NOT NULL,
                tipo_arquivo TEXT,
                descricao TEXT,
                url_certificado TEXT,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (curriculum_id) REFERENCES curriculum (id)
            )
        """)

        # Tabela de Habilidades
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS habilidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curriculum_id INTEGER NOT NULL,
                categoria TEXT NOT NULL,
                nome_habilidade TEXT NOT NULL,
                nivel INTEGER DEFAULT 3,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (curriculum_id) REFERENCES curriculum (id)
            )
        """)

        # Tabela de Redes Sociais/Links
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS links_sociais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                curriculum_id INTEGER NOT NULL,
                plataforma TEXT NOT NULL,
                url TEXT NOT NULL,
                ativo BOOLEAN DEFAULT 1,
                data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (curriculum_id) REFERENCES curriculum (id)
            )
        """)

        self.conn.commit()

        # Migração: adicionar coluna 'tema' na tabela 'certificados' se ainda não existir
        try:
            cursor.execute("PRAGMA table_info(certificados)")
            cols = [r[1] if isinstance(r, tuple) else r["name"] for r in cursor.fetchall()]
            if "tema" not in cols:
                cursor.execute("ALTER TABLE certificados ADD COLUMN tema TEXT DEFAULT 'primary'")
                self.conn.commit()
        except Exception as e:
            # Não interrompe a inicialização; apenas avisa em caso de falha na migração
            print(f"⚠️ Migration warning: não foi possível adicionar coluna 'tema': {e}")

    def get_curriculum(self):
        """Recupera os dados do currículo principal"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM curriculum ORDER BY data_criacao DESC LIMIT 1")
        return cursor.fetchone()

    def create_curriculum(self, nome: str, email: str, profissao: str, telefone: str = "", sobre: str = "") -> int:
        """Cria um novo currículo"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO curriculum (nome, email, profissao, telefone, sobre)
            VALUES (?, ?, ?, ?, ?)
        """, (nome, email, profissao, telefone, sobre))
        self.conn.commit()
        return cursor.lastrowid

    def update_curriculum(self, curriculum_id: int, nome: str = "", email: str = "", 
                         profissao: str = "", telefone: str = "", sobre: str = "", resumo: str = ""):
        """Atualiza dados do currículo"""
        cursor = self.conn.cursor()
        updates = []
        params = []
        
        if nome:
            updates.append("nome = ?")
            params.append(nome)
        if email:
            updates.append("email = ?")
            params.append(email)
        if profissao:
            updates.append("profissao = ?")
            params.append(profissao)
        if telefone:
            updates.append("telefone = ?")
            params.append(telefone)
        if sobre:
            updates.append("sobre = ?")
            params.append(sobre)
        if resumo:
            updates.append("resumo = ?")
            params.append(resumo)
        
        updates.append("data_atualizacao = CURRENT_TIMESTAMP")
        params.append(curriculum_id)
        
        query = f"UPDATE curriculum SET {', '.join(updates)} WHERE id = ?"
        cursor.execute(query, params)
        self.conn.commit()

    def add_certificado(self, curriculum_id: int, titulo: str, arquivo_path: str, 
                       issuer: str = "", data_obtencao: str = "", validade_fim: str = "",
                       descricao: str = "", url_certificado: str = "", tipo_arquivo: str = "", tema: str = "primary"):
        """Adiciona um novo certificado (agora com suporte a 'tema')"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO certificados 
            (curriculum_id, titulo, arquivo_path, issuer, data_obtencao, validade_fim, 
             descricao, url_certificado, tipo_arquivo, tema)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (curriculum_id, titulo, arquivo_path, issuer, data_obtencao, validade_fim, 
              descricao, url_certificado, tipo_arquivo, tema))
        self.conn.commit()
        return cursor.lastrowid

    def get_certificados(self, curriculum_id: int):
        """Recupera todos os certificados de um currículo na ordem de inserção"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM certificados 
            WHERE curriculum_id = ? 
            ORDER BY id ASC
        """, (curriculum_id,))
        return cursor.fetchall()

    def delete_certificado(self, certificado_id: int):
        """Deleta um certificado"""
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM certificados WHERE id = ?", (certificado_id,))
        self.conn.commit()

    def update_certificado(self, certificado_id: int, titulo: str, arquivo_path: str,
                          issuer: str = "", data_obtencao: str = "", validade_fim: str = "",
                          descricao: str = "", url_certificado: str = "", tipo_arquivo: str = "", tema: str = "primary"):
        """Atualiza um certificado existente"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE certificados 
            SET titulo = ?, arquivo_path = ?, issuer = ?, data_obtencao = ?, 
                validade_fim = ?, descricao = ?, url_certificado = ?, tipo_arquivo = ?, 
                tema = ?, data_atualizacao = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (titulo, arquivo_path, issuer, data_obtencao, validade_fim, 
              descricao, url_certificado, tipo_arquivo, tema, certificado_id))
        self.conn.commit()

    def add_experiencia(self, curriculum_id: int, titulo: str, empresa: str, 
                       descricao: str = "", data_inicio: str = "", data_fim: str = ""):
        """Adiciona uma experiência profissional"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO experiencia (curriculum_id, titulo, empresa, descricao, data_inicio, data_fim)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (curriculum_id, titulo, empresa, descricao, data_inicio, data_fim))
        self.conn.commit()
        return cursor.lastrowid

    def get_experiencias(self, curriculum_id: int):
        """Recupera todas as experiências"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM experiencia WHERE curriculum_id = ? AND ativo = 1 
            ORDER BY data_inicio DESC
        """, (curriculum_id,))
        return cursor.fetchall()

    def add_educacao(self, curriculum_id: int, titulo: str, instituicao: str,
                    data_conclusao: str = "", descricao: str = "", data_inicio: str = ""):
        """Adiciona educação/curso"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO educacao (curriculum_id, titulo, instituicao, data_conclusao, descricao, data_inicio)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (curriculum_id, titulo, instituicao, data_conclusao, descricao, data_inicio))
        self.conn.commit()
        return cursor.lastrowid

    def get_educacao(self, curriculum_id: int):
        """Recupera toda educação"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM educacao WHERE curriculum_id = ? ORDER BY data_conclusao DESC
        """, (curriculum_id,))
        return cursor.fetchall()

    def add_habilidade(self, curriculum_id: int, categoria: str, nome_habilidade: str, nivel: int = 3):
        """Adiciona uma habilidade"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO habilidades (curriculum_id, categoria, nome_habilidade, nivel)
            VALUES (?, ?, ?, ?)
        """, (curriculum_id, categoria, nome_habilidade, nivel))
        self.conn.commit()
        return cursor.lastrowid

    def get_habilidades(self, curriculum_id: int):
        """Recupera todas as habilidades agrupadas por categoria"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT id, categoria, nome_habilidade, nivel FROM habilidades 
            WHERE curriculum_id = ? ORDER BY categoria, nome_habilidade
        """, (curriculum_id,))
        return cursor.fetchall()

    def delete_habilidade(self, habilidade_id: int):
        """Deleta uma habilidade pelo ID"""
        cursor = self.conn.cursor()
        cursor.execute("""
            DELETE FROM habilidades WHERE id = ?
        """, (habilidade_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def add_link_social(self, curriculum_id: int, plataforma: str, url: str):
        """Adiciona link de rede social"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO links_sociais (curriculum_id, plataforma, url)
            VALUES (?, ?, ?)
        """, (curriculum_id, plataforma, url))
        self.conn.commit()
        return cursor.lastrowid

    def get_links_sociais(self, curriculum_id: int):
        """Recupera todos os links sociais ativos"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM links_sociais WHERE curriculum_id = ? AND ativo = 1
        """, (curriculum_id,))
        return cursor.fetchall()

    def delete_link_social(self, link_id: int):
        """Remove um link social (soft delete)"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE links_sociais SET ativo = 0 WHERE id = ?
        """, (link_id,))
        self.conn.commit()
        return cursor.rowcount > 0

    def update_link_social(self, link_id: int, url: str):
        """Atualiza a URL de um link social"""
        cursor = self.conn.cursor()
        cursor.execute("""
            UPDATE links_sociais SET url = ? WHERE id = ?
        """, (url, link_id))
        self.conn.commit()
        return cursor.rowcount > 0

    def close(self):
        """Fecha a conexão com o banco de dados"""
        if self.conn:
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
