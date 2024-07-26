import sqlite3

class insertdata:
    def __init__(self):
        self.conn = sqlite3.connect("sms.db")
        self.cur = self.conn.cursor()

    def insertstudent(self,sid,sname,email,city):
        self.cur.execute(
            f'''
        INSERT INTO STUDENT VALUES(
        {sid},
        "{sname}",
        "{email}",
        "{city}"
        )
        '''
        )
        self.conn.commit()
        print("Data added successfully")

    def insertcourse(self, cid, coursename,sid,price):
        self.cur.execute(f'''
                         INSERT INTO COURSE VALUES(
                         {cid},
                         "{coursename}",
                         "{sid}",
                         "{price}"
                         )
                         ''')
        self.conn.commit()
        print("Data added successfully")

    def inserttranscation(self, tid,sid,cid,price):
        self.cur.execute(f'''
                        INSERT INTO TRANSCATION VALUES(
                        {tid},
                        {sid},
                        {cid},
                        {price}
                        )
                        ''')
        self.conn.commit()
        print("Data added successfully")