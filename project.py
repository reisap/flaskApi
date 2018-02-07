import uuid

class Project:
	__name = None
	__start_date = None
	__end_date = None
	__id = None
	__description = None

	def __init__(self,name,start_date,end_date,description):
		self.__id= uuid.uuid4()
		self.__name = name
		self.__start_date = start_date
		self.__end_date = end_date
		self.__description = description

	#
	# PROPERTIES
	#
	@property
	def id(self):
    	return self.__id

	@property
	def name(self):
    	return self.__name

	@name.setter
	def name(self,value):
    	self.__name = value

	@property
	def start_date(self):
    	return self.__start_date

	@start_date.setter
	def start_date(self,value):
    	self.__start_date = value
