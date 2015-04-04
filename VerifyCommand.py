import sublime, sublime_plugin
import urllib
from .src import util

class VerifyCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.get_code()

  def get_code(self, error_msg=''):
    self.window.show_input_panel('%s Verification code: ' % error_msg, '', self.handle_code, None, None)

  def handle_code(self, content):
    if(len(content) > 0 and self.is_valid(content)):
      util.set_pref('key', content)
      sublime.message_dialog('Success!')
    else:
      self.get_code('(Invalid code)')

  def is_valid(self, code):
    data = {'username': util.get_pref('username'), 'code': code}
    data = urllib.parse.urlencode(data).encode('utf-8')
    res = urllib.request.urlopen('http://localhost:5000/verify', data)
    if res.code == 200:
      if 'OK' in res.read().decode('utf-8'):
        return True
      else:
        return False
    else:
      False # we should throw an error here eventually.