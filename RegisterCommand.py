import sublime, sublime_plugin, urllib.parse, urllib.request
from SubTexting.src import util
import imp

class RegisterCommand(sublime_plugin.WindowCommand):
	def run(self):
		imp.reload(util)
		self.phone = None
		self.username = None
		self.get_username()

	def get_username(self, error_msg=''):
		self.window.show_input_panel("%s Username: " % error_msg, '', self.handle_username, None, None)

	def handle_username(self, content):
		if content == '':
			self.get_username('(Cannot be empty)')
		else:
			self.username = content
			self.get_phone()

	def get_phone(self, error_msg=''):
		self.window.show_input_panel("%s Phone (we will NOT store your number!): " % error_msg, '5745142948', self.handle_phone, None, None)

	def handle_phone(self, content):
		if len(content) != 10:
			self.get_phone('(Invalid number)')
		else:
			self.phone = content
			self.register()

	def register(self):
		data = {'username': self.username, 'phone': self.phone}
		res = urllib.request.urlopen('http://localhost:5000/signup', data=urllib.parse.urlencode(data).encode('utf-8'))
		res_data = res.read().decode('utf-8')
		if res_data == 'OK':
			util.set_pref('username', self.username)
			util.set_pref('phone', self.phone)
			sublime.message_dialog('A verification text has been sent to your phone. Please run "CTRL+SHIFT+P -> Verify" once you have the code.')
		else:
			sublime.message_dialog(res_data)