from Api.connect import connect
from Api.sql_columns import sql_columns


def sql_insert(table_name, **atributs):

    atributs_list = sql_columns(table_name)
    atributs_dict = dict(zip(atributs_list, ['NULL'] * len(atributs_list)))
    for i, j in atributs.items():
        atributs_dict[i] = j
    format_dict = atributs_dict
    for i, j in atributs_dict.items():
        if j != 'NULL':
            format_dict[i] = '%s'

    print("atr_dict = ", atributs_dict)
    print("form_dict = ", format_dict)
    atributs_str = ""
    format_val = ""
    for i in atributs_list:
        format_val += '{' + i + '}'
        if atributs_list.index(i) < len(atributs_list) - 1:
            format_val += ', '

    for i in atributs_list:
        atributs_str += i
        if atributs_list.index(i) < len(atributs_list) - 1:
            atributs_str += ', '

    print("val =", format_val)
    print("atri_str= ", atributs_str)

    db = connect()
    curseur = db.cursor()

    sql = "INSERT INTO " + table_name + " (" + atributs_str + ") \
       VALUES (" + format_val + ")"
    print(sql)
    sql = sql.format(**format_dict)
    valeurs = list(atributs.values())
    print(sql, valeurs)

    curseur.execute(sql, valeurs)
    db.commit()
    print(curseur.rowcount, "record inserted.")

    #except:
      #  print("ereur")
       # db.rollback()

    curseur.close()
    db.close()


def sql_delete(table_name, where):

    sql = "DELETE FROM {0} \
            WHERE {1}"
    sql = sql.format(table_name, where)

    db = connect()
    curseur = db.cursor()
    curseur.execute(sql)
    db.commit()
    print(curseur.rowcount, "record(s) deleted")

    curseur.close()
    db.close()


def sql_drop(table_name):
    db = connect()
    curseur = db.cursor()
    sql = "DROP TABLE IF EXISTS {}".format(table_name)
    curseur.execute(sql)
    curseur.close()
    db.close()
    print('table ' + table_name + ' drop!')


def sql_update(table_name, set, valset, where):

    sql = "UPDATE {0} \
            SET {1} = %s \
            WHERE {2}"
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


def sql_read(table_name, distinct=False, where=None):

    dist = " "
    if distinct:
        dist = " DISTINCT "

    sql = "SELECT{1}* FROM {0}".format(table_name, dist)

    if where is not None:
        where = " WHERE " + where

    sql += where

    print("Reads:", sql)

    db = connect()
    curseur = db.cursor()

    colomns = sql_columns(table_name)
    valeur = None
    result = []
    try:

        curseur.execute(sql)
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


def sql_comand(table_name, cmd):
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

    print(valeur)
    print(result)

    curseur.close()
    db.close()

    return valeur
