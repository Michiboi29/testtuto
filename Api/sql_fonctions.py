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
    if not checkTableExists(table_name):
        print('table ' + table_name + ' drop!')


def sql_update(table_name, set, valset, where=None):

    sql = "UPDATE {0} \
            SET {1} = %s"
    sql = sql.format(table_name, set)

    if where is not None:
        where = " WHERE " + where
    sql += where

    valset = [valset]
    print(sql, valset)

    db = connect()
    curseur = db.cursor()
    curseur.execute(sql, valset)
    db.commit()
    print(curseur.rowcount, "record(s) affected")

    curseur.close()
    db.close()


def sql_read(table_name, select="*", distinct=False, where=None):

    dist = " "
    if distinct:
        dist = " DISTINCT "

    sql = "SELECT{1}{0} FROM {2}".format(select, dist, table_name)

    if where is not None:
        where = " WHERE " + where
        sql += where

    print("Reads:", sql)

    colomns = sql_columns(table_name)
    if select != "*":
        colomns = []
        sections = select.split()
        sections.append("fin")
        for col in sections:
            if col == "fin":
                break
            if sections[(sections.index(col) + 1)] != "AS" and col != "AS":
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
        if i == "FROM":
            f = True

    opperation = cmd.split()[0]

    curseur.execute(cmd)
    if opperation == "SELECT":
        f = False
        s = False
        select = ""
        for i in cmd.split():
            if i == "FROM":
                f = True
            if s and not f:
                select += " " + i
            if i == "SELECT":
                s = True

        colomns = sql_columns(table_name)
        sections = select.split()
        if sections[0] != "*" and sections[0] != "DISTINCT":
            colomns = []
            sections.append("fin")
            for col in sections:
                if col == "fin":
                    break
                if sections[(sections.index(col) + 1)] != "AS" and col != "AS":
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
