def build(parent):
	sscards = {
	'Select':'No Card Selected',
	'7i64':'24 Outputs, 24 Inputs',
	'7i69':'48 Digital I/O Bits',
	'7i70':'48 Inputs',
	'7i71':'48 Sourcing Outputs',
	'7i72':'48 Sinking Outputs',
	'7i73':'Pendant Card',
	'7i84':'32 Inputs 16 Outputs',
	'7i87':'8 Analog Inputs'
	}
	parent.smartSerialInfoLbl.setText(sscards[parent.smartSerialCardCB.currentText()])
	parent.smartSerialSW.setCurrentIndex(parent.smartSerialCardCB.currentData())
	pins7i64 = {}
	pins7i69 = {}
	pins7i70 = {}
	pins7i71 = {}
	pins7i72 = {}
	pins7i73 = {}
	pins7i84 = {}
	pins7i87 = {}


	"""

	outputDict = {
	'Coolant Flood': 'net flood-output iocontrol.0.coolant-flood => ',
	'Coolant Mist': 'net mist-output iocontrol.0.coolant-mist => ',
	'Spindle On': 'net spindle-on spindle.0.on => ',
	'Spindle CW': 'net spindle-cw spindle.0.forward => ',
	'Spindle CCW': 'net spindle-ccw spindle.0.reverse => ',
	'Spindle Brake': 'net spindle-brake spindle.0.brake => ',
	'E-Stop Out': 'net estop-loop ',
	'Digital Out 0': 'net digital-out-0 motion.digital-out-00 => ',
	'Digital Out 1': 'net digital-out-1 motion.digital-out-01 => ',
	'Digital Out 2': 'net digital-out-2 motion.digital-out-02 => ',
	'Digital Out 3': 'net digital-out-3 motion.digital-out-03 => ',
	'Start Tool Change': '',
	'Tool Change': '',
	'Tool Prepare': '',
	}


	if combo == 'input':
		comboList = [
		['Select', False],
		['E-Stop', 'E-Stop'],
		['Home', 'Home'],
		['Both Limit', 'Both Limit'],
		['Min Limit', 'Min Limit'],
		['Max Limit', 'Max Limit'],
		['Home & Limit', 'Home & Limit'],
		['Min Limit & Home', 'Min Limit & Home'],
		['Max Limit & Home', 'Max Limit & Home'],
		['Probe', 'Probe'],
		['Digital In 0', 'Digital In 0'],
		['Digital In 1', 'Digital In 1'],
		['Digital In 2', 'Digital In 2'],
		['Digital In 3', 'Digital In 3'],
		['Start Tool Change Ack', 'start-change-ack'],
		['Tool Changed', 'tool-changed'],
		['Tool Prepared', 'tool-prepared'],
		['Tool Changer Fault', 'toolchanger-fault'],
		['Tool Changer Clear Fault', 'toolchanger-clear-fault']
		]

	if combo == 'input_invert':
		comboList = [
		['Select', False],
		['Normal', 'Normal'],
		['Inverted', 'Inverted']
		]

	if combo == 'output':
		comboList = [
		['Select', False],
		['Coolant Flood', 'Coolant Flood'],
		['Coolant Mist', 'Coolant Mist'],
		['Spindle On', 'Spindle On'],
		['Spindle CW', 'Spindle CW'],
		['Spindle CCW', 'Spindle CCW'],
		['Spindle Brake', 'Spindle Brake'],
		['E-Stop Out', 'E-Stop Out'],
		['Digital Out 0', 'Digital Out 0'],
		['Digital Out 1', 'Digital Out 1'],
		['Digital Out 2', 'Digital Out 2'],
		['Digital Out 3', 'Digital Out 3'],
		['Start Tool Change', 'start-change'],
		['Tool Change', 'tool-change'],
		['Tool Prepare', 'tool-prepare'],
		['', ''],
		]
	"""


def buildCB(parent):
	inputs = [
		['Select', False],
		['Signal Only', ' '],
		['Probe', 'motion.probe-input'],
		['Digital In 0', 'motion.digital-in-00'],
		['Digital In 1', 'motion.digital-in-01'],
		['Digital In 2', 'motion.digital-in-02'],
		['Digital In 3', 'motion.digital-in-03'],
		]

	outputs = [
		['Select', False],
		['Signal Only', ' '],
		['Coolant Flood', 'iocontrol.0.coolant-flood'],
		['Coolant Mist', 'iocontrol.0.coolant-mist'],
		['Spindle On', 'spindle.0.on'],
		['Spindle CW', 'spindle.0.forward'],
		['Spindle CCW', 'spindle.0.reverse'],
		['Spindle Brake', 'spindle.0.brake'],
		['E-Stop Out', 'iocontrol.0.user-enable-out'],
		['Digital Out 0', 'motion.digital-out-00'],
		['Digital Out 1', 'motion.digital-out-01'],
		['Digital Out 2', 'motion.digital-out-02'],
		['Digital Out 3', 'motion.digital-out-03'],
		]

	# 7i64 Combo Boxes
	for i in range(24):
		for item in inputs:
			getattr(parent, 'ss7i64in_' + str(i)).addItem(item[0], item[1])
		for item in outputs:
			getattr(parent, 'ss7i64out_' + str(i)).addItem(item[0], item[1])

	# 7i69 Combo Boxes
	for i in range(24):
		for item in inputs:
			getattr(parent, 'ss7i69in_' + str(i)).addItem(item[0], item[1])
		for item in outputs:
			getattr(parent, 'ss7i69out_' + str(i)).addItem(item[0], item[1])

	# 7i70 Combo Boxes
	for i in range(48):
		for item in inputs:
			getattr(parent, 'ss7i70in_' + str(i)).addItem(item[0], item[1])

	# 7i71 Combo Boxes
	for i in range(48):
		for item in outputs:
			getattr(parent, 'ss7i71out_' + str(i)).addItem(item[0], item[1])

	# 7i72 Combo Boxes
	for i in range(48):
		for item in outputs:
			getattr(parent, 'ss7i72out_' + str(i)).addItem(item[0], item[1])

	# 7i84 Combo Boxes
	for i in range(32):
		for item in inputs:
			getattr(parent, 'ss7i84in_' + str(i)).addItem(item[0], item[1])
	for i in range(16):
		for item in outputs:
			getattr(parent, 'ss7i84out_' + str(i)).addItem(item[0], item[1])
