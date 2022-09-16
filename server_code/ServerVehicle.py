import anvil.secrets
import anvil.email
import anvil.http
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime, timedelta
from .ModuleVehicle import JSONEncoder
from pymongo import MongoClient
import json

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.

## Anvil server sessions ( put inside a method)
#anvil.server.session.get('something', 0)
#anvil.server.session['something'] = "value"
## example session variable
#@anvil.server.callable
#def check_password(password):
 # if password == "MY SECRET":
   # anvil.server.session["authenticated"] = True

## Anvil server cookies
# anvil.server.cookie.local (app only); anvil.server.cookies.shared ( all apps ahare this)
#anvil.server.cookies.local['vehicle'] = 'Subaru Forester'

@anvil.server.callable
def add_new_vehicle(new_vehicle_dict):
  row = app_tables.vehicles.add_row(**new_vehicle_dict)
  return row
  

@anvil.server.callable
def get_vehicle_maint():
  """ rest_api  get / call """
  return app_tables.vehicle_maint.search()
  
  
@anvil.server.callable
def add_vehicle_maint(vehicle_dict):
   if vehicle_dict['driver'] and vehicle_dict['vehicle']:
     row = app_tables.vehicle_maint.add_row(**vehicle_dict)
     return row
    
@anvil.server.callable
def update_vehicle(vehicle_row, vehicle_dict):
  # check that the article given is really a row in the ‘articles’ table
  if app_tables.vehicle_maint.has_row(vehicle_row):
    vehicle_dict['updated'] = datetime.now()    # row will be automatically created if not exist
    print(vehicle_dict)
    vehicle_row.update(**vehicle_dict)
  else:
    raise Exception('Vehicle does not exist')
                    
@anvil.server.callable
def delete_vehicle(vehicle_row):
  # check that the article being deleted exists in the Data Table
  if app_tables.vehicle_maint.has_row(vehicle_row):
    vehicle_row.delete()
  else:
    raise Exception("Vehicle does not exist")

@anvil.server.callable
def get_vehicles():
  """ get * vehicles from db"""
  return app_tables.vehicle_maint.search()

@anvil.server.callable
def get_vin(vehicle_row):
  """  get vehicle vin """
  #car = self.item['vehicle'] ## server modules have no self. 
  #car_row =  [ x['vin'] for x in app_tables.vehicle_maint.search(vehicle=self.item['vin'])]
  return car_row
  
    
# Scheduled Tasks here ....
@anvil.server.background_task
def alert_upcoming_inspections():
  """ check for upcoming inspection due  """
  vehicles_soon = [ (x['driver'], x['inspection'] ) for x in app_tables.vehicle_maint.search(
       inspection=q.between(
       datetime.now().date(),
       datetime.now().date() + timedelta(days=30)
  ))]
  
  print(f"Car: {vehicles_soon[0][1].strftime('%m-%d-%Y')}")
  #for vehicle in vehicles_soon:
  anvil.email.send(
      from_name="Vehicle Maintenance", 
      to=["99jeffbrown100@gmail.com","michaelharning@gmail.com","7169829009@vtext.com"],
      subject="Inspection Due ...",
      text=f"Owner: {vehicles_soon[0][0]}\nInspection Due: {vehicles_soon[0][1]}"
  )
  #vehicle['reminder_sent'] = True
  
  ## HTTP-ENDPOINTS HERE 
@anvil.server.http_endpoint('/getveh')
def get_coll():
  """ get recs from pymongo """
  atlas_secret = anvil.secrets.get_secret('atlas_secret')
  #print(atlas_secret)
  client = MongoClient(f"mongodb+srv://jbrow57:{atlas_secret}@cluster0.4q4rz.mongodb.net/")
  db = client.for_anvil
  #collection = client.coll_for_anvil
  #coll =  db.list_collection_names()[0]
  ret_dict = db.coll_for_anvil.find_one()
  response = JSONEncoder().encode(ret_dict)
  #response_json = json.encode(resp, cls=JSONEncoder)

  response = anvil.server.HttpResponse(200, response)
  response.headers['Content-Type'] = 'application/json'
  return response
  