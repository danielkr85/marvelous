import sublime, sublime_plugin,os


class renamefilesCommand(sublime_plugin.WindowCommand):

	paths = None
	input1 = None

	def run(self,paths):

		self.paths = paths;
		self.window.show_input_panel("String to Replace","",self.nextPrompt,"","");

	def nextPrompt(self,user_input):

		self.input1 = user_input;
		self.window.show_input_panel("Replace with","",self.replacefilename,"","")

	def replacefilename(self,user_input):
		
		for path in self.paths:
			splitpath = path.split('\\')
			filename = splitpath.pop(-1) #-1 removes last of array
			# splitfilename = filename.split('.')
			# extension = splitfilename.pop(-1) 
			# filename = '.'.join(splitfilename)
			newfilename = filename.replace(self.input1,user_input)
			# newfilename = newfilename +'.'+extension
			splitpath.append(newfilename)
			newpath = '\\'.join(splitpath)
			os.rename(path,newpath)
