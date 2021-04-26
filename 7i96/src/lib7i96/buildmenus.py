from PyQt5.QtWidgets import QMenu, QAction

inputs = [{'Not Used':'Select'},
	{'Homing':['Joint 0 Home', 'Joint 1 Home', 'Joint 2 Home',
		'Joint 3 Home', 'Joint 4 Home', 'Joint 5 Home',
		'Joint 6 Home', 'Joint 7 Home', 'Joint 8 Home', 'Home All']},
	{'Limits':[
		{'Joint 0':['Joint 0 Plus', 'Joint 0 Minus', 'Joint 0 Both']},
		{'Joint 1':['Joint 1 Plus', 'Joint 1 Minus', 'Joint 1 Both']},
		{'Joint 2':['Joint 2 Plus', 'Joint 2 Minus', 'Joint 2 Both']},
		{'Joint 3':['Joint 3 Plus', 'Joint 3 Minus', 'Joint 3 Both']},
		{'Joint 4':['Joint 4 Plus', 'Joint 4 Minus', 'Joint 4 Both']},
		{'Joint 5':['Joint 5 Plus', 'Joint 5 Minus', 'Joint 5 Both']},
		{'Joint 6':['Joint 6 Plus', 'Joint 6 Minus', 'Joint 6 Both']},
		{'Joint 7':['Joint 7 Plus', 'Joint 7 Minus', 'Joint 7 Both']},
		{'Joint 8':['Joint 8 Plus', 'Joint 8 Minus', 'Joint 8 Both']}]},
	{'Jog':[{'X Axis':['X Plus', 'X Minus', 'X Enable']},
		{'Y Axis':['Y Plus', 'Y Minus', 'Y Enable']},
		{'Z Axis':['Z Plus', 'Z Minus', 'X Enable']},
		{'A Axis':['A Plus', 'A Minus', 'A Enable']},
		{'B Axis':['B Plus', 'B Minus', 'B Enable']},
		{'C Axis':['C Plus', 'C Minus', 'C Enable']},
		{'U Axis':['U Plus', 'U Minus', 'U Enable']},
		{'V Axis':['V Plus', 'V Minus', 'V Enable']},
		{'W Axis':['W Plus', 'W Minus', 'W Enable']}
	]},
	{'I/O Control':['Flood', 'Mist', 'Lube Level', 'Tool Changed',
		'Tool Prepared', 'External E Stop']},
	{'Motion':['Probe Input', 'Digital 0', 'Digital 1', 'Digital 2', 'Digital 3']}
]

# {'':['', ]},
# '', 
outputs = [{'Not Used':'Select'},
	{'Spindle':['Spindle On', 'Spindle CW', 'Spindle CCW', 'Spindle Brake']},
	{'I/O Control':['Coolant Flood', 'Coolant Mist', 'Lube Pump',
		'Tool Change', 'Tool Prepare', 'E Stop Out']},
	{'Digital Out':['Digital Out 0', 'Digital Out 1', 'Digital Out 2', 'Digital Out 3', ]}
]

def build(parent):
	for i in range(11):
		button = getattr(parent, "inputPB_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(inputs, menu)
		button.setMenu(menu)

	for i in range(24):
		button = getattr(parent, "ss7i64in_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(inputs, menu)
		button.setMenu(menu)

	for i in range(24):
		button = getattr(parent, "ss7i69in_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(inputs, menu)
		button.setMenu(menu)

	for i in range(48):
		button = getattr(parent, "ss7i70in_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(inputs, menu)
		button.setMenu(menu)

	for i in range(32):
		button = getattr(parent, "ss7i84in_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(inputs, menu)
		button.setMenu(menu)

	for i in range(6):
		button = getattr(parent, "outputPB_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(outputs, menu)
		button.setMenu(menu)

	for i in range(24):
		button = getattr(parent, "ss7i64out_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(outputs, menu)
		button.setMenu(menu)

	for i in range(24):
		button = getattr(parent, "ss7i69out_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(outputs, menu)
		button.setMenu(menu)

	for i in range(48):
		button = getattr(parent, "ss7i71out_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(outputs, menu)
		button.setMenu(menu)

	for i in range(48):
		button = getattr(parent, "ss7i72out_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(outputs, menu)
		button.setMenu(menu)

	for i in range(16):
		button = getattr(parent, "ss7i84out_{}".format(i))
		menu = QMenu()
		menu.triggered.connect(lambda action, button=button: button.setText(action.text()))
		add_menu(outputs, menu)
		button.setMenu(menu)

def add_menu(data, menu_obj):
	if isinstance(data, dict):
		for k, v in data.items():
			sub_menu = QMenu(k, menu_obj)
			menu_obj.addMenu(sub_menu)
			add_menu(v, sub_menu)
	elif isinstance(data, list):
		for element in data:
			add_menu(element, menu_obj)
	else:
		action = menu_obj.addAction(data)
		action.setIconVisibleInMenu(False)
