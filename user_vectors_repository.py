import psycopg2
from psycopg2.pool import SimpleConnectionPool
from contextlib import contextmanager

class UserVectorRepository:

    conn_pool: SimpleConnectionPool


    def __init__(self, conn_string):
        self.conn_pool = SimpleConnectionPool(1, 10, dsn=conn_string)

    @contextmanager
    def getcursor(self):
        con = self.conn_pool.getconn()
        try:
            yield con.cursor()
        finally:
            self.conn_pool.putconn(con)


    def look_for_similar_user_vector(self, embedding):
        try:
            with self.getcursor() as cur:
                string_representation = "["+ ",".join(str(x) for x in embedding.tolist()) +"]"
                cur.execute("SELECT * FROM userVectors ORDER BY embedding <-> %s LIMIT 1;", (string_representation,))
                rows = cur.fetchall()
                return rows[0]
        except Exception as e:
            print('Error when looking for similar image')

        