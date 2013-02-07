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
	def get(self,topic):
		t = Topic.get(topic)
		user = User.get(self.session['current_user'])
		comments = [comment for comment in t.comment_set.run()]
		self.render_response('comments.html',topic=t,comments=comments)
	
	def post(self,topic):
		user = User.get(self.session['current_user'])
		comment = self.request.POST['comment']
		Comment.create(user,comment,topic)
		self.redirect('/comments/create/'+topic)
		
