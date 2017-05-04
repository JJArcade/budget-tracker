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

    def add_tran(self, account, date, catergory="", description="", amount=0):
        insert_string = "INSERT INTO transactions VALUES(acc_id, catergory, description, trans_date, amount)" \
                      "(%s,\'%s\',\'%s\',\'%s\',%s)" % (account,date,catergory,description,amount)
        self.curr.execute(insert_string)

    def delete_tran(self, tran_id):
        delete_string = "DELETE FROM transactions WHERE trans_id = %s" % tran_id
        self.curr.execute(delete_string)

    def show_cats(self, date_stamp):
        select_string = "SELECT cat_name, budget_amount, transaction_amount, remainder_amount" \
                      "FROM catergories WHERE cat_date =\'%s\'"
        self.curr.execute(select_string)


