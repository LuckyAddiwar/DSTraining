import sqlite3

class updatedata:
    def __init__(self):
        self.conn = sqlite3.connect("sms.db")
        self.cur = self.conn.cursor()

    def updatestudent(self,sid,sname,email,city):
        self.cur.execute(
            f'''
            UPDATE STUDENT SET
            sname = "{sname}",
            email = "{email}",
            city = "{city}"
            WHERE sid = {sid}
            '''
        )
        self.conn.commit()
        print("Data updated successfully")

    def updatecourse(self,cid,coursename,sid,price):
        self.cur.execute(
            f'''
            UPDATE COURSE SET
            coursename = "{coursename}",
            sid = "{sid}",
            price = "{price}"
            WHERE cid = {cid}
        ''')
        self.conn.commit()
        print("Data updated successfully")

    def updatetranscation(self,tid,sid,cid,price):
        self.cur.execute(
            f'''
            UPDATE TRANSCATION SET
            sid = {sid},
            cid = {cid},
            price = "{price}"
            WHERE tid = {tid}
        ''')
        self.conn.commit()
        print("Data updated successfully")
