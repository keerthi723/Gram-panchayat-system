import os
import sys
import pymysql
import certifi

host = os.environ['DB_HOST']
port = int(os.environ.get('DB_PORT', '4000'))
user = os.environ['DB_USER']
password = os.environ['DB_PASSWORD']
db = os.environ.get('DB_NAME', 'python_digital_gram_panchayat')
path = sys.argv[1] if len(sys.argv) > 1 else 'python_digital_gram_panchayat.sql'

conn = pymysql.connect(host=host, port=port, user=user, password=password,
                       charset='utf8', ssl_ca=certifi.where(),
                       ssl_verify_cert=True, ssl_verify_identity=True)
cur = conn.cursor()
cur.execute(f"CREATE DATABASE IF NOT EXISTS `{db}`")
cur.execute(f"USE `{db}`")

text = open(path, encoding='utf8').read()
text = '\n'.join(l for l in text.splitlines() if not l.startswith('--'))
ok = 0
for stmt in text.split(';\n'):
    stmt = stmt.strip().rstrip(';')
    if not stmt:
        continue
    try:
        cur.execute(stmt)
        ok += 1
    except Exception as e:
        print('SKIPPED:', stmt[:70].replace('\n', ' '), '->', e)
conn.commit()
conn.close()
print('Finished.', ok, 'statements ran.')