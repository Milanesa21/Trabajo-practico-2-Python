import sys
import MySQLdb



def connect_db():
    try:
        db = MySQLdb.connect("localhost","root","","test")
    except MySQLdb.Error as e:
        print("No se pudo conectar:", e)
        sys.exit(1)
    print("Conexion correcta")
    return db

def create_db(db):
    cursor = db.cursor()
    sql_delete = "DROP TABLE IF EXISTS localidades"
    cursor.execute(sql_delete)
    db.commit()
    sql_create = """CREATE TABLE IF NOT EXISTS localidades(
    provincia VARCHAR(255),
    id INT,
    localidad VARCHAR(255),
    cp INT,
    id_prov_mstr INT)"""
    cursor.execute(sql_create)


def insert_db(db, rows_to_insert):
    cursor = db.cursor()
    sql_insert = """INSERT INTO localidades (provincia, id, localidad, cp, id_prov_mstr) VALUES (%s, %s, %s, %s, %s)"""
    
    cursor.executemany(sql_insert, rows_to_insert)
    db.commit()


def select_db(db):
    cursor = db.cursor()
    sql_select = "SELECT * FROM localidades"
    cursor.execute(sql_select)
    result = cursor.fetchall()
    return result

def count_localidades(db):
    cursor = db.cursor()
    sql_count = "SELECT provincia, COUNT(*) FROM localidades GROUP BY provincia"
    cursor.execute(sql_count)
    result = cursor.fetchall()
    return result


