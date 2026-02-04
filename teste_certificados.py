"""Teste de lógica para show_certificados"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path('.') / 'assets'))

from database import Database

db = Database('data/portfolio.db')
curriculum = db.get_curriculum()

print(f"✅ Currículo: {curriculum['nome']}")

certificados = db.get_certificados(curriculum['id'])
print(f"📌 Certificados recuperados: {len(certificados)}")

# Simular a verificação
if certificados is None or len(certificados) == 0:
    print("❌ Nenhum certificado")
else:
    num_certs = len(certificados)
    print(f"✅ Número de certificados: {num_certs}")
    
    if num_certs < 1:
        print("❌ Erro ao carregar")
    else:
        print(f"✅ Slider pode ir de 0 a {num_certs - 1}")
        print(f"✅ Certificado 0: {certificados[0]['titulo']}")
