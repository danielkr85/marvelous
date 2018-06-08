import sublime, sublime_plugin,fileinput,subprocess,os


class bigiparmCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		
		self.view.window().show_input_panel("Parameter File Location",self.view.file_name(),self.update,"","")


	def update(self,user_input):
		bteqFileName = self.view.file_name()
		parmFile = user_input
		fi = fileinput.input(files=parmFile)
		bteqFile = self.view.substr(sublime.Region(0,self.view.size()))
		for line in fi:
			parsed_line = line.split("\t")
			parm_name = parsed_line[0]
			parm_value = parsed_line[1].replace("\n","")
			bteqFile=bteqFile.replace("~>"+parm_name,parm_value)
		fp = open(bteqFileName+"TEMP.bteq","w+")
		fp.write(bteqFile)
		sublime.active_window().open_file(fp.name);
		fp.close()
		os.remove(tempFileName)