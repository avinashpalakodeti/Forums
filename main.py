import webapp2
import webapp2_local
from views import home

route = [
  webapp2.Route(r'/', handler=home.Main, name='main'),
  webapp2.Route(r'/login', handler=home.Login),
  webapp2.Route(r'/signup', handler=home.Signup),
  webapp2.Route(r'/tags', handler=home.Tags),
  webapp2.Route(r'/comments', handler=home.Comments)
  ]

config = {}
config['webapp2_extras.sessions'] = {
  'secret_key': 'asdfasdfasdfasdfasf12341234213412341asdfasdfasdf4werwer',
}

app = webapp2.WSGIApplication(route, config=config)
app.router.set_dispatcher(webapp2_local.custom_dispatcher)

