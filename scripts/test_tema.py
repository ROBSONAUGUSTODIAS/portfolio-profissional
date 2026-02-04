import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from database import Database

if __name__ == '__main__':
    db = Database('data/portfolio.db')
    cur = db.get_curriculum()
    cert_id = db.add_certificado(cur['id'], 'TEST TEMA 3', 'data/certificados/test_tema3.png', 'Issuer', '2024-01-01', '', 'Desc', 'http://test', 'image/png', 'info')
    certs = db.get_certificados(cur['id'])
    print('Inserted', cert_id)
    found = [c for c in certs if c['id'] == cert_id]
    if found:
        print('Inserted cert tema:', found[0]['tema'])
    else:
        print('Inserted cert not found in query results')
