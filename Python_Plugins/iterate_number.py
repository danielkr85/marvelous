import sublime, sublime_plugin

class iterate_numberCommand(sublime_plugin.TextCommand):

	def run(self, edit):

		self.numberStr = self.view.substr(self.view.sel()[0])	;
		self.numberInt = int(self.numberStr);
		self.view.window().show_input_panel("Iterations:","",self.iterate,"","");

	def iterate(self,user_input):
		self.Iterations = int(user_input);
		self.my_list=list(range(self.numberInt,self.numberInt+self.Iterations+1));
		self.output= '\n'.join(str(x) for x in self.my_list);
		self.view.run_command("insertiteration",{'args':self.output});


class insertiterationCommand(sublime_plugin.TextCommand):

	def run(self, edit,args):
		self.edit=edit;
		self.output=args;
		print(self.output);
		self.view.erase(self.edit,self.view.sel()[0]);
		self.view.insert(self.edit,self.view.sel()[0].a,self.output);