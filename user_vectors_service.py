from imgbeddings import imgbeddings
from PIL import Image
from user_vectors_repository import UserVectorRepository
import psycopg2
import numpy
import ast

class UserVectorsService:

    userVectorsRepository : UserVectorRepository

    def __init__(self, userVectorsRepository):
        self.userVectorsRepository = userVectorsRepository

    def look_for_similar_user_vector(self, picture):
        ibed = imgbeddings()
        embedding = ibed.to_embeddings(picture)[0]
        most_similar = self.userVectorsRepository.look_for_similar_user_vector(embedding)
        
        if numpy.linalg.norm(embedding-ast.literal_eval(most_similar[1])) > 10:
            print("ACCESS DENIED")
        else:
            print('ACCESS GRANTED ' + most_similar[0])


    #Only in case of wanting to save someone for testing
    #TODO Delete when not necessary
    def save_embedding(self):
        conn_string = "host='localhost' dbname='postgres' user='myuser' password='mypassword'"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        ibed = imgbeddings()

        embedding = ibed.to_embeddings("resources/face.jpg")[0]
        cur.execute('INSERT INTO uservectors values (%s,%s)', ('Federico', embedding.tolist()))
        conn.commit()
        conn.close()
        

