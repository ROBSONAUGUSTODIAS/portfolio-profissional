"""Verificar dados no banco"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path('.') / 'assets'))

from database import Database

db = Database('data/portfolio.db')
c = db.get_curriculum()
print(f'Currículo ID: {c["id"]}')
print(f'Currículo: {c["nome"]}')

certs = db.get_certificados(c['id'])
print(f'Certificados: {len(certs)}')

if len(certs) > 0:
    print('Certificados encontrados:')
    for cert in certs:
        print(f'  - {cert["titulo"]}')
else:
    print('Nenhum certificado cadastrado')
