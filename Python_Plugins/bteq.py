import sublime, sublime_plugin,fileinput,subprocess,os,threading


class BteqCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		thread1 = myThread(1,"BTEQ",1,self.view)
		thread1.start()

class myThread (threading.Thread):
	def __init__(self, threadID, name, counter,view):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		self.view = view;
	
	def run(self):
		print ("Starting " + self.name)
		self.view.window().show_input_panel("Parameter File Location","",self.runbteq,"","")
		print ("Exiting " + self.name)

	def runbteq(self,user_input):
		bteqFileName = self.view.file_name()
		parmFile = user_input
		fi = fileinput.input(files=parmFile)
		bteqFile = self.view.substr(sublime.Region(0,self.view.size()))
		for line in fi:
			parsed_line = line.split("=")
			parm_name = parsed_line[0]
			parm_value = parsed_line[1].replace("\n","")
			bteqFile=bteqFile.replace("${"+parm_name+"}",parm_value)
		fp = open(bteqFileName+"TEMP","w+")
		fp.write(bteqFile)
		tempFileName = fp.name
		LogFile = bteqFileName+".log"
		open(LogFile,"a")
		sublime.active_window().open_file(LogFile);
		subprocess.check_call("C:\\PROGRA~2\\Teradata\\Client\\15.10\\bin\\bteq < "+tempFileName+" > "+LogFile,shell=True)
		fp.close()
		os.remove(tempFileName)

