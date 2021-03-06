import sublime, sublime_plugin, threading, urllib, json
from .src import util
import imp

SETTINGS_FILE = "SubTexting.sublime-settings"	

class LoadContactsCommand(sublime_plugin.ApplicationCommand):

	def run(self):
		imp.reload(util)
		loader = ContactLoader(SETTINGS_FILE)
		loader.start()

class ContactLoader(threading.Thread):
	def __init__(self, settings_file):
		threading.Thread.__init__(self)
		self.settings_file = settings_file

	def run(self):
		sublime_settings = sublime.load_settings(SETTINGS_FILE) 

		contact_list = self.get_contacts() 

		sublime_settings.set('contact_list', contact_list)
		sublime.save_settings(SETTINGS_FILE)

		sublime.status_message('Loaded %d contacts.' % len(contact_list))


	def get_contacts(self):

		req = urllib.request.Request('http://%s/contacts' % util.get_host(), headers={'Authorization': util.get_auth_token()})

		res = urllib.request.urlopen(req)
		if res.code == 200:
			contact_list = json.loads(res.read().decode('utf-8'))
			return contact_list['contact_list']
		else:
			return {}
