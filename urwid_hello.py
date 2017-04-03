import urwid

def exit_on_q(key):
	if key in ('q','Q'):
		raise urwid.ExitMainLoop()

palette = [
	('banner','','','','#000','g75'),
	('streak','','','','#000','#f33'),
	('bg','','','','#000','#33f'),]

txt = urwid.Text(('banner', " Hello World "), align='center')
map1 = urwid.AttrMap(txt, 'streak')
fill = urwid.Filler(map1)
map2 = urwid.AttrMap(fill, 'bg')
loop = urwid.MainLoop(map2, palette, unhandled_input=exit_on_q)
loop.screen.set_terminal_properties(colors=256)
loop.run()
