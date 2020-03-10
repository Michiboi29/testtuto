from Api.connect import connect


def sql_drop(table_name):
    db = connect()
    curseur = db.cursor()
    sql = "DROP TABLE IF EXISTS {}".format(table_name)
    curseur.execute(sql)
    curseur.close()
    db.close()
    print('table' + table_name + 'drop!')
