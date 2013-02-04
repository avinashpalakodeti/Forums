import datetime
from google.appengine.ext import db
from google.appengine.api import users
from cryptacular.crypt import CRYPTPasswordManager, SHA256CRYPT
#from models import ModelMixin


class User(db.Model):
	password = db.StringProperty()
	email = db.EmailProperty()

	@classmethod
	def create(cls,username,password):
		u = cls(email=username,password=password)
		u.put()