from source_file import SourceFile, SourceClass, SourceMethod, SourceField, SourceParameter

class JavaFile(SourceFile):
	def __init__(self, name, classes):
		super().__init__(name)
		self.classes = classes  # List of JavaClass objects

	def __str__(self):
		classes_str = "\n".join(str(c) for c in self.classes)
		return f'JavaFile: {self.name}\nClasses:\n{classes_str}'

class JavaClass(SourceClass):
	def __init__(self, name, methods, fields):
		super().__init__(name)
		self.methods = methods  # List of JavaMethod objects
		self.fields = fields  # List of JavaField objects

	def __str__(self):
		methods_str = "\n".join(str(m) for m in self.methods)
		fields_str = "\n".join(str(f) for f in self.fields)
		return f'JavaClass: {self.name}\nMethods:\n{methods_str}\nFields:\n{fields_str}'

class JavaMethod(SourceMethod):
	def __init__(self, name, return_type, parameters, body):
		super().__init__(name)
		self.return_type = return_type
		self.parameters = parameters  # List of JavaParameter objects
		self.body = body  # String representing method body

	def __str__(self):
		parameters_str = ", ".join(str(p) for p in self.parameters)
		return f'JavaMethod: {self.name}\nReturn Type: {self.return_type}\nParameters: {parameters_str}\nBody: {self.body}'

class JavaField(SourceField):
	def __init__(self, name, field_type):
		super().__init__(name)
		self.field_type = field_type

	def __str__(self):
		return f'JavaField: {self.name}\nType: {self.field_type}'

class JavaParameter(SourceParameter):
	def __init__(self, name, param_type):
		super().__init__(name)
		self.param_type = param_type

	def __str__(self):
		return f'JavaParameter: {self.name}\nType: {self.param_type}'