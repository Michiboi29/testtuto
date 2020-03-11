from Api.connect import connect


def sql_columns(table_name):
    db = connect()
    curseur = db.cursor()
    sql = "SHOW COLUMNS FROM {}".format(table_name)
    curseur.execute(sql)
    colomns = curseur.fetchall()
    atributs = []
    for i in range(len(colomns)):
        atributs.append(colomns[i][0])
    curseur.close()
    db.close()

    return atributs
