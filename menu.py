class Menu:
	def __init__(self,_it=[]):
		"""Initiate menu object with items _it (Optional)."""
		self.items=_it
		self.options={'space':' ','bullet':'-','tab':'\t','sep':'---','msg':'What would you like to do?'}
		self.level=0
	def add_submenu(self,_submenu_object):
		"""Add submenu _submenu_object to the menu's list of items."""
		_submenu_object.parent=self
		_submenu_object.level=self.level
		_submenu_object.options=self.options
		for each_item in _submenu_object.items:
			each_item.options = self.options
		self.items.append(_submenu_object)
		return self
	def add_menu_option(self,_menu_option_object):
		"""Add menu option _menu_option_object to the menu's list of items."""
		_menu_option_object.parent=self
		_menu_option_object.level=0
		_menu_option_object.options=self.options
		self.items.append(_menu_option_object)
		return self
	def display(self):
		"""Display the entire menu and all submenus."""
		for each_item in self.items:
			each_item.display()
	def listen(self):
		"""Listen for user input after displaying the menu listening message."""
		user_input = input(self.options['msg']+' ')
		action_check = None
		for each_item in self.items:
			action_check = each_item.check_input(user_input)
			if action_check is not None:
				action_check()
				return 0
		print("Sorry, that option wasn't in my list.")
		pass
class SubMenu():
	def __init__(self,_text='Empty submenu',_parent=None):
		"""Initiate new submenu."""
		self.parent=_parent
		self.text=_text
		self.options={}
		self.level=0
		self.items = []
	def add_menu_option(self,_menu_option_object):
		"""Add menu option _menu_option_object to the submenu."""
		_menu_option_object.parent=self
		_menu_option_object.level=self.level+1
		_menu_option_object.options=self.options
		self.items.append(_menu_option_object)
		return self
	def add_submenu(self,_submenu_object):
		"""Add submenu _submenu_object to the submenu."""
		_submenu_object.parent=self
		_submenu_object.level=self.level+1
		_submenu_object.options = self.options
		for each_option in _submenu_object.items:
			each_option.options = parent.options
		self.items.append(_submenu_object)
		return self
	def display(self):
		"""Display the submenu and all suboptions."""
		s = self.options['space']
		v = self.level
		t = self.options['tab']
		p = self.options['sep']
		b = self.options['bullet']
		print(v*t+b+s+self.text)
		for each_item in self.items:
			each_item.display()
	def check_input(self,_user_input):
		"""Check user input _user_input against the available options, then return either None or the function of the matching menu item."""
		action_check = None
		for each_item in self.items:
			action_check = each_item.check_input(_user_input)
			if action_check is not None:
				break
		return action_check
	pass
class MenuOption:
	def __init__(self,_abbrev='?',_text='Empty option',_func=None,_par=None):
		"""Initiate menu option object."""
		self.text=_text
		self.abbrev=_abbrev
		self.func=_func
		self.options = {}
		self.parent=_par
		self.level=0
	def display(self):
		"""Display the menu option."""
		s = self.options['space']
		v = self.level
		p = self.options['sep']
		t = self.options['tab']
		b = self.options['bullet']
		print(v*t+b+s+self.abbrev+s+p+s+self.text)
	def check_input(self,_user_input):
		"""Check user input _user_input against the menu option's abbreviation/key. If it matches, return the menu option's function. If not, return None."""
		if _user_input == self.abbrev:
			return self.func
		return None