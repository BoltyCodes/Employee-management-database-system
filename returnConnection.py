import mysql.connector as m1

def returnConnection():
        mycon = m1.connect(host='127.0.0.1',user="root",password='admin',database='company')
        return mycon


	
