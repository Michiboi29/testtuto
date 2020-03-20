from Api.connect import connect


def sql_create():
    db = connect()
    curseur = db.cursor()

    file = open('Api\init_db.sql', 'r')
    sql = file.read()
    for table in sql.split(';'):
        if table.strip():
            curseur.execute(table)

    db.commit()

    curseur.close()
    db.close()


sql_create()