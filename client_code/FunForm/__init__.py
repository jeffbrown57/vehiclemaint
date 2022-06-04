from ._anvil_designer import FunFormTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class FunForm(FunFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    from ..HomePage import HomePage
    form = HomePage()
    open_form(form)
    pass

