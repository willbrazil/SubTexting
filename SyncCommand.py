import sublime, sublime_plugin, threading, sched, time

class SyncCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		thread = MessageSync(5, self.view, edit)
		thread.start()
		#self.view.insert(edit, 0, "Hello, World!")

class MessageSync(threading.Thread):
	def __init__(self, timeout, view, edit):
		self.timeout = timeout
		self.result = None
		self.view = view
		self.edit = edit
		threading.Thread.__init__(self)
		self.message_animation = NewMessageAnimation() 

	def run(self):
		self.message_animation.start()
		print(self.view.file_name())
		#self.view.insert(self.edit, 0, "Inside thread!")
		#self.result = 'Hey!!!!!!!'

class NewMessageAnimation(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		self.display_eye_catcher(1)
		#self.display_anim_frame(1)

	def display_eye_catcher(self, frame):
		spaces = frame % 200
		message_prefix = ' '*spaces 
		sublime.status_message("%s( ͡° ͜ʖ ͡°)" % message_prefix);
		s = sched.scheduler(time.time, time.sleep)
		s.enter(0.03, 1, self.display_eye_catcher, (frame+1,))
		if frame < 200:
			s.run()
		else:
			self.display_anim_frame(1) 
		

	def display_anim_frame(self, frame):
		spaces = frame % 50
		message_prefix = ' '*spaces 
		sublime.status_message("%s ツ NEW MESSAGE ツ" % message_prefix);
		s = sched.scheduler(time.time, time.sleep)
		s.enter(0.07, 1, self.display_anim_frame, (frame+1,))
		if frame < 100:
			s.run() 
		

