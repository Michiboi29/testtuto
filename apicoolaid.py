from Api.connect import connect
from Api.createsql import sql_create
from Api.readsql import sql_read


def sql_insert(table_name, *atributs, **val):
    """Exemple d'entrée :
    sql_insert(tabtest, nom, age, sex, {s:'michaud', d:20, c:'M'})"""
    db = connect()
    curseur = db.cursor()
    print(atributs)
    print(val)
    print(tuple(val))
    print(tuple(val.values()))
    lon = len(tuple(val.values()))
    print()
    sql = "INSERT INTO`" + table_name + "(" + atributs + ") \
       VALUES (" + ('{}') * lon + ")"

    print(sql)
    try:
        curseur.execute(sql)
        db.commit()
    except:
        db.rollback()

    curseur.close()
    db.close()


sql_create()
sql_insert('ami', 'prenom', 'nom', 'age', 'sex', s='etienne', s1='michaud', d=20, c='M')
sql_read("SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d' AND AGE < '%d'", 50, 1000)
