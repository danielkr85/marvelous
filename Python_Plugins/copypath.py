import sublime, sublime_plugin

class copypathCommand(sublime_plugin.ApplicationCommand):
	def run(self,paths):
		sublime.set_clipboard(paths[0])
		sublime.active_window().status_message(paths[0] + " has been copied to clipboard.")