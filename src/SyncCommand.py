import sublime, sublime_plugin, threading, sched, time, urllib.request as urllib2, json

class SyncCommand(sublime_plugin.ApplicationCommand):

	def __init__(self):
		self.running = False

	def run(self):
		if self.running:
			print("Already running.")
		else:
			print('Started.')
			thread = MessageSync(5)
			thread.start()
			self.running = True
		#self.view.insert(edit, 0, "Hello, World!")

class MessageSync(threading.Thread):

	def __init__(self, timeout):
		self.timeout = timeout
		self.result = None
		threading.Thread.__init__(self)
		self.message_animation = NewMessageAnimation()
		self.s = sched.scheduler(time.time, time.sleep)
		self.last_message = ''
		self.message_from = ''

	def run(self):	
		self.ping()
		#self.view.insert(self.edit, 0, "Inside thread!")
		#self.result = 'Hey!!!!!!!'

	def ping(self):
		if self.has_new_message():
	 		NewMessageAnimation().display_eye_catcher(1, self.message_from, self.last_message)

		self.s.enter(2, 1, self.ping, ())
		#self.s.run()

	def has_new_message(self):
		res = urllib2.urlopen('http://localhost:5000')
		if res.code == 200:
			res_body = json.loads(res.read().decode('utf-8'))
			if res_body['message_count'] > 0:
				self.last_message = res_body['messages'][0]['body']
				self.message_from = res_body['messages'][0]['from']
				return True
		return False

class NewMessageAnimation():

	def display_eye_catcher(self, frame, message_from, message_body):
		spaces = frame % 100
		message_prefix = ' '*spaces 
		sublime.status_message("%s( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°) ( ͡° ͜ʖ ͡°)" % message_prefix);
		s = sched.scheduler(time.time, time.sleep)
		s.enter(0.02, 1, self.display_eye_catcher, (frame+1, message_from, message_body))
		if frame < 100:
			s.run()
		else:
			self.display_anim_frame(1, message_from, message_body) 
		

	def display_anim_frame(self, frame, message_from, message_body):
		spaces = frame % 50
		message_prefix = ' '*spaces 
		sublime.status_message("%s %s:\"%s\"    --    ツ NEW MESSAGE ツ   --  CTRL+SHIT+R to respond" % (message_prefix, message_from, message_body));
		s = sched.scheduler(time.time, time.sleep)
		s.enter(0.1, 1, self.display_anim_frame, (frame+1, message_from, message_body))
		if frame < 100:
			s.run() 
		

