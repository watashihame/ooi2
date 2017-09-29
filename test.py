from DbConnect.query import DbQuery
dbc = DbQuery('localhost',3306,'row','deepdarkfantasy','row')
print(dbc.update('watashihame@163.com'))
dbc.close()
