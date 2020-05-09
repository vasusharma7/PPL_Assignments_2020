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
		Gtk.Window.__init__(self, title="Button Demo")
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

		button = Gtk.Button.new_with_mnemonic("_Close")
		button.connect("clicked", self.on_close_clicked)
		hbox.pack_start(button, True, True, 0)

		# button = Gtk.Button.new_with_mnemonic("Get")
		# button.connect("clicked", self.on_text_entry)
		# hbox.pack_start(button, True, True, 0)

		button = Gtk.Button.new_with_mnemonic("Color")
		button.connect("clicked", self.openColorsPallete)
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


class InputRectangle(Gtk.Window):
	def __init__(self):
		self.len = 0
		self.bred = 0
		Gtk.Window.__init__(self, title="Input Of Rectangle")
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
		self.show_all()

	def submit(self,button):
		self.len = int(self.entryl.get_text())
		self.bred = int(self.entryb.get_text())
		self.hide()
		self.trigger(self.w,self.cr,self.len,self.bred)

	def get_inp(self):
		return self.inp






class Paint(Gtk.Window):
	def __init__(self):
		super(Paint, self).__init__()
		self.functions_dict = {0:self.on_draw,1:self.line_draw,2:self.draw_circle,3:self.draw_rectangle}
		self.init_ui()
		self.win = Options()
		self.win.connect("destroy", Gtk.main_quit)
		self.win.show_all()
		self.inpC = InputCircle() ; self.inpC.connect("destroy", Gtk.main_quit)
		self.inpR = InputRectangle() ; self.inpR.connect("destroy", Gtk.main_quit)
		self.brushes = []



	def init_ui(self):
		self.darea = Gtk.DrawingArea()
		self.trigger = 0
		self.darea.connect("draw", self.draw)
		css_provider = Gtk.CssProvider()
		css_provider.load_from_path("./style.css")

		Gtk.StyleContext.add_provider_for_screen(
			Gdk.Screen.get_default(),
			css_provider,
			Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		

		
		self.darea.set_events(self.darea.get_events() |
            Gdk.EventMask.BUTTON_PRESS_MASK |
            Gdk.EventMask.POINTER_MOTION_MASK)
		self.add(self.darea)

		self.coords = []
		self.allocation = {"width":500,"height":400}
		# self.darea.connect("button-press-event", self.on_button_press)

		self.set_title("Paint")
		self.resize(self.allocation["width"],self.allocation["height"])

		self.set_position(Gtk.WindowPosition.CENTER)
		self.connect("delete-event", Gtk.main_quit)

		self.darea.connect("button-press-event", self.on_button_press)
		self.darea.connect("motion-notify-event", self.mouse_move)

		self.show_all()
		a = self.darea.get_allocation()

		print (a.x, a.y, a.width, a.height)

		self.img = cairo.ImageSurface(5, a.width, a.height)

	def draw(self,w,cr):
		cr.set_source_surface(self.img, 0, 0)
		cr.paint()

	def mouse_move(self, w, e):
		if (self.win.function != 0):
			return
		cr = cairo.Context(self.img)
		if e.state & Gdk.EventMask.BUTTON_PRESS_MASK:
			curr_brush = self.brushes[-1]
			curr_brush.add_point((e.x, e.y))
			cr.set_line_cap(0)
			self.on_draw(w,cr)
			# w.queue_draw()

	def on_draw(self, wid, cr):
		cr.set_source_surface(self.img, 0, 0)
		cr.paint()
		if self.win.function != 0:
			return
		color = self.win.rgba
		rgba_color = (color.red,color.green,color.blue,color.alpha)
		cr.set_source_rgba(*rgba_color)

		for brush in self.brushes[::-1]: 
			# cr.set_source_rgba(*brush.rgba_color)
			cr.set_line_width(brush.width)
			cr.set_line_cap(1)
			cr.set_line_join(cairo.LINE_JOIN_ROUND)
			cr.new_path()
			
			for x, y in brush.stroke:
				cr.line_to(x, y)
			cr.stroke()
			break
		self.darea.queue_draw()


	def line_draw(self, wid, cr,e):
		if self.win.function != 1:
			return
		cr.set_line_width(2)
		color = self.win.rgba
		rgba_color = (color.red,color.green,color.blue,color.alpha)
		cr.set_source_rgba(*rgba_color)

		self.coords.append([e.x, e.y])
		if len(self.coords) >= 2:
			for i in range(0, len(self.coords) - 1):
				# i = - 2
				j = i + 1
				c1 = self.coords[i]
				c2 = self.coords[j]
				cr.move_to(c1[0], c1[1])
				cr.line_to(c2[0], c2[1])
				# cr.stroke_preserve()
				# cr.fill()
				cr.stroke()

		self.darea.queue_draw()
		# del self.coords[:]
		
	def draw_circle(self, widget, cr,radius):
		cr.set_source_surface(self.img, 0, 0)
		cr.set_line_width(2)
		color = self.win.rgba
		rgba_color = (color.red,color.green,color.blue,color.alpha)
		cr.set_source_rgba(*rgba_color)
		
		cr.translate(self.coords[-1][0], self.coords[-1][1])
		cr.arc(0, 0, radius, 0, 2*math.pi)
		cr.stroke_preserve()	
			# cr.set_source_rgb(0.3, 0.4, 0.6)
			# cr.fill()
		# self.coords = []

		self.darea.queue_draw()


	def draw_rectangle(self, widget, cr,len,bred):
		print(self.coords)
		
		cr.set_source_surface(self.img, 0, 0)
		color = self.win.rgba
		rgba_color = (color.red,color.green,color.blue,color.alpha)
		cr.set_source_rgba(*rgba_color)
		cr.set_line_width(2)
		sx,sy = self.coords[-1]
		cr.translate(sx,sy)
		cr.rectangle(sx, sy, sx+len, sy+bred)
		cr.stroke_preserve()	
		self.darea.queue_draw()

		
	def on_button_press(self, w, e):
		if e.type == Gdk.EventType.BUTTON_PRESS \
			and e.button == MouseButtons.LEFT_BUTTON:
			cr = cairo.Context(self.img)
			
			if (self.win.function == 0):
				color = self.win.rgba
				rgba_color = (color.red,color.green,color.blue,color.alpha)
				cr.set_source_rgba(*rgba_color)
				print(rgba_color)
				brush = Brush(2, rgba_color)
				brush.add_point((e.x, e.y))
				self.brushes.append(brush)
				self.on_draw(w,cr)
				# w.queue_draw()
			if (self.win.function == 2):
				self.coords = []
				self.coords.append([e.x, e.y])
				self.inpC.action(w,cr,self.draw_circle)
			elif (self.win.function == 3):
				self.coords = []
				self.coords.append([e.x, e.y])
				print(self.coords)
				self.inpR.action(w,cr,self.draw_rectangle)
			elif (self.win.function == 1):
				self.line_draw(w, cr,e)


		self.darea.queue_draw()




def main():
	app = Paint()
	Gtk.main()




if __name__ == "__main__":
	main()
	
