from Api.connect import connect
from Api.sql_columns import sql_columns


def sql_delete(table_name, where):

    sql = "DELETE FROM {} \
            WHERE {}"
    sql = sql.format(table_name, where)

    print(sql)

    db = connect()
    curseur = db.cursor()
    curseur.execute(sql)
    db.commit()
    print(curseur.rowcount, "record(s) deleted")

    curseur.close()
    db.close()
