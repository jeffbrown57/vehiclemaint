from ._anvil_designer import VehicleSummaryTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
#from ..VehicleView import VehicleView

class VehicleSummary(VehicleSummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.label_1.text = f"Driver: {self.item['driver']}"
    self.label_2.text = f"Vehicle: {self.item['vehicle']}"
    self.label_3.text = f"Registration: {self.item['registration']}"
    self.label_4.text = f"Inspection: {self.item['inspection']}"
    self.label_5.text = self.item['repairs']

  def button_edit_click(self, **event_args):
    """This method is called when the button is clicked"""
    from ...VehicleView import VehicleView
    vehicle_copy = dict(self.item)
    save_clicked = alert(
      content = VehicleView(item = vehicle_copy),
      title = 'Edit Vehicle Record',
      large = True,
      buttons=[('Save', True),('Cancel', False)]
    )
    if save_clicked:
      anvil.server.call('update_vehicle', self.item, vehicle_copy)
      Notification("Vehicle record updated successfully").show()
    pass

