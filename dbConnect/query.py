import pymysql
#user data format:
#id    userName
class DBconnect:

    def query_user(login_id):
        conn = pymysql.connect(host='localhost',user='rowing',passwd='passwd',db='rowing_system',port=3306,charset='utf8')
        cur=conn.cursor()
        if cur.execute("select * from `users` where userName=%s"%(login_id)) > 0:
            cur.close()
            conn.close()
            return True
        else :
            cur.close()
            conn.close()
            return False