import gi
import math
import time
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GdkPixbuf
import cairo


class MouseButtons:

	LEFT_BUTTON = 1
	RIGHT_BUTTON = 3
class Brush():
    def __init__(self, width, rgba_color):
        self.width = width
        self.rgba_color = rgba_color
        self.stroke = []

    def add_point(self, point):
        self.stroke.append(point)

class colorPicker(Gtk.Window):
	def __init__(self):
		window = Gtk.Window()
		self.color = Gdk.RGBA(red=1, green=1, blue=1, alpha=1)
		window.connect("destroy", Gtk.main_quit)

		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		window.add(box)
		self.window = window

		self.colorchooser = Gtk.ColorChooserWidget(show_editor=True)
		box.add(self.colorchooser)
	
		# self.entry = Gtk.Entry(text='0.5, 0.5, 0.5, 1.0')
		# box.add(self.entry)
		button = Gtk.Button(label="Select Color")
		button.connect("clicked", self.on_button_clicked)
		box.add(button)

	def on_button_clicked(self,button):
		print(self.colorchooser.get_rgba())
		# values = [float(v) for v in self.entry.get_text().split(',')]
		# self.colorchooser.set_rgba(Gdk.RGBA(*values))
		self.color = self.colorchooser.get_rgba()
		self.callback(self.color)
		self.window.hide()
		# self.colorchooser.set_property("show-editor", True)

	def action(self,function):
		self.callback = function
		self.window.show_all()

class Options(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="Tools")
		self.colors = colorPicker()
		self.set_border_width(10)
		self.function = 0
		self.rgba = self.colors.color
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		hbox = Gtk.Box(spacing=6)
		self.add(vbox)
		self.entry = Gtk.Entry()    

		button = Gtk.Button.new_with_label("Brush")
		button.connect("clicked", self.brush)
		hbox.pack_start(button, True, True, 0)

		button = Gtk.Button.new_with_label("Line")
		button.connect("clicked", self.line)
		hbox.pack_start(button, True, True, 0)

		button = Gtk.Button.new_with_mnemonic("Circle")
		button.connect("clicked", self.circle)
		hbox.pack_start(button, True, True, 0)

		button = Gtk.Button.new_with_mnemonic("Rectangle")
		button.connect("clicked", self.rectangle)
		hbox.pack_start(button, True, True, 0)

		# button = Gtk.Button.new_with_mnemonic("Get")
		# button.connect("clicked", self.on_text_entry)
		# hbox.pack_start(button, True, True, 0)

		button = Gtk.Button.new_with_mnemonic("Color")
		button.connect("clicked", self.openColorsPallete)
		hbox.pack_start(button, True, True, 0)
		
		button = Gtk.Button.new_with_mnemonic("_Close")
		button.connect("clicked", self.on_close_clicked)
		hbox.pack_start(button, True, True, 0)
		vbox.pack_start(hbox, True, True, 0)
		# vbox.pack_start(self.entry, True, True, 0)

	def openColorsPallete(self,button):
		self.colors.action(self.setColor);
	
	def setColor(self,color):
		self.rgba = color

	def brush(self, button):
		self.function = 0
		print(self.function)

	def line(self, button):
		self.function = 1
		dialog = Gtk.MessageDialog(self,0,Gtk.MessageType.INFO,Gtk.ButtonsType.OK,"Important Info")
		dialog.format_secondary_text("Click on two locations to draw a line and see the effect")
		dialog.run()
		print("INFO dialog closed")
		dialog.destroy()
		print(self.function)

	def on_text_entry(self, button):
		print(self.entry.get_text())


	def circle(self, button):
		self.function = 2
		print(self.function)

	def rectangle(self, button):
		self.function = 3
		print(self.function)

	def on_close_clicked(self, button):
		print("Closing application")
		Gtk.main_quit()

		
