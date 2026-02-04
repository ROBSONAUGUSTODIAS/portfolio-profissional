"""
Script de teste para verificar as funcionalidades de habilidades
"""

from database import Database

def test_habilidades():
    """Testa as funções de habilidades"""
    
    print("🔍 Testando funcionalidades de Habilidades\n")
    print("=" * 60)
    
    db = Database("data/portfolio.db")
    
    # Verificar currículo
    curriculum = db.get_curriculum()
    if not curriculum:
        print("❌ Nenhum currículo encontrado!")
        return
    
    print(f"✅ Currículo: {curriculum['nome']}\n")
    
    # Listar habilidades
    habilidades = db.get_habilidades(curriculum['id'])
    
    print("📋 Habilidades Cadastradas:")
    print("-" * 60)
    
    if habilidades:
        categorias = {}
        for hab in habilidades:
            cat = hab['categoria']
            if cat not in categorias:
                categorias[cat] = []
            categorias[cat].append(hab)
        
        total = 0
        for categoria, habs in categorias.items():
            print(f"\n{categoria}:")
            for hab in habs:
                stars = "⭐" * hab['nivel']
                print(f"  • {hab['nome_habilidade']:30} {stars} (ID: {hab['id']})")
                total += 1
        
        print(f"\n{'=' * 60}")
        print(f"Total de habilidades: {total}")
    else:
        print("   (Nenhuma habilidade cadastrada)")
    
    print("\n✨ Teste concluído!")
    
    db.close()

if __name__ == "__main__":
    test_habilidades()
