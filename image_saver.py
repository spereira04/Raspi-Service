import os
import numpy as np
from imgbeddings import imgbeddings
from PIL import Image
import psycopg2

# remember it needs to have the table defined already
conn_string = "host='localhost' dbname='postgres' user='myuser' password='mypassword'"
conn = psycopg2.connect(conn_string)

# load imgbeddings so we can calculate embeddings
ibed = imgbeddings()

    # read the image
img = Image.open('face.jpg')
    # calculate the embedding for this face
embedding = ibed.to_embeddings(img)[0]
# and write it to PostgreSQL
cur = conn.cursor()
cur.execute("INSERT INTO userVectors values (%s,%s)", ('face.jpg', embedding.tolist()))

conn.commit()