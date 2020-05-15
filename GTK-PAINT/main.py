from tools import *
from inputs import *



class Paint(Gtk.Window):
	def __init__(self):
		super(Paint, self).__init__()
		self.allocation = {"width":500,"height":500}
		self.functions_dict = {0:self.on_draw,1:self.line_draw,2:self.draw_circle,3:self.draw_rectangle}
		self.init_ui()
		self.win = Options()
		self.win.connect("destroy", Gtk.main_quit)
		self.set_default_size(self.allocation["width"],self.allocation["height"])
		self.win.show_all()
		self.inpC = InputCircle() ; self.inpC.connect("destroy", Gtk.main_quit)
		self.inpR = InputRectangle() ; self.inpR.connect("destroy", Gtk.main_quit)
		self.brushes = []
		self.set_resizable( False )
		self.win.set_resizable(False)
		self.inpC.set_resizable(False)
		self.inpR.set_resizable(False)



	def init_ui(self):
		self.darea = Gtk.DrawingArea()
		self.trigger = 0
		self.darea.connect("draw", self.draw)
		css_provider = Gtk.CssProvider()
		# css_provider.load_from_path("./style.css")

		# Gtk.StyleContext.add_provider_for_screen(
		# 	Gdk.Screen.get_default(),
		# 	css_provider,
		# 	Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		

		
		self.darea.set_events(self.darea.get_events() |
            Gdk.EventMask.BUTTON_PRESS_MASK |
            Gdk.EventMask.POINTER_MOTION_MASK)
		self.add(self.darea)

		self.coords = []
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
			cr.set_line_width(2)
			# cr.set_line_cap(2)
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
			# for i in range(0, len(self.coords) - 1):
			i = - 2
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
		print(len,bred)
		cr.set_source_surface(self.img, 0, 0)
		color = self.win.rgba
		rgba_color = (color.red,color.green,color.blue,color.alpha)
		cr.set_source_rgba(*rgba_color)
		cr.set_line_width(2)
		sx,sy = self.coords[-1]
		sx = self.coords[-1][0]
		sy = self.coords[-1][1]
		# cr.translate(sx,sy)
		cr.rectangle(sx,sy,len,bred)
		cr.stroke_preserve()	
		self.darea.queue_draw()

		
	def on_button_press(self, w, e):
		if e.type == Gdk.EventType.BUTTON_PRESS \
			and e.button == MouseButtons.LEFT_BUTTON:
			cr = cairo.Context(self.img)
			if (self.win.function == 0):
				self.coords = []
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
	
