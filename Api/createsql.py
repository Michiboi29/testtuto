from Api.connect import connect


def sql_create():
    db = connect()
    curseur = db.cursor()

    tab1 = """CREATE TABLE IF NOT EXISTS EMPLOYEE (
             FIRST_NAME  VARCHAR(20),
             LAST_NAME VARCHAR(20),
             AGE INT,  
             SEX CHAR(1),
             INCOME FLOAT )"""
    curseur.execute(tab1)

    tab2 = """CREATE TABLE IF NOT EXISTS ami (
             prenom  VARCHAR(20) NOT NULL,
             nom  VARCHAR(20),
             age INT,  
             sex CHAR(1))"""
    curseur.execute(tab2)

    curseur.close()
    db.close()


sql_create()
