from Api.connect import connect


def checkTableExists(table_name):
    db = connect()
    curseur = db.cursor()

    curseur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(table_name.replace('\'', '\'\'')))

    exists = False
    if curseur.fetchone()[0] == 1:
        exists = True

    curseur.close()
    return exists
