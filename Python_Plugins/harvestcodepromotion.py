import sublime
import sublime_plugin
import subprocess
import datetime
import threading

class harvestcodepromotionCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.usernamePrompt()

	def usernamePrompt(self):
		self.window.show_input_panel("Username","",self.environmentPrompt,"","") 

	def environmentPrompt(self,userinput):
		self.username = userinput
		self.environments = ['Dev','Test','Test_IP','Prod','Prod_IP']
		self.window.show_quick_panel(self.environments, self.packagenamePrompt) 

	def packagenamePrompt(self,userinput):
		self.environment = self.environments[userinput]
		self.window.show_input_panel("Package Name","",self.packagetypePrompt,"","") 

	def packagetypePrompt(self,userinput):
		self.packagename = userinput
		self.packagetypes = ['INFORMATICA','DIPERL_FILES','SCRIPTS']
		self.window.show_quick_panel(self.packagetypes, self.implementationtimePrompt)
		

	def implementationtimePrompt(self,userinput):
		self.packagetype = self.packagetypes[userinput]

		if datetime.datetime.now().hour <10:
			hour = "0"+str(datetime.datetime.now().hour)
		else:
			hour = str(datetime.datetime.now().hour)

		if datetime.datetime.now().minute <10:
			minute = "0"+str(datetime.datetime.now().minute)
		else:
			minute = str(datetime.datetime.now().minute)

		if datetime.datetime.now().day <10:
			day = "0"+str(datetime.datetime.now().day)
		else:
			day = str(datetime.datetime.now().day)

		if datetime.datetime.now().month <10:
			month = "0"+str(datetime.datetime.now().month)
		else:
			month = str(datetime.datetime.now().month)	

		self.window.show_input_panel("Implementation Time",str(datetime.datetime.now().year) +"-"+month+"-"+day+" "+hour+":"+minute+":00",self.runcommand,"","") 

	def runcommand(self,userinput):
		self.implementationtime = userinput
		sqlcommand = "EXEC RPT_INFA_DB.Harvest_Package_Promotion_Macro ('"+self.packagename+"','"+self.username+"','"+self.packagetype+"','"+self.implementationtime+"');"
		print(sqlcommand)
		thread1 = myThread1(1,"Thread-1",1,self.username,self.environment,sqlcommand)
		thread1.start()

class myThread1 (threading.Thread):
	def __init__(self, threadID, name, counter,username,environment,sqlcommand):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		self.username = username
		self.environment = environment
		self.sqlcommand = sqlcommand

	def run(self):
		print ("Starting " + self.name)
		command = 'python "C:\\Users\\roberd7\\AppData\\Roaming\\Sublime Text 3\\Packages\\Python_Plugins\\python_query_module.txt" -e '+self.environment+' -s "'+self.sqlcommand +'"'
		CREATE_NO_WINDOW = 0x08000000
		print (command)
		try:
			returncode = subprocess.check_call(command,creationflags=CREATE_NO_WINDOW)
			if (returncode==0):
				sublime.active_window().status_message("Success!")
			else:
				sublime.active_window().status_message("Failure :-(")
		except:
			sublime.active_window().status_message("Failure :-(")
		print ("Exiting " + self.name)