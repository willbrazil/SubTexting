import sublime

SETTNIGS_FILE = 'SubTexting.sublime-settings'

def set_pref(key, val):
	pref = sublime.load_settings(SETTNIGS_FILE)
	pref.set(key, val)
	sublime.save_settings(SETTNIGS_FILE)

def get_pref(key):
	return sublime.load_settings(SETTNIGS_FILE).get(key)