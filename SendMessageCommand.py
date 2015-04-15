import sublime, sublime_plugin, urllib, json
from .src import util
import imp
class SendMessageCommand(sublime_plugin.WindowCommand):

	def run(self):
		imp.reload(util)
		self.contacts = self.get_contact_list()
		self.names = list(self.contacts.keys())
		self.pick_to_address()

	def get_contact_list(self):
		return sublime.load_settings('SubTexting.sublime-settings').get('contact_list')

	def pick_to_address(self):
		self.window.show_quick_panel(self.names, self.handle_addressed_picked)	

	def handle_addressed_picked(self, index):
		if index >= 0 :
			self.selected_contact = {'name' : self.names[index], 'local_id' : self.contacts[self.names[index]]}
			self.get_msg_body()

	def get_msg_body(self):
		self.window.show_input_panel(self.selected_contact['name'], "", lambda content: self.send_msg(self.selected_contact['local_id'], content), None, None)

	def send_msg(self, to_address, body):
		gcm_url = 'http://%s/send' % util.get_pref('host')

		body = {
			'to_local_id': to_address,
			'message_body': body
		}
		print(util.get_basic_http_auth_string())

		data = urllib.parse.urlencode(body).encode('utf-8')
		req = urllib.request.Request(gcm_url, data, headers={'Authorization': util.get_basic_http_auth_string()})
		response = urllib.request.urlopen(req)
		if response.code == 200:
			sublime.status_message('Message sent!')
		else:
			sublime.status_message('Failed to send message.')