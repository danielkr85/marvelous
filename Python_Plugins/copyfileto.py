import sublime
import sublime_plugin
from shutil import copyfile

class copyfiletoCommand(sublime_plugin.WindowCommand):
	def run(self, paths):
		self.paths = paths;
		self.window.show_input_panel("Target directory:",sublime.get_clipboard(500),self.copy,"","");
		
	def copy(self,user_input):
		self.target = user_input
		for path in self.paths:
			self.filename = path.split("\\")[-1]
			try:
				copyfile(self.paths[0],self.target+"\\"+self.filename)
				sublime.active_window().status_message("Success!")
			except:
				sublime.active_window().status_message("Failed :-(")
		