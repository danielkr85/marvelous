import sublime, sublime_plugin

class AddcommasCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.substr(self.view.sel()[0])	
		selection = selection.replace("\n",",\n")
		self.view.erase(edit,self.view.sel()[0])
		self.view.insert(edit,self.view.sel()[0].a,selection)