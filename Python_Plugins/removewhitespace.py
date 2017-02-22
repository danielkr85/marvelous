import sublime, sublime_plugin

class RemovewhitespaceCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		string = self.view.substr(self.view.sel()[0])
		strings = string.split('\n')
		string = ''
		for st in strings:
			st = st.strip()+'\n'
			string = string+st
		self.view.erase(edit,self.view.sel()[0])
		self.view.insert(edit,self.view.sel()[0].a,string)