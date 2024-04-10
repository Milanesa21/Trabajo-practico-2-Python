import sys
import MySQLdb

def connect_db():
    try:
        db = MySQLdb.connect("localhost","root","","test")
    except MySQLdb.Error as e:
        print("No se pudo conectar:", e)
        sys.exit(1)
    print("Conexion correcta")
    cursor = db.cursor()
    sql_create = """CREATE TABLE IF NOT EXISTS localidades(
    provincia VARCHAR(255),
    id INT,
    localidad VARCHAR(255),
    cp INT,
    id_prov_mstr INT)"""
    cursor.execute(sql_create)
    return db


def insert_db(db, rows_to_insert):
    cursor = db.cursor()
    sql_insert = """INSERT INTO localidades (provincia, id, localidad, cp, id_prov_mstr) VALUES (%s, %s, %s, %s, %s)"""
    
    cursor.executemany(sql_insert, rows_to_insert)
    db.commit()



