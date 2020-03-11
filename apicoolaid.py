from Api.createsql import sql_create
from Api.readsql import sql_read
from Api.insertsql import sql_insert_ami, sql_insert
from Api.dropsql import sql_drop
from Api.updatesql import sql_update

sql_drop('EMPLOYEE')
sql_create()
#sql_insert_ami(prenom='etienne', nom='mich', age=20)
#sql_insert_ami(prenom='bob', sex='M')

sql_insert('ami', prenom='guillaume', nom='laprise', age=20)
sql_update('ami', 'prenom', "max", "nom = 'laprise' AND age < 30")
sql_read('ami', "SELECT DISTINCT * FROM ami")

#sql_read("SELECT * FROM ami")
