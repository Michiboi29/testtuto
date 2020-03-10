from Api.connect import connect


def sql_read(cmd):
    db = connect()
    curseur = db.cursor()
    sql = cmd
    print(sql)

    try:
        curseur.execute(sql)
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
