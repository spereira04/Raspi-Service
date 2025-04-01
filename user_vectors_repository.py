import psycopg2

class UserVectorRepository:

    conn_string : str

    def __init__(self, conn_string):
        self.conn_string = conn_string


    def look_for_similar_user_vector(self, embedding):
        conn = psycopg2.connect(self.conn_string)

        cur = conn.cursor()
        string_representation = "["+ ",".join(str(x) for x in embedding.tolist()) +"]"
        cur.execute("SELECT * FROM userVectors ORDER BY embedding <-> %s LIMIT 1;", (string_representation,))
        rows = cur.fetchall()
        conn.close()

        return rows