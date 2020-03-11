from Api.connect import connect
from Api.sql_columns import sql_columns


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
      #  print("ereurr")
       # db.rollback()

    curseur.close()
    db.close()

