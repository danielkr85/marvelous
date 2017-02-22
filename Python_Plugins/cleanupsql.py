import sublime, sublime_plugin, re

class CleanupsqlCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		selection = self.view.substr(self.view.sel()[0])	
		selection = re.sub(",(?!\n)",",\n",selection)
		selection = selection.replace("FROM","\n FROM")
		selection = selection.replace("WHERE","\n WHERE")
		selection = selection.replace("AND","\n AND")
		selection = selection.replace("ON","\n ON")
		selection = selection.replace("RIGHT OUTER JOIN","\n RIGHT OUTER JOIN")
		selection = selection.replace("INNER JOIN","\n INNER JOIN")
		selection = selection.replace("LEFT OUTER JOIN","\n LEFT OUTER JOIN")
		selection = selection.replace("GROUP BY","\n GROUP BY \n")
		selection = selection.replace("SELECT","\n SELECT \n")


		string = selection
		strings = string.split('\n')
		string = ''
		for st in strings:
			st = st.strip()+'\n'
			string = string+st
		self.view.erase(edit,self.view.sel()[0])
		self.view.insert(edit,self.view.sel()[0].a,string)
		

