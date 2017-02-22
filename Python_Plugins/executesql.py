import sublime
import sublime_plugin
import datetime
import threading
import tempfile
import subprocess
import os


class executesqlCommand(sublime_plugin.TextCommand):

	def run(self,edit):
		
		self.sql = self.view.substr(self.view.sel()[0])
		self.environments = ['Dev','Test','Prod','Prod_IP']
		self.view.window().show_quick_panel(self.environments, self.runcommand) 

	def runcommand(self,userinput):
		self.environment = self.environments[userinput]
		
		thread1 = myThread1(1,"Thread-1",1,self.environment,self.sql)
		thread1.start()
		

class myThread1 (threading.Thread):
	def __init__(self, threadID, name, counter,environment,sqlcommand):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter
		self.environment = environment
		self.sqlcommand = sqlcommand
		print(sqlcommand)

	def run(self):
		print ("Starting " + self.name)
		CREATE_NO_WINDOW = 0x08000000
		command = ('python "'+os.environ["APPDATA"]+'\\Sublime Text 3\\Packages\\Python_Plugins\\python_query_module.txt" -e '+self.environment+' -s "'+self.sqlcommand+'"')
		print(command)
		try:

			filename = tempfile.gettempdir()+'\\answerset.sql'
			fp = open(filename,'wb+')
			output = subprocess.check_output(command,creationflags=CREATE_NO_WINDOW)
			fp.write(output)
			fp.close
			
			newview = sublime.active_window().open_file(filename)
			sublime.active_window().status_message("Success!")
		except CalledProcessError as e:

			print(e.returncode)
			sublime.active_window().status_message("Failure :-(")

		print ("Exiting " + self.name)









