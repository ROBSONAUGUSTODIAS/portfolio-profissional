"""
Script para corrigir caminhos dos certificados no banco de dados
Converte barras invertidas (\) para barras normais (/) para compatibilidade Linux
"""
from database import Database

def corrigir_caminhos():
    """Corrige os caminhos no banco de dados"""
    db = Database("data/portfolio.db")
    
    curriculum = db.get_curriculum()
    if not curriculum:
        print("❌ Nenhum currículo encontrado!")
        return
    
    certificados = db.get_certificados(curriculum['id'])
    
    if not certificados:
        print("❌ Nenhum certificado encontrado!")
        return
    
    print(f"📊 Total de certificados: {len(certificados)}")
    print("🔄 Corrigindo caminhos...\n")
    
    corrigidos = 0
    cursor = db.conn.cursor()
    
    for cert in certificados:
        caminho_atual = cert['arquivo_path']
        caminho_corrigido = caminho_atual.replace('\\', '/')
        
        if caminho_atual != caminho_corrigido:
            cursor.execute("""
                UPDATE certificados 
                SET arquivo_path = ? 
                WHERE id = ?
            """, (caminho_corrigido, cert['id']))
            
            print(f"✅ {cert['titulo']}")
            print(f"   Antes: {caminho_atual}")
            print(f"   Depois: {caminho_corrigido}\n")
            corrigidos += 1
    
    db.conn.commit()
    
    print(f"\n{'='*70}")
    print(f"✨ {corrigidos} caminhos corrigidos com sucesso!")
    print(f"{'='*70}")
    
    # Verificar resultado
    print("\n📋 Verificando caminhos atualizados...\n")
    certificados_atualizados = db.get_certificados(curriculum['id'])
    
    for i, cert in enumerate(certificados_atualizados[:3], 1):
        print(f"{i}. {cert['titulo']}")
        print(f"   Caminho: {cert['arquivo_path']}")
        print(f"   Usa barras corretas: {'/' in cert['arquivo_path']}\n")
    
    db.close()

if __name__ == "__main__":
    corrigir_caminhos()
