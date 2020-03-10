from Api.createsql import sql_create
from Api.readsql import sql_read
from Api.insertsql import sql_insert


sql_insert('ami', 'prenom', 'nom', 'age', 'sex', s='etienne', s1='michaud', d=20, c='M')

sql_read("SELECT * FROM EMPLOYEE \
       WHERE INCOME > '%d' AND AGE < '%d'", 50, 1000)
