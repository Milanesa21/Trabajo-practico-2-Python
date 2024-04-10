import csv as c 
from tarea import connect_db, insert_db

with open('localidades.csv', mode='r')as read:
    reader = c.DictReader(read)
    db = connect_db()
    rows_to_insert = []
    for row in reader:
        provincia = row['provincia']
        id = int(row['id'])
        localidad = row['localidad']
        cp = int(row['cp']) if row ['cp'] != '' else None
        id_prov_mstr = int(row['id_prov_mstr'])if row ['id_prov_mstr'] != '' else None
        rows_to_insert.append((provincia, id, localidad, cp, id_prov_mstr))
    insert_db(db, rows_to_insert)