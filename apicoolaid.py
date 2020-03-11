from Api.createsql import sql_create
from Api.readsql import sql_read
from Api.insertsql import sql_insert_ami
from Api.dropsql import sql_drop


sql_insert_ami(prenom='etienne', nom='mich', age=20)
sql_insert_ami(prenom='bob', sex='M')

#sql_insert('EMPLOYEE', LAST_NAME='beaulieu', FIRST_NAME='michel')

sql_read('ami', "SELECT * FROM ami")
#sql_drop('ami')
#sql_read("SELECT * FROM ami")
