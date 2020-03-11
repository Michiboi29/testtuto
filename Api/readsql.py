from Api.connect import connect


def sql_read(table_name, cmd):
    db = connect()
    curseur = db.cursor()
    sql = "SHOW COLUMNS FROM {}".format(table_name)
    print(cmd)
    print(sql)

    results = None
    try:

        curseur.execute(cmd)
        results = curseur.fetchall()
        print(results)
        for row in results:
            # Now print fetched result
            print(row)

    except:
        print("Error: unable to fecth data")

    curseur.close()
    db.close()

    return results
