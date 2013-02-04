""" 
simple implementation of an utility class
to add common methods to all models for basic CRUD operations and queries with pagination etc.
"""
class ModelMixin(object):

	""" returns a list of properites of the class """
	@classmethod
	def get_properties(cls):
		return cls.properties().keys()


	""" method to create a record in datastore"""
	@classmethod
	def create(cls,request):
		c = cls()
		for i in cls.get_properties():
			setattr(cls,i,request.post[i])
		cls.put()
		return c


	""" method to update a record in datastore"""
	@classmethod
	def update(cls,request):
		c = cls.get(request.POST['key'])
		for i in cls.get_properties():
			setattr(cls,i,request.post[i])
		c.put() 
		return c


	@classmethod
	def delete(cls,request):
		c = cls.get(request.POST['key'])
		c.delete()
		pass

	""" an utility method to make paginated queries """
	@classmethod
	def paginate(cls):
		pass
		
