import sublime
import base64

SETTNIGS_FILE = 'SubTexting.sublime-settings'

def set_pref(key, val):
	pref = sublime.load_settings(SETTNIGS_FILE)
	pref.set(key, val)
	sublime.save_settings(SETTNIGS_FILE)

def get_pref(key):
	return sublime.load_settings(SETTNIGS_FILE).get(key)

def get_basic_http_auth_string():
	u_and_p = base64.encodestring(bytes('%s:%s' % (get_pref('username'), get_pref('key')), 'utf-8')).decode('utf-8').replace('\n', '')
	return ('Basic %s' % u_and_p)