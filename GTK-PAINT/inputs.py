import gi
import math
import time
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import cairo

class InputCircle(Gtk.Window):
	def __init__(self):
		self.inp = 0
		Gtk.Window.__init__(self, title="Input Of Circle")
		self.set_border_width(10)
		self.function = 0
		self.trigger = None
		hbox = Gtk.Box(spacing=6)
		self.add(hbox)
		self.entry = Gtk.Entry()    
		hbox.pack_start(self.entry, True, True, 0)

		button = Gtk.Button.new_with_mnemonic("Submit")
		button.connect("clicked", self.submit)
		hbox.pack_start(button, True, True, 0)


		self.w = 0
		self.cr = 0
		self.e = 0
		self.darea = 0
		self.img = 0


	def action(self,w,cr,circle):
		self.trigger = circle
		self.w = w
		self.cr = cr
		self.show_all()

	def submit(self,button):
		self.inp = int(self.entry.get_text())
		self.hide()
		self.trigger(self.w,self.cr,self.inp)

	def get_inp(self):
		return self.inp



class InputCircle(Gtk.Window):
	def __init__(self):
		self.inp = 0
		Gtk.Window.__init__(self, title="Enter Radius of Circle")
		self.set_border_width(10)
		self.function = 0
		self.trigger = None
		hbox = Gtk.Box(spacing=6)
		self.add(hbox)
		self.entry = Gtk.Entry()
		hbox.pack_start(self.entry, True, True, 0)

		button = Gtk.Button.new_with_mnemonic("Submit")
		button.connect("clicked", self.submit)
		hbox.pack_start(button, True, True, 0)


	def action(self,w,cr,circle):
		self.trigger = circle
		self.w = w
		self.cr = cr
		self.entry.set_text("0")    
		self.show_all()

	def submit(self,button):
		self.inp = int(self.entry.get_text())
		self.hide()
		self.trigger(self.w,self.cr,self.inp)

	def get_inp(self):
		return self.inp


class InputRectangle(Gtk.Window):
	def __init__(self):
		self.len = 0
		self.bred = 0
		Gtk.Window.__init__(self, title="Enter Length and Breadth")
		self.set_border_width(10)
		self.function = 0
		self.trigger = None
		hbox = Gtk.Box(spacing=6)
		self.add(hbox)
		self.entryl = Gtk.Entry()    
		hbox.pack_start(self.entryl, True, True, 0)

		self.entryb = Gtk.Entry()    
		hbox.pack_start(self.entryb, True, True, 0)

		button = Gtk.Button.new_with_mnemonic("Submit")
		button.connect("clicked", self.submit)
		hbox.pack_start(button, True, True, 0)



	def action(self,w,cr,rectangle):
		self.trigger = rectangle
		self.w = w
		self.cr = cr
		self.entryl.set_text("0")    
		self.entryb.set_text("0")    
		self.show_all()

	def submit(self,button):
		self.len = int(self.entryl.get_text())
		self.bred = int(self.entryb.get_text())
		print(self.len,self.bred)
		self.hide()
		self.trigger(self.w,self.cr,self.len,self.bred)


	def get_inp(self):
		return self.inp
