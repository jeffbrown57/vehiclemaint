import anvil.server
import anvil.tables
from anvil.tables import app_tables

class Registration(app_tables.registration.Row):
  """ this is a model class"""

  for veh in app_tables.registration.search():
    print(f"{veh['vehicle']} registration is  due{veh.date}")