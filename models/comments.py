import datetime
from google.appengine.ext import db
from google.appengine.api import users
from cryptacular.crypt import CRYPTPasswordManager, SHA256CRYPT
from models.user import User
from models.topics import Topic

class Comment(db.Model):
	comment = db.TextProperty()
	user = db.ReferenceProperty(User)
	topic =db.ReferenceProperty(Topic)
	created_at = db.DateTimeProperty(auto_now=True)

	@classmethod
	def create(cls,userkey,topic,topickey):
		 t = Topic.get(topickey)
		 b = cls(user=userkey,comment=topic,topic=t)
		 b.put()

	@classmethod
	def update(cls,key,topic):
		c = Comment.get(key)
		c.comment = topic
		c.put()

	@classmethod
	def delete(cls,key,comment):
		c = Comment.get(key)
		c.delete()