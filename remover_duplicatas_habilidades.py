"""
Script para remover habilidades duplicadas
"""

from database import Database

def remover_duplicadas():
    """Remove habilidades duplicadas mantendo a de maior nível"""
    
    print("🔍 Verificando habilidades duplicadas...\n")
    print("=" * 60)
    
    db = Database("data/portfolio.db")
    
    curriculum = db.get_curriculum()
    if not curriculum:
        print("❌ Nenhum currículo encontrado!")
        return
    
    habilidades = db.get_habilidades(curriculum['id'])
    
    # Agrupar por nome e categoria
    duplicatas = {}
    for hab in habilidades:
        key = (hab['categoria'], hab['nome_habilidade'])
        if key not in duplicatas:
            duplicatas[key] = []
        duplicatas[key].append(hab)
    
    # Encontrar duplicadas
    removidas = 0
    for (categoria, nome), habs in duplicatas.items():
        if len(habs) > 1:
            print(f"\n⚠️  Duplicata encontrada: {nome} ({categoria})")
            # Ordenar por nível (maior primeiro) e data (mais recente primeiro)
            habs_sorted = sorted(habs, key=lambda h: (-h['nivel'], h['id']), reverse=False)
            
            # Manter o primeiro (maior nível), remover os outros
            manter = habs_sorted[0]
            remover = habs_sorted[1:]
            
            print(f"   ✅ Mantendo: ID {manter['id']} - Nível {manter['nivel']}")
            for hab in remover:
                print(f"   🗑️  Removendo: ID {hab['id']} - Nível {hab['nivel']}")
                db.delete_habilidade(hab['id'])
                removidas += 1
    
    if removidas > 0:
        print(f"\n{'=' * 60}")
        print(f"✨ Total de duplicatas removidas: {removidas}")
    else:
        print("\n✅ Nenhuma duplicata encontrada!")
    
    db.close()

if __name__ == "__main__":
    remover_duplicadas()
