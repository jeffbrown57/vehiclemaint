from ._anvil_designer import HomePageTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..VehicleEdit import VehicleEdit
from ..NewVehicleAdd import NewVehicleAdd
from ..VehicleReport import VehicleReport

anvil.google.auth.login()

class HomePage(HomePageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # must use call_js on custom html form
    address = anvil.js.call("getText('http://192.168.1.50:8000/name.html')") 
    self.label_addr.text = address
    self.refresh_vehicles()
    
    # Any code you write here will run when the form opens.
    self.label_user.text = anvil.google.auth.get_user_email()
    self.repeating_panel_1.items = anvil.server.call('get_vehicle_maint')
    self.repeating_panel_1.set_event_handler('x-delete-vehicle', self.delete_vehicle)
    self.repeating_panel_1.set_event_handler('x-refresh-vehicles', self.refresh_vehicles)
    
  def refresh_vehicles(self):
    """ refesh the repeating_panel ***"""
    self.repeating_panel_1.items = anvil.server.call('get_vehicle_maint')

  def button_maint_click(self, **event_args):
    """This method is called when the button is clicked"""
    #from ..VehicleEdit import VehicleEdit
    vehicle_dict = {}
    
    save_clicked = alert(
      content = VehicleEdit(item = vehicle_dict),
      large = True,
      title = 'Add Maintenance Record',
      buttons=[('Save', True),('Cancel', False)]
    )
    if save_clicked:
      row = anvil.server.call('add_vehicle_maint', vehicle_dict)
      if row:
        Notification('Thanks for submitting maintenance record.').show()
        self.refresh_data_bindings()
        self.refresh_vehicles()
    pass
  
  
  def delete_vehicle(self, vehicle, **event_args):
    # Delete the vehicle
    anvil.server.call('delete_vehicle', vehicle)
    self.refresh_vehicles()

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    from ..FunForm import FunForm
    form = FunForm()
    open_form(form)
    pass

  def button_addcar_click(self, **event_args):
    """This method is called when the button is clicked"""
    new_vehicle = {}
    
    save_clicked = alert(
      content = NewVehicleAdd(item = new_vehicle),
      title = 'Add New Vehicle',
      large = True,
      buttons = [('Save', True),('Cancel', False)]
    )
    if save_clicked:
      anvil.server.call('add_new_vehicle', new_vehicle)
      Notification("Vehicles Updated (Add) !!").show()
    pass

  def button_report_click(self, **event_args):
    """This method is called when the button is clicked"""
    form = VehicleReport()
    open_form(form)   
    pass





