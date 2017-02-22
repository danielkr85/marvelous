import sublime, sublime_plugin,subprocess,threading,tempfile,os

class createundopackagesCommand(sublime_plugin.WindowCommand):
    def run(self,paths):
        self.paths = paths
        self.paths.sort()
        self.window.show_input_panel("Project","",self.createScriptFile,"","");
        

    def createScriptFile(self,user_input):
        Project = user_input
        self.scriptFile = tempfile.mkstemp()
        self.logFile = tempfile.mkstemp()
        f = open(self.scriptFile[1],'w')
        f.write('LOCK PROJECT"' +Project+'";')
        for file in self.paths:
            splitfile = file.split('.')
            splitfile.pop(-1)
            UndoFileName = '.'.join(splitfile)+'_Undo(DEV).mmp'
            Undo = 'CREATE UNDOPACKAGE LOCAL"'+UndoFileName+'"FOR PROJECT "'+Project +'" FROM PACKAGE LOCAL"'+file+'";\n'
            f.write(Undo)
        f.write('UNLOCK PROJECT"' +Project+'";')
        f.close()
        os.close(self.scriptFile[0])
        self.window.open_file(f.name)
        self.window.open_file(self.logFile[1])
        self.window.show_input_panel("Username","",self.passwordPrompt,"","");


    def passwordPrompt(self,user_input):
        self.username = user_input
        self.window.show_input_panel("Password","",self.projectSourcePrompt,"","");

    def projectSourcePrompt(self,user_input):
        self.password = user_input
        self.window.show_input_panel("Project Source","Development - elvmad746",self.runThread,"","");

    def runThread(self,user_input):
        self.projectSource = user_input
        thread1 = myThread1(1,"Thread-1",1,self.username,self.password,self.projectSource,self.scriptFile,self.logFile)
        thread1.start()


class myThread1 (threading.Thread):
    def __init__(self, threadID, name, counter,username,password,projectSource,scriptFile,logFile):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.username = username
        self.password = password
        self.projectSource = projectSource
        self.scriptFile = scriptFile
        self.logFile = logFile
        
    def run(self):
        print ("Starting " + self.name)
        command = 'cmdmgr.exe -n "'+self.projectSource+'" -u '+self.username+' -p '+self.password+' -f '+self.scriptFile[1]+' -o '+self.logFile[1]
        f = open(self.logFile[1],'w')
        f.write(command+'\n')
        f.write('Running Scipt \n')
        f.close()
        os.close(self.logFile[0])
        CREATE_NO_WINDOW = 0x08000000
        subprocess.check_call(command,creationflags=CREATE_NO_WINDOW)
        self.window.open_file(self.logFile[1])
        os.remove(self.logFile[1])
        os.remove(self.scriptFile[1])
        print ("Exiting " + self.name)