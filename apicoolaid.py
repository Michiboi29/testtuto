from Api.createsql import sql_create
from Api.sql_fonctions import sql_delete, sql_comand, sql_drop, sql_update, sql_insert, sql_read

sql_drop('EMPLOYEE')
sql_create()
sql_insert('ami', prenom='bob', nom='landrie', age=12)
sql_update('ami', where="nom = 'laprise' AND age < 30", prenom="max", age=20)
sql_read(table_name='ami', select="COUNT(prenom) AS nbr_prenom_masculin, sex", groupby='sex', orderby='sex', where="sex IS NOT NULL")
#sql_delete('ami', "sex IS NULL")
sql_comand("SELECT DISTINCT * FROM AMI")
