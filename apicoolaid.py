from Api.createsql import sql_create
from Api.sql_fonctions import sql_delete, sql_comand, sql_drop, sql_update, sql_insert, sql_read

sql_drop('EMPLOYEE')
sql_create()
#sql_insert_ami(prenom='etienne', nom='mich', age=20)
#sql_insert_ami(prenom='bob', sex='M')

sql_insert('ami', prenom='guillaume', nom='laprise', age=20)
sql_update('ami', 'prenom', "max", "nom = 'laprise' AND age < 30")
sql_read('ami', True, "nom = 'mich'")
sql_delete('ami', 'nom IS NULL')
sql_comand('ami', "SELECT DISTINCT * FROM ami")
