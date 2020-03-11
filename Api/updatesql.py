from Api.connect import connect


def sql_update(table_name, set, valset, where):

    sql = "UPDATE {} \
            SET {} = %s \
            WHERE {}"
    sql = sql.format(table_name, set, where)

    valset = [valset]
    print(sql, valset)

    db = connect()
    curseur = db.cursor()
    curseur.execute(sql, valset)
    db.commit()
    print(curseur.rowcount, "record(s) affected")

    curseur.close()
    db.close()

    """cond =""
    liste_where = list(where)
    for key, value in where.items():
        cond += str(key) + " = " + str(value)
        if liste_where.index(key) < len(liste_where) - 1:
            cond += " AND "
    print("cond:", cond)
    sql += cond
    print(sql)"""
