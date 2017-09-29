import pymysql

class DbQuery:
    def __init__(self, _host, _port, _user, _password, _db):
        self.conn = pymysql.connect(host = _host,port = _port,user = _user,password = _password,db = _db)
        self.cursor = self.conn.cursor()

    def query(self, login_id):
        self.cursor.execute('SELECT * FROM `user` WHERE `mail`=\'' + login_id + '\'')
        res = self.cursor.fetchall()
        #print(res)
        if res.__len__() > 0:
            state = True
        else:
            state = False
        return state

    def update(self, login_id):
        try:
            self.cursor.execute('UPDATE `user` SET `visit` = `visit` + 1 WHERE `mail` = \'' + login_id + '\'')
            self.conn.commit()
        except:
            print ('error: fail to add visit times')

    def close(self):
        self.conn.close()

