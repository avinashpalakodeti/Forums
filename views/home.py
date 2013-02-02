from views import BaseHandler
import webapp2
from google.appengine.ext import db

class Login(BaseHandler):
	def get(self):
		self.render_response('login.html')
	def post(self):
		username = self.request.POST['username']
		password = self.request.POST['password']
		print username


class Signup(BaseHandler):
	def get(self):
		self.render_response('signup.html')


class Main(BaseHandler):
	def get(self):
		self.render_response('main.html')

class Tags(BaseHandler):
	def post(self):
		tag = self.request.POST['tag']
		self.render_response("tags.html",tag=tag)

class Comments(BaseHandler):
	def get(self):
		self.render_response('comments.html')