import sqlite3
import os
from os.path import abspath, curdir
import re
import urwid


#global variables
conn=sqlite3.connect("")
curr=""

#start with the interface?
class BUDGET:
	
	def __init__(self, file_location):
		self.file='./'+file_location
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
		cat_query="SELECT cat_name, budget_amount, transactions, remainder_amount FROM catergories"
		#go through results
		rows=[("Catergory","Budgeted","Transactions","Remaining")]
		curr.execute(cat_query)
		for a in curr.fetchall():
			rows.append(a)
		#print results
		returned_text=""
		for a in rows:
			temp_str=""
			for b in a:
				x=str(b)
				temp_str+=x.ljust(13," ")
			#print(temp_str)
			returned_text+=temp_str
		return returned_text
		
	def close(self):
		conn.close()
		print(self.file+" has been closed.\n Goodbye.")

#Load files
def load_database_choices(title):
	body = [urwid.Text(title), urwid.Divider()]
	for a in os.listdir(curdir):
		if bool(re.search('.db', a, re.IGNORECASE)):
			button = urwid.Button(a)
			urwid.connect_signal=(button, 'click', load_database, a)
			body.append(urwid.AttrMap(button, None, focus_map='reversed'))
	return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def load_database(button, choice):
	#budget=BUDGET(file_location=choice)
	response = urwid.Text(choice+"\n loaded")
	done = urwid.Button('OK')
	urwid.connect_signal(done, 'click', show_budget)
	main.orignal_widget = urwid.Filler(urwid.Pile([response, urwid.AttrMap(done, None, focus_map='reversed')]))

#exit program
def exit_on_q(key):
	if key in ('q','Q'):
		budget.close()
		raise urwid.ExitMainLoop()

#load the budget up
def show_budget():
	bud = urwid.Text(budget.print_cats())
	main.original_widget=urwid.Filler(bud)
	
##MAIN LOOP
budget=BUDGET(file_location='dummy.db')
main = urwid.Padding(load_database_choices("Jess's Budget"), left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill('\N{MEDIUM SHADE}'),
	align = 'center', width=('relative', 60),
	valign = 'middle', height=('relative', 60),
	min_width=20, min_height=9)
urwid.MainLoop(top, palette=[('reversed','standout','')]).run()
	
		
				