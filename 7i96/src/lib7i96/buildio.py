import os
from datetime import datetime

def build(parent):
	filePath = os.path.join(parent.configPath, 'io.hal')
	parent.outputPTE.appendPlainText(f'Building {filePath}')
	contents = []
	contents = ['# This file was created with the 7i96 Wizard on ']
	contents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	contents.append('# If you make changes to this file DO NOT use the Configuration Tool\n\n')

	# build the inputs
	for index in range(11):
		inputText = getattr(parent, 'input_' + str(index)).currentText()
		joint = getattr(parent, 'inputJoint_' + str(index)).currentData()
		if getattr(parent, 'inputInvert_' + str(index)).currentData() == 'Inverted':
			invert = '_not'
		else:
			invert = ''
		if inputText == 'E-Stop':
			contents.append('# External E-Stop\n')
			contents.append('net estop-loopout iocontrol.0.emc-enable-in <= estop-latch.0.ok-out\n')
			contents.append('net estop-loopin iocontrol.0.user-enable-out => estop-latch.0.ok-in\n')
			contents.append('net estop-reset iocontrol.0.user-request-enable => estop-latch.0.reset\n')
			contents.append(f'net remote-estop estop-latch.0.fault-in <= hm2_7i96.0.gpio.{index:02}.in{invert}\n\n')
		elif inputText == 'Home':
			contents.append(f'net home-joint-{joint} joint.{joint}.home-sw-in <= hm2_7i96.0.gpio.{index:02}.in{invert}\n')
		elif inputText == 'Both Limit':
			contents.append(f'net limits-joint-{joint} joint.{joint}.neg-lim-sw-in <= hm2_7i96.0.gpio.{index:02}.in\n')
			contents.append(f'net limits-joint-{joint} joint.{joint}.pos-lim-sw-in\n')
		elif inputText == 'Min Limit':
			contents.append(f'net min-limit-joint-{joint} joint.{joint}.neg-lim-sw-in <= hm2_7i96.0.gpio.{index:02}.in\n')
		elif inputText == 'Max Limit':
			contents.append(f'net max-limit-joint-{joint} joint.{joint}.pos-lim-sw-in <= hm2_7i96.0.gpio.{index:02}.in\n')
		elif inputText == 'Home & Limit':
			contents.append(f'net home-limit-joint-{joint} joint.{joint}.home-sw-in <= hm2_7i96.0.gpio.{index:02}.in\n')
			contents.append(f'net home-limit-joint-{joint} joint.{joint}.neg-lim-sw-in\n')
			contents.append(f'net home-limit-joint-{joint} joint.{joint}.pos-lim-sw-in\n')
		elif inputText == 'Min Limit & Home':
			contents.append(f'net min-limit-home-joint-{joint} joint.{joint}.neg-lim-sw-in <= hm2_7i96.0.gpio.{index:02}.in\n')
			contents.append(f'net min-limit-home-joint-{joint} joint.{joint}.home-sw-in\n')
		elif inputText == 'Max Limit & Home':
			contents.append(f'net max-limit-home-joint-{joint} joint.{joint}.pos-lim-sw-in <= hm2_7i96.0.gpio.{index:02}.in\n')
			contents.append(f'net max-limit-home-joint-{joint} joint.{joint}.home-sw-in\n')
		elif inputText == 'Probe':
			contents.append(f'net probe-input motion.probe-input <= hm2_7i96.0.gpio.{index:02}.in\n')
		elif inputText == 'Digital In 0':
			contents.append(f'net digital-input-0 motion.digital-in-00 <= hm2_7i96.0.gpio.{index:02}.in\n')
		elif inputText == 'Digital In 1':
			contents.append(f'net digital-input-1 motion.digital-in-01 <= hm2_7i96.0.gpio.{index:02}.in\n')
		elif inputText == 'Digital In 2':
			contents.append(f'net digital-input-2 motion.digital-in-02 <= hm2_7i96.0.gpio.{index:02}.in\n')
		elif inputText == 'Digital In 3':
			contents.append(f'net digital-input-3 motion.digital-in-03 <= hm2_7i96.0.gpio.{index:02}.in\n')

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


	# build the outputs
	for index in range(6):
		outputText = getattr(parent, 'output_' + str(index)).currentText()
		if outputText != 'Select':
			netLine = outputDict[outputText]
			contents.append(f'{netLine}hm2_7i96.0.ssr.00.out-0{index}\n')

	try:
		with open(filePath, 'w') as f:
			f.writelines(contents)
	except OSError:
		parent.outputPTE.appendPlainText(f'OS error\n {traceback.print_exc()}')
