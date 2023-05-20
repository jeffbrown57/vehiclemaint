from ._anvil_designer import VehicleEditTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil.js.window import fetchText

class VehicleEdit(VehicleEditTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)    

    # Any code you write here will run when the form opens.
    self.drop_down_driver.items = [ x['name'] for x in app_tables.owners.search()]
    self.drop_down_vehicle.items = [ x['name'] for x in app_tables.vehicles.search()]
    self.label_3.visible = False
    if  fetchText():
      self.label_3.visible = True
      self.label_3.text = fetchText()

  def date_picker_inspect_change(self, **event_args):
      """This method is called when the selected date changes"""
      pass
