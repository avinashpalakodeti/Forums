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

class Create(BaseHandler):
	def get(self):
		self.render_response('topics.html')

	def post(self):
		user = User.get(self.session['current_user'])
		topic = self.request.POST['topic']
		desc = self.request.POST['description']
		Topic.create(user,topic,desc)
		self.redirect('/')