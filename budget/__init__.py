import sys
from os import path
import sqlite3


class Budget:
    def __init__(self):
        self.file_location = ""

    def Open(self, file_loc):
        self.file_location = path.abspath(file_loc)
        self.conn = sqlite3.connect(self.file_location)
        self.curr = self.conn.cursor()
        # debug line
        print(self.file_location)
        print("File opened")

    def Close(self):
        self.conn.close()
        # debug line
        print("File Closed")

    def add_tran(self, account, date, catergory="", description="", amount=0):
        insert_string = "INSERT INTO transactions VALUES(acc_id, catergory, description, trans_date, amount)" \
                        "(%s,\'%s\',\'%s\',\'%s\',%s)" % (account, date, catergory, description, amount)
        # debug line
        print(insert_string)
        self.curr.execute(insert_string)

    def delete_tran(self, tran_id):
        delete_string = "DELETE FROM transactions WHERE trans_id = %s" % tran_id
        # debug line
        print(delete_string)
        self.curr.execute(delete_string)

    def show_cats(self, date_stamp):
        select_string = "SELECT cat_name, budget_amount, transactions, remainder_amount" \
                        " FROM catergories WHERE cat_date like \'"+date_stamp+"%\'"

        print(select_string)
        self.curr.execute(select_string)
        returned_cats = self.curr.fetchall()
        return returned_cats
