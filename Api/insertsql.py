from Api.connect import connect


def sql_insert_ami(**atributs):
    atributs_list = ['prenom', 'nom', 'age', 'sex']
    atributs_dict = dict(zip(atributs_list, ['NULL'] * len(atributs_list)))
    for i, j in atributs.items():
        atributs_dict[i] = j
    format_dict = atributs_dict
    for i, j in atributs_dict.items():
        if j != 'NULL':
            format_dict[i] = '%s'

    val = tuple(atributs.values())
    sql = """INSERT INTO ami(prenom, nom, age, sex) VALUES ({prenom}, {nom}, {age}, {sex})"""
    sql = sql.format(**format_dict)
    print(sql, val)

    db = connect()
    curseur = db.cursor()
    curseur.execute(sql, val)
    db.commit()
    print(curseur.rowcount, "record inserted.")

    #except:
      #  print("errrrrreeeeeur")
      #  db.rollback()

    curseur.close()
    db.close()


"""def sql_insert(table_name, **atributs):
    

    atributs_list = list(atributs)
    atributs_str = ""
    values = list(atributs.values())
    val = ""
    for i in values:
        val += '{' + i + '}'
        if values.index(i) < len(values) - 1:
            val += ', '
    for i in atributs_list:
        atributs_str += i
        if atributs_list.index(i) < len(atributs_list) - 1:
            atributs_str += ', '
    db = connect()
    curseur = db.cursor()

    sql = "INSERT INTO " + table_name + " (" + atributs_str + ") \
       VALUES (" + val + ")"
    print(sql)
    print(atributs)
    sql_formate = sql.format(**atributs)
    print(sql_formate)
    try:
        curseur.execute(sql_formate)
        db.commit()
        print(curseur.rowcount, "record inserted.")
    except:
        print("ereurr")
        db.rollback()

    curseur.close()
    db.close()
"""
