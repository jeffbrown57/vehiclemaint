from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def link_vin_click(self, **event_args):
    """This method is called when the link is clicked"""
    #data_row = anvil.server.call('get_vin', self.item['vehicle'])
    data_row = app_tables.vehicle_maint.get(vin=)
    #self.auto_display_data
    if data_row:
      Notification(f"<b>Vehicle Vin:</b> <font color='blue'> {data_row} </font>").show()
    #except TypeError:
    #  Notification("No Vin data supplied.").show()
    #print(data_row)
    pass

  

