from Api.connect import connect


def sql_create():
    with open('Api\init_sql.txt', 'r') as file:
        data = file.read().replace('\n', '')
    print(data)

    db = connect()
    curseur = db.cursor()
    curseur.execute(data, multi=True)
    curseur.close()
    db.close()


sql_create()
