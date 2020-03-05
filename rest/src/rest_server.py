from wsgiref.simple_server import make_server
from pyramid.config import Configurator
import json

def get_location(req):
  with open('database.txt','r') as db_file:
    location = json.load(db_file)
  return location

def modify_location(req):
  location = get(location(req))
  if 'latitude' in location:
    location['latitude'] = req.POST['latitude']
  else:
    print("no lat key in db file")
  if 'longitude' in location:
    location['longitude'] = req.POST['longitude']
  else:
    print("no long key in db file")
  with open('database.txt','w') as db_file:
    json.dumps(location, db_file)
  return location

if __name__ == '__main__':
  config = Configurator()

  config.add_route('rest_route', '/location')
  config.add_view(get_location, route_name='rest_route', renderer='json')
  config.add_view(modify_location, route_name='rest_route', renderer='json', request_method='POST')

  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 5000, app)
  server.serve_forever()