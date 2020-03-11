from Api.connect import connect
from Api.sql_columns import sql_columns


def sql_update(table_name, set, valset, **where):

    db = connect()
    curseur = db.cursor()

    sql = "UPDATE {} \
                SET {} = {} \
                WHERE "
    sql = sql.format(table_name, set, valset)
    print(where)
    cond =""
    liste_where = list(where)
    for key, value in where.items():
        cond += key + " = " + value
        if liste_where.index(key) < len(liste_where) - 1:
            cond += " AND "

    print("cond:", cond)
