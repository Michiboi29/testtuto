from Api.connect import connect


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
    print(lon)

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

