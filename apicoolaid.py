from Api.createsql import sql_create
from Api.readsql import sql_read
from Api.insertsql import sql_insert_ami, sql_insert
from Api.dropsql import sql_drop

sql_create()
#sql_insert_ami(prenom='etienne', nom='mich', age=20)
#sql_insert_ami(prenom='bob', sex='M')

sql_insert('EMPLOYEE', FIRST_NAME='michel', LAST_NAME='beaulieu')

#sql_read('ami', "SELECT * FROM ami")
#sql_drop('ami')
#sql_read("SELECT * FROM ami")
