from Api.connect import connect
from Api.sql_columns import sql_columns


def sql_read(table_name, cmd):
    db = connect()
    curseur = db.cursor()
    print("Reads:", cmd)

    colomns = sql_columns(table_name)

    valeur = None
    result = []
    try:

        curseur.execute(cmd)
        valeur = curseur.fetchall()
        print(colomns)
        for row in valeur:
            # Now print fetched result
            print(row)
            dictio = dict(zip(colomns, row))
            result.append(dictio)

    except:
        print("Error: unable to fecth data")

    print(result)

    curseur.close()
    db.close()

    return result
