import anvil.server
from anvil.tables import app_tables

class Registration(app_tables.registration.Row):
  """ this is a model class"""
  @property
  def get_reg_date(self):
      pass