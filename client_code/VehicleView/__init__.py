from ._anvil_designer import VehicleViewTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..VehicleEdit import VehicleEdit

class VehicleView(VehicleViewTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    costx = self.item['cost']
    print(type(costx))
    if ( type(costx) == 'float' ) :
      cost_fix = f"{round(costx,2)}"
      self.label_cost.text = cost_fix

    # Any code you write here will run when the form opens.

  def button_edit_click(self, **event_args):
    """This method is called when the button is clicked"""
    vehicle_copy = dict(self.item)
    
    save_clicked = alert(
      content = VehicleEdit(item=vehicle_copy),
      title = 'Edit Vehicle Record',
      large = True,
      buttons=[('Save', True),('Cancel', False)]
    )
    if save_clicked:
      row = anvil.server.call('update_vehicle', self.item, vehicle_copy)
      print(f"Item -> : {self.item}")
      self.refresh_data_bindings()
      if row:
        Notification('Vehicle record updated.').show()
        
  def button_delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    if confirm("Are you sure you want to delete {}?".format(self.item['vehicle'])):
      self.parent.raise_event('x-delete-vehicle', vehicle=self.item)

    pass


