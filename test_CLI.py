import sqlite3
import os
from os.path import abspath, curdir
import re
import urwid

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
def menu(title, choices):
	body = [urwid.Text(title), urwid.Divider()]
	for c in choices:
		button = urwid.Button(c)
		urwid.connect_signal(button,'click',item_chosen,c)
		body.append(urwid.AttrMap(button, None, focus_map='reversed'))
	return urwid.ListBox(urwid.SimpleFocusListWalker(body))

def item_chosen(button, choice):
	response = urwid.Text(['You chose ', choice, '\n'])
	done = urwid.Button('Ok')
	urwid.connect_signal(done, 'click', exit_program)
	main.original_widget = urwid.Filler(urwid.Pile([response, urwid.AttrMap(done, None, focus_map='reversed')]))


def show_budget(path):
	budget=BUDGET(file_location=path)
	bud = budget.

def exit_program(button):
	raise urwid.ExitMainLoop()

choices=[]
for a in os.listdir('.'):
	if bool(re.search('db', a)):
		choices.append(a)

main = urwid.Padding(menu('Budget',choices),left=2,right=2)
top = urwid.Overlay(main, urwid.SolidFill('\N{MEDIUM SHADE}'),
	align='center', width=('relative',60),
	valign='middle',height=('relative',60),
	min_width=20, min_height=9)
urwid.MainLoop(top,palette=[('reversed','standout','')]).run()
