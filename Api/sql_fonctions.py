from Api.connect import connect
from Api.sql_columns import sql_columns
from Api.checkexists import checkTableExists


def sql_insert(table_name, **atributs):

    atributs_list = sql_columns(table_name)
    atributs_dict = dict(zip(atributs_list, ['NULL'] * len(atributs_list)))
    for i, j in atributs.items():
        atributs_dict[i] = j
    format_dict = atributs_dict
    for i, j in atributs_dict.items():
        if j != 'NULL':
            format_dict[i] = '%s'

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

    db = connect()
    curseur = db.cursor()

    sql = "INSERT INTO " + table_name + " (" + atributs_str + ") \
       VALUES (" + format_val + ")"
    sql = sql.format(**format_dict)
    valeurs = list(atributs.values())
    print(sql, valeurs)
    try:
        curseur.execute(sql, valeurs)
        db.commit()
        print(curseur.rowcount, "record inserted.")

    except:
        print("ereur d'insertion")
        db.rollback()

    curseur.close()
    db.close()


def sql_delete(table_name, where=None):

    sql = "DELETE FROM {0}"
    sql = sql.format(table_name)

    if where is not None:
        where = " WHERE " + where
    sql += where
    print(sql)

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
    if not checkTableExists(table_name):
        print('table ' + table_name + ' drop!')


def sql_update(table_name, where=None, **set_val):

    sql = "UPDATE {0} SET "
    sql = sql.format(table_name)

    set_liste = list(set_val)
    val_liste = list(set_val.values())
    sets = ""
    for t, val in set_val.items():
        sets += t + " = %s"
        if set_liste.index(t) < len(set_liste) - 1:
            sets += ', '
    sql += sets

    if where is not None:
        where = " WHERE " + where
    sql += where

    print(sql, val_liste)

    db = connect()
    curseur = db.cursor()
    curseur.execute(sql, val_liste)
    db.commit()
    print(curseur.rowcount, "record(s) affected")

    curseur.close()
    db.close()


def sql_read(table_name, select="*", distinct=False, where=None, groupby=None,having=None, orderby=None):

    dist = " "
    if distinct:
        dist = " DISTINCT "

    sql = "SELECT{1}{0} FROM {2}".format(select, dist, table_name)

    if where is not None:
        where = " WHERE " + where
        sql += where
    if groupby is not None:
        groupby = " GROUP BY " + groupby
        sql += groupby
    if having is not None:
        having = " ORDER BY " + having
        sql += having
    if orderby is not None:
        orderby = " ORDER BY " + orderby
        sql += orderby

    print("Reads:", sql)

    colomns = sql_columns(table_name)
    if select != "*":
        colomns = []
        sections = select.split()
        sections.append("fin")
        for col in sections:
            if col == "fin":
                break
            if sections[(sections.index(col) + 1)] != "AS" and col != "AS" and sections[(sections.index(col) + 1)] != "as" and col != "as":
                col = col.replace(',', '')
                colomns.append(col)

    db = connect()
    curseur = db.cursor()

    result = []
    try:

        curseur.execute(sql)
        valeur = curseur.fetchall()
        print(colomns)
        for row in valeur:
            print(row)
            dictio = dict(zip(colomns, row))
            result.append(dictio)

    except:
        print("Error: unable to fecth data")

    print(result)

    curseur.close()
    db.close()

    return result


def sql_comand(cmd):
    db = connect()
    curseur = db.cursor()
    print("Commande:", cmd)

    f = False
    table_name = None
    for i in cmd.split():
        if f:
            table_name = i
        if i == "FROM" or i == "from":
            f = True

    opperation = cmd.split()[0]

    curseur.execute(cmd)
    if opperation == "SELECT" or opperation == "select":
        f = False
        s = False
        select = ""
        for i in cmd.split():
            if i == "FROM" or i == "from":
                f = True
            if s and not f:
                select += " " + i
            if i == "SELECT" or i == "select":
                s = True

        colomns = sql_columns(table_name)
        sections = select.split()
        if sections[0] != "*" and sections[0] != "DISTINCT" and sections[0] != "distinct":
            colomns = []
            sections.append("fin")
            for col in sections:
                if col == "fin":
                    break
                if sections[(sections.index(col) + 1)] != "AS" and col != "AS" and sections[(sections.index(col) + 1)] != "as" and col != "as":

                    col = col.replace(',', '')
                    colomns.append(col)

        result = []
        valeur = curseur.fetchall()
        print(colomns)
        for row in valeur:
            print(row)
            dictio = dict(zip(colomns, row))
            result.append(dictio)
        print(result)
        print(curseur.rowcount, "record(s) reached")
    else:
        result = None
        db.commit()
        print(curseur.rowcount, "record(s) affected")
    curseur.close()
    db.close()

    return result
