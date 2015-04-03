import sublime, sublime_plugin, urllib.parse, urllib.request
from SubTexting.src import util
import imp

class RegisterCommand(sublime_plugin.WindowCommand):
	def run(self):
		imp.reload(util)
		print(util.get_pref('password'))
		self.username = None
		self.password = None
		self.get_username()

	def get_username(self, caption='Username: '):
		self.window.show_input_panel(caption, '', self.handle_username, None, None)

	def handle_username(self, content):
		if content == '':
			self.get_username('(Cannot be empty) Username: ')
		else:
			self.username = content
			self.get_password()

	def get_password(self, caption='Password: '):
		self.window.show_input_panel(caption, '', self.handle_password, None, None)

	def handle_password(self, content):
		if content == '':
			self.get_password('(Cannot be empty) Password: ')
		else:
			self.password = content
			self.register()

	def register(self):
		sublime.status_message("%s:%s" % (self.username, self.password))

		data = {'username': self.username}
		res = urllib.request.urlopen('http://localhost:5000/signup', data=urllib.parse.urlencode(data).encode('utf-8'))
		res_data = res.read().decode('utf-8')
		if res_data == 'OK':
			util.set_pref('username', self.username)
			util.set_pref('password', self.password)
			sublime.message_dialog('Successfully Registered!')
		else:
			sublime.message_dialog(res_data)