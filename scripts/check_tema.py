import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from database import Database

if __name__ == '__main__':
    db = Database('data/portfolio.db')
    cur = db.get_curriculum()
    certs = db.get_certificados(cur['id'])
    nulls = [c for c in certs if ('tema' not in c.keys()) or (not c['tema'])]
    print('Total certs:', len(certs))
    print('Certs with missing or empty tema:', len(nulls))
    for c in nulls:
        print(c['id'], c['titulo'], c['tema'] if 'tema' in c.keys() else None)
