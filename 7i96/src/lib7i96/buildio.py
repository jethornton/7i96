import os
from datetime import datetime

def build(parent):
	filePath = os.path.join(parent.configPath, 'io.hal')
	parent.outputPTE.appendPlainText(f'Building {filePath}')
	contents = []
	contents = ['# This file was created with the 7i96 Wizard on ']
	contents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	contents.append('# If you make changes to this file DO NOT use the Configuration Tool\n\n')

	inputs = [{'Not Used':'Select'},
		{'Homing':['Joint 0 Home', 'Joint 1 Home', 'Joint 2 Home',
		'Joint 3 Home', 'Joint 4 Home', 'Joint 5 Home',
		'Joint 6 Home', 'Joint 7 Home', 'Joint 8 Home',]},
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
		{'I/O Control':['Flood', 'Mist', 'Lube Level', 'Tool Changed', 'Tool Prepared']},
		{'Motion':['Probe Input','Digital 0', 'Digital 1', 'Digital 2', 'Digital 3']}
	]

	input_dict = {
		'Joint 0 Home':'net joint-0-home joint.0.home-sw-in <= ',
		'Joint 1 Home':'net joint-1-home joint.1.home-sw-in <= ',
		'Joint 2 Home':'net joint-2-home joint.2.home-sw-in <= ',
		'Joint 3 Home':'net joint-3-home joint.3.home-sw-in <= ',
		'Joint 4 Home':'net joint-4-home joint.4.home-sw-in <= ',
		'Joint 5 Home':'net joint-5-home joint.5.home-sw-in <= ',
		'Joint 6 Home':'net joint-6-home joint.6.home-sw-in <= ',
		'Joint 7 Home':'net joint-7-home joint.7.home-sw-in <= ',
		'Joint 8 Home':'net joint-8-home joint.8.home-sw-in <= ',

		'Joint 0 Plus':'net pos-limit-joint-0 joint.0.pos-lim-sw-in <= ',
		'Joint 0 Minus':'net neg-limit-joint-0 joint.0.neg-lim-sw-in <= ',
		'Joint 0 Both':'net both-limit-joint-0 joint.0.pos-lim-sw-in\n'
			'net both-limit-joint-0 joint.0.neg-lim-sw-in <= ',
		'Joint 1 Plus':'net pos-limit-joint-1 joint.1.pos-lim-sw-in <= ',
		'Joint 1 Minus':'net neg-limit-joint-1 joint.1.neg-lim-sw-in <= ',
		'Joint 1 Both':'net both-limit-joint-1 joint.1.pos-lim-sw-in\n'
			'net both-limit-joint-1 joint.1.neg-lim-sw-in <= ',
		'Joint 2 Plus':'net pos-limit-joint-2 joint.2.pos-lim-sw-in <= ',
		'Joint 2 Minus':'net neg-limit-joint-2 joint.2.neg-lim-sw-in <= ',
		'Joint 2 Both':'net both-limit-joint-2 joint.2.pos-lim-sw-in\n'
			'net both-limit-joint-2 joint.2.neg-lim-sw-in <= ',
		'Joint 3 Plus':'net pos-limit-joint-3 joint.3.pos-lim-sw-in <= ',
		'Joint 3 Minus':'net neg-limit-joint-3 joint.3.neg-lim-sw-in <= ',
		'Joint 3 Both':'net both-limit-joint-3 joint.3.pos-lim-sw-in\n'
			'net both-limit-joint-3 joint..neg-lim-sw-in <= ',
		'Joint 4 Plus':'net pos-limit-joint-4 joint.4.pos-lim-sw-in <= ',
		'Joint 4 Minus':'net neg-limit-joint-4 joint.4.neg-lim-sw-in <= ',
		'Joint 4 Both':'net both-limit-joint-4 joint.4.pos-lim-sw-in\n'
			'net both-limit-joint-4 joint.4.neg-lim-sw-in <= ',
		'Joint 5 Plus':'net pos-limit-joint-5 joint.5.pos-lim-sw-in <= ',
		'Joint 5 Minus':'net neg-limit-joint-5 joint.5.neg-lim-sw-in <= ',
		'Joint 5 Both':'net both-limit-joint-5 joint.5.pos-lim-sw-in\n'
			'net both-limit-joint-5 joint.5.neg-lim-sw-in <= ',
		'Joint 6 Plus':'net pos-limit-joint-6 joint.6.pos-lim-sw-in <= ',
		'Joint 6 Minus':'net neg-limit-joint-6 joint.6.neg-lim-sw-in <= ',
		'Joint 6 Both':'net both-limit-joint-6 joint.6.pos-lim-sw-in\n'
			'net both-limit-joint-6 joint.6.neg-lim-sw-in <= ',
		'Joint 7 Plus':'net pos-limit-joint-7 joint.7.pos-lim-sw-in <= ',
		'Joint 7 Minus':'net neg-limit-joint-7 joint.7.neg-lim-sw-in <= ',
		'Joint 7 Both':'net both-limit-joint-7 joint.7.pos-lim-sw-in\n'
			'net both-limit-joint-7 joint.7.neg-lim-sw-in <= ',
		'Joint 8 Plus':'net pos-limit-joint-8 joint.8.pos-lim-sw-in <= ',
		'Joint 8 Minus':'net neg-limit-joint-8 joint.8.neg-lim-sw-in <= ',
		'Joint 8 Both':'net both-limit-joint-8 joint.8.pos-lim-sw-in\n'
			'net both-limit-joint-8 joint.8.neg-lim-sw-in <= ',

		'Probe Input':'net probe-input motion.probe-input <= ',
		'Digital 0':'net digital-0-input motion.digital-in-00 <= ',
		'Digital 1':'net digital-1-input motion.digital-in-01 <= ',
		'Digital 2':'net digital-2-input motion.digital-in-02 <= ',
		'Digital 3':'net digital-3-input motion.digital-in-03 <= ',

		'Flood':'net coolant-flood iocontrol.0.coolant-flood <= ',
		'Mist':'net coolant-mist iocontrol.0.coolant-mist <= ',
		'Lube Level':'net lube-level iocontrol.0.lube_level <= ',
		'Tool Changed':'net tool-changed iocontrol.0.tool-changed <= ',
		'Tool Prepared':'net tool-prepared iocontrol.0.tool-prepared <= '
		}

	# build inputs from qpushbutton menus
	for i in range(11):
		key = getattr(parent, 'inputPB_' + str(i)).text()
		invert = '_not' if getattr(parent, 'inputInvertCb_' + str(i)).isChecked() else ''
		if input_dict.get(key, False): # return False if key is not in dictionary
			contents.append(input_dict[key] + f'hm2_7i96.0.gpio.{i:03}.in{invert}\n')
		else: # handle special cases
			if key == 'Home All':
				contents.append('\n# Home All Joints\n')
				contents.append('net home-all ' + f'hm2_7i96.0.gpio.{i:03}.in{invert}\n')
				for i in range(5):
					if getattr(parent, 'axisCB_' + str(i)).currentData():
						contents.append('net home-all ' + f'joint.{i}.home-sw-in\n')
			elif key == 'External E Stop':
				contents.append('\n# External E-Stop\n')
				contents.append('loadrt estop_latch\n')
				contents.append('addf estop-latch.0 servo-thread\n')
				contents.append('net estop-loopout iocontrol.0.emc-enable-in <= estop-latch.0.ok-out\n')
				contents.append('net estop-loopin iocontrol.0.user-enable-out => estop-latch.0.ok-in\n')
				contents.append('net estop-reset iocontrol.0.user-request-enable => estop-latch.0.reset\n')
				contents.append(f'net remote-estop estop-latch.0.fault-in <= hm2_7i96.0.gpio.{i:02}.in{invert}\n\n')

	output_dict = {
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
	'Digital Out 3': 'net digital-out-3 motion.digital-out-03 => '
	}

	# build the outputs
	for i in range(6):
		key = getattr(parent, 'outputPB_' + str(i)).text()
		if output_dict.get(key, False): # return False if key is not in dictionary
			contents.append(output_dict[key] + f'hm2_7i96.0.ssr.00.out-0{i}\n')
		else: # handle special cases
			if key == 'E Stop Out':
				contents.append(f'net estop-loopin hm2_7i96.0.ssr.00.out-0{i}\n')


	try:
		with open(filePath, 'w') as f:
			f.writelines(contents)
	except OSError:
		parent.outputPTE.appendPlainText(f'OS error\n {traceback.print_exc()}')
