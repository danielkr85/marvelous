import sublime
import sublime_plugin
import datetime
import threading
import tempfile
import teradata
import os
import sys
import traceback


class executesqlCommand(sublime_plugin.TextCommand):

	def run(self,edit):
		
		self.sql = self.view.substr(self.view.sel()[0])
		self.environments = ['Dev','Test','Prod']
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
		try:

			filename = tempfile.gettempdir()+'\\answerset.sql'
			fp = open(filename,'wb+')

			environment = '${'+self.environment+'}'
			home='C:'+os.environ['HOMEPATH']
			udaExec = teradata.UdaExec (systemConfigFile=home+"\\AppData\\Roaming\\Sublime Text 3\\Packages\\teradata\\udaexec.ini",logFile=tempfile.gettempdir()+"\${appName}.${runNumber}.log")
			session = udaExec.connect(environment, password="$$tdwallet(td_credential)")
			result = session.execute(self.sqlcommand)

			columns=[]
			for column in result.description:
				columns.append(column[0])
			fp.write(','.join(columns))

			for record in result:
				row=[]
				for item in record:
					row.append(str(item))
				fp.write(','.join(row))



			sublime.active_window().status_message("Success!")
			newview = sublime.active_window().open_file(filename)
			
			
		except Exception as e:
			print(sys.exc_info()[0])
			sublime.active_window().status_message("Failure :-(")
			traceback.print_exc(file=sys.stdout)
		print ("Exiting " + self.name)









