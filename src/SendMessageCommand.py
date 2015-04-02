import sublime, sublime_plugin

class SendMessageCommand(sublime_plugin.WindowCommand):

	username = 'will'
	password = 'brazil'

	def run(self):
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
		gcm_url = 'https://android.googleapis.com/gcm/send'

		headers = {
			#'Authorization': self.api_key,
			'Content-Type': 'application/json'
		}

		body = {
			#"registration_ids" : [self.device_id],
			"data" : {
				"command" : "send_message",
				"to_local_id": 0,
				"message_body" : body
			},
		}

		#data = json.dumps(body)
		#data = data.encode('utf-8')
		#req = urllib.request.Request(gcm_url, data, headers)
		#response = urllib.request.urlopen(req)

		sublime.status_message('Message sent!')