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

# This script RESETS the demo database every time it runs
cur.execute(f"DROP DATABASE IF EXISTS `{db}`")
cur.execute(f"CREATE DATABASE `{db}`")
cur.execute(f"USE `{db}`")

text = open(path, encoding='utf8').read()
text = '\n'.join(l for l in text.splitlines() if not l.startswith('--'))
# TiDB does not support the old latin1 collation, so use utf8mb4 instead
text = text.replace('latin1_swedish_ci', 'utf8mb4_general_ci').replace('latin1', 'utf8mb4')

ok = 0
for stmt in text.split(';\n'):
    stmt = stmt.strip().rstrip(';')
    if not stmt:
        continue
    low = stmt.lower()
    # TiDB cannot add AUTO_INCREMENT with ALTER, so these are handled below
    if low.startswith('alter table') and 'auto_increment' in low:
        continue
    try:
        cur.execute(stmt)
        ok += 1
    except Exception as e:
        print('SKIPPED:', stmt[:70].replace('\n', ' '), '->', e)

# Recreate the table that needs auto-numbering
cur.execute("DROP TABLE IF EXISTS voting_votes")
cur.execute("CREATE TABLE voting_votes (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, "
            "user_aadhaar VARCHAR(20) NOT NULL, candidate_id VARCHAR(20) NOT NULL)")

conn.commit()
conn.close()
print('Finished.', ok, 'statements ran.')