import sqlite3
import os
from os.path import abspath, curdir
import re

#global variables
conn=sqlite3.connect("")
curr=""

#start with the interface?
class BUDGET:
	
	def __init__(self, file_location):
		self.file=file_location
		self.setup()
	
	def setup(self):
		conn = sqlite3.connect(self.file)
		curr = conn.cursor()
		curr.execute("PRAGMA foreign_keys=ON;")
		curr.fetchall()	

	def save(self):
		conn.commit()

	def print_cats(self):
		#get all the relevant info
		conn = sqlite3.connect(self.file)
		curr=conn.cursor()
		cat_query="SELECT cat_name, cat_
		curr.execute(cat_query)
	def close(self):
		conn.close()
		print(self.file+" has been closed.\n Goodbye.")

def __main__():
	file_selected=False
	paths=[]
	while not file_selected:
		for a in os.listdir(curdir):
			db_found=bool(re.search('.db',a,re.IGNORECASE))
			if db_found:
				temp_path=abspath(curdir)+'/%s' % a
				print(temp_path)	#debug line
				paths.append(temp_path)
		i=1
		for a in paths:
			temp_print="%d)".ljust(5," ") %i
			temp_print+=a
			print(temp_print)
			i+=1
		pick = input("please enter the number of the DB to load.\n")
		budget = BUDGET(file_location=paths[int(pick)-1])
		file_selected=True
	budget.print_cats()

__main__()
				
