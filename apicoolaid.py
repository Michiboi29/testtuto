from Api.createsql import sql_create
from Api.readsql import sql_read
from Api.insertsql import sql_insert_ami, sql_insert


sql_insert_ami(nom='mich', prenom='etienne', age=20)
sql_insert_ami(prenom='bob', age=20, nom='tremblay')

#sql_insert('EMPLOYEE', LAST_NAME='beaulieu', FIRST_NAME='michel')

sql_read("SELECT * FROM ami")
