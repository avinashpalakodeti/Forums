import datetime
from google.appengine.ext import db
from google.appengine.api import users
from models.user import User
from cryptacular.crypt import CRYPTPasswordManager, SHA256CRYPT

class Topic(db.Model):
	name = db.StringProperty()
	description = db.TextProperty()
	user = db.ReferenceProperty(User)


	@classmethod
	def create(cls,user,topic):
		 b = cls(user=user,name=topic)
		 b.put()

	@classmethod
	def update(cls,key,comment):
		c = Topic.get(key)
		c.name = comment
		c.put()

	@classmethod
	def delete(cls,key,comment):
		c = Topic.get(key)
		c.delete()

