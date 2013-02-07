from views import BaseHandler
import logging as log
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext.blobstore import BlobInfo
from cryptacular.crypt import CRYPTPasswordManager, SHA256CRYPT
import urllib
from models.user import User
from models.topics import Topic
from models.comments import Comment
import webapp2
import re
from webapp2_extras import json
from google.appengine.ext import db

class Login(BaseHandler):
	def post(self):
		username = self.request.POST['username']
		password = self.request.POST['password']
		user = User.gql("where email = :1",username)
		user = user.get()
		if user is None:
			self.session.add_flash("Invalid Username!",key='error')
			self.redirect("/login")
		else:
			manager = CRYPTPasswordManager(SHA256CRYPT)
			if manager.check(user.password,password):
				self.session["current_user"] = str(user.key())
				self.redirect("/")
			else:
				self.session.add_flash("Invalid Password!",key='error')
				self.redirect("/login")
		
	def get(self):
		self.render_response('login.html')



class Signup(BaseHandler):
	def get(self):
		self.render_response('signup.html')

	def post(self):
		username = self.request.POST['username']
		passwor = self.request.POST['password']
		gender = self.request.POST['sex']
		manager = CRYPTPasswordManager(SHA256CRYPT)
		password=manager.encode(passwor)
				
		if re.match("^[a-zA-Z0-9._%-]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$", username) != None:
			
			q = db.GqlQuery("SELECT * from User where email = :1",username)
			a = q.get()			
			if a is not None:
				self.session.add_flash("Username already exists!",key='error')
				self.redirect("/signup")
			else:
				User.create(username,password,gender)
				self.redirect("/login")
		else:
			self.session.add_flash("Enter valid email!",key='error')
			self.redirect("/signup")


class Logout(BaseHandler):
	def get(self):
		if self.session.has_key('current_user'):
			del self.session['current_user']
		self.redirect("/login")


class Main(BaseHandler):
	def get(self):
		user = User.get(self.session['current_user'])
		topics = Topic.all()			
		self.render_response('main.html',user=user,topics=topics)


class TopicHandle(BaseHandler):
	pass

class Tags(BaseHandler):
	def get(self):
		self.render_response('tags.html')
	def post(self):
		tag = self.request.POST['tag']
		self.render_response("tags.html",tag=tag)

class Comments(BaseHandler):
	def get(self):
		self.render_response('comments.html')


class Contact(BaseHandler):
	def get(self):
		self.render_response('contactus.html')