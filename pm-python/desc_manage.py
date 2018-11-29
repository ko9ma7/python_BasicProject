from sqlite_orm.database import Database
from sqlite_orm.field import IntegerField, BooleanField, TextField
from sqlite_orm.table import BaseTable
from passlib.hash import pbkdf2_sha256
import ntplib
from time import ctime
import logging

class Manage(BaseTable):
    __table_name__='users'
    #index, site_name, site_url,user_id, user_pw, date, content
    idx = IntegerField(primary_key=True, auto_increment=True)
    site_name = TextField(not_null=True)
    site_url = TextField()
    user_id = TextField(not_null=True)
    user_pw = TextField(not_null=True)
    content = TextField()
    date = TextField()

    def verify_login(self, _password):
        return pbkdf2_sha256.verify(_password, self.user_pw)

if __name__=="__main__":
    #logger configure:
    logging.basicConfig(filename="C:/Users/namki/Desktop/python_BasicProject/pm-python/error.log", level=logging.DEBUG, format=('%(asctime)s: '
                                                                            '%(filename)s: '
                                                                            '%(levelname)s: '
                                                                            '%(funcName)s(): '
                                                                            '%(lineno)d: '
                                                                            '%(message)s'), datefmt="%Y-%m-%d %H:%M:%S")
                        
    with Database("C:/Users/namki/Desktop/python_BasicProject/pm-python/shadow.db") as db:
        try:
            c = ntplib.NTPClient()
            response = c.request('europe.pool.ntp.org',version=3)
            print(ctime(response.tx_time)) #�ð����
        except ntplib.NTPException:
            print(ctime())
        
        #���̺� ����
        #db.query(Manage).create().execute()

        #�����ͺ��̽� ��ü ����
        #user1 = Manage(site_name="naver",site_url="www.naver.com",user_id="rltmd1004",user_pw="0000",content='',date=ctime(response.tx_time))
        
        #�����ͺ��̽� ��ü insert
        #db.query().insert(user1).execute()
        
        #select ��¹�
        for row in db.query(Manage).select().execute():
            print(row)
        print(pbkdf2_sha256.hash("asd"))
