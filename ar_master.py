import os
import pymysql


class master_flask_code:
    def __init__(self):
        self.user = os.environ.get('DB_USER', 'root')
        self.password = os.environ.get('DB_PASSWORD', '')
        self.host = os.environ.get('DB_HOST', 'localhost')
        self.port = int(os.environ.get('DB_PORT', '3306'))
        self.database = os.environ.get('DB_NAME', 'python_digital_gram_panchayat')

        def connect(self):
        options = {}
        ca = os.environ.get('DB_SSL_CA')
        if ca:
            options = {'ssl_ca': ca, 'ssl_verify_cert': True,
                       'ssl_verify_identity': True}
        return pymysql.connect(user=self.user, password=self.password,
                               host=self.host, port=self.port,
                               database=self.database, charset='utf8',
                               **options)
    def _run(self, qry, values=None, write=False):
        conn = self.connect()
        try:
            cursor = conn.cursor()
            if values is None:
                result = cursor.execute(qry)
            else:
                result = cursor.execute(qry, values)
            if write:
                conn.commit()
                return result
            return cursor.fetchall()
        finally:
            conn.close()

    def find_max_id(self, table):
        data = self._run("SELECT id FROM " + table)
        return len(data) + 1

    def insert_query(self, qry):
        return self._run(qry, write=True)

    def insert_query2(self, qry, values=None):
        return self._run(qry, values, write=True)

    def select_login(self, qry):
        return 'no' if len(self._run(qry)) == 0 else 'yes'

    def select_single_colum(self, table, colum):
        return self._run("select " + colum + " from " + table)

    def select_direct_query(self, qry):
        return self._run(qry)

    def select_direct_query2(self, qry, values=None):
        return self._run(qry, values)