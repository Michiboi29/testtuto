from mysql.connector import MySQLConnection, Error
from Api.configsql import read_db_config


def connect():
    db_config = read_db_config()
    db_name = db_config['database']

    temp_conn = MySQLConnection(
        host=db_config['host'],
        user=db_config['user'],
        passwd=db_config['password']
    )

    temp_cur = temp_conn.cursor()
    temp_cur.execute("CREATE DATABASE IF NOT EXISTS %s" % db_name)

    temp_cur.close()
    temp_conn.close()

    conn = None
    try:
        #print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        '''if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')'''

    except Error as error:
        print(error)

    return conn
