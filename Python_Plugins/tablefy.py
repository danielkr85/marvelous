import sublime, sublime_plugin, re

class TablefyCommand(sublime_plugin.TextCommand):
	def run(self, edit):


		firstnl = re.compile('^.*\n')

		selection = self.view.substr(self.view.sel()[0])	

		selection = "|"+selection+"|"
		selection = selection.replace("\t","|")
		selection = selection.replace("\n","|\n|")

		firstnlM = firstnl.match(selection)

		if firstnlM:
			columns = len(firstnlM.group().split('|'))-2
			columnstr = "|--|"
			for x in range(1,columns):
				columnstr=columnstr+"--|"
			columnstr=columnstr+'\n'

			selection = selection.replace(firstnlM.group(),firstnlM.group()+columnstr)


		#selection = "'"+selection+"'"
		self.view.erase(edit,self.view.sel()[0])
		self.view.insert(edit,self.view.sel()[0].a,selection)

		