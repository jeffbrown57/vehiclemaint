from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from anvil_extras import augment

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    augment.set_event_handler(self.link_vin, 'hover', self.link_hover)

  def link_vin_click(self, **event_args):
    """This method is called when the link is clicked"""
    #data_row = anvil.server.call('get_vin', self.item['vehicle'])
    vehicle_row = app_tables.vehicle_maint.get(cost=self.item['cost'])
    #print(cost_row['vin']['vin'])
    x = vehicle_row['vin']['vin']
    #self.auto_display_data
    if x:
      Notification(f"<b>Vehicle Vin:</b> <font color='blue'> {x} </font>").show()
    #except TypeError:
    #  Notification("No Vin data supplied.").show()
    #print(data_row)
    pass

  def link_hover(self, **event_args):
    if 'enter' in event_args['event_type']:
      self.link_vin.text = 'Get Vin'
    else:
      self.link_vin.text = 'Get Vin_out'

  

