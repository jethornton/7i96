def build(parent):
	ipAddress = [
	['Select', False],
	['10.10.10.10', '"10.10.10.10"'],
	['192.168.1.121', '"192.168.1.121"']
	]

	for item in ipAddress:
		parent.ipAddressCB.addItem(item[0], item[1])

	stepgens = [
		['Default', False],
		['0', '0'],
		['1', '1'],
		['2', '2'],
		['3', '3'],
		['4', '4'],
		['5', '5']
	]

	for item in stepgens:
		parent.stepgensCB.addItem(item[0], item[1])

	encoders = [
		['Default', False],
		['0', '0'],
		['1', '1']
	]

	for item in encoders:
		parent.encodersCB.addItem(item[0], item[1])

	pwmgens = [
		['Default', False],
		['0', '0'],
		['1', '1']
	]

	for item in pwmgens:
		parent.pwmgensCB.addItem(item[0], item[1])

	sserialport = [
		['Default', False],
		['00xxxx', '00xxxx']
	]

	for item in sserialport:
		parent.sserialPortCB.addItem(item[0], item[1])


	axes = [
		['Select', False],
		['X', 'X'],
		['Y', 'Y'],
		['Z', 'Z'],
		['A', 'A'],
		['B', 'B'],
		['C', 'C'],
		['U', 'U'],
		['V', 'V'],
		['W', 'W']
		]

	for i in range(parent.card['joints']):
		for item in axes:
			getattr(parent, f'axisCB_{i}').addItem(item[0], item[1])

	linearUnits = [
		['Select', False],
		['Imperial', 'inch'],
		['Metric', 'metric']
		]

	for item in linearUnits:
		parent.linearUnitsCB.addItem(item[0], item[1])

	gui = [
		['Select', False],
		['Axis', 'axis'],
		['Touchy', 'touchy']
		]

	for item in gui:
		parent.guiCB.addItem(item[0], item[1])

	positionOffset = [
		['Select', False],
		['Relative', 'RELATIVE'],
		['Machine', 'MACHINE']
		]

	for item in positionOffset:
		parent.positionOffsetCB.addItem(item[0], item[1])

	positionFeedback = [
		['Select', False],
		['Commanded', 'COMMANDED'],
		['Actual', 'ACTUAL']
		]

	for item in positionFeedback:
		parent.positionFeedbackCB.addItem(item[0], item[1])

	ssCards = [
		['Select', False],
		['7i64', '7i64'],
		['7i69', '7i69'],
		['7i70', '7i70'],
		['7i71', '7i71'],
		['7i72', '7i72'],
		['7i73', '7i73'],
		['7i84', '7i84'],
		['7i87', '7i87']
		]

	for item in ssCards:
		parent.ssCardCB.addItem(item[0], item[1])

	drives = [
		['Custom', False],
		['Gecko 201', ['500', '4000', '20000', '1000']],
		['Gecko 202', ['500', '4500', '20000', '1000']],
		['Gecko 203v', ['1000', '2000', '200', '200']],
		['Gecko 210', ['500', '4000', '20000', '1000']],
		['Gecko 212', ['500', '4000', '20000', '1000']],
		['Gecko 320', ['3500', '500', '200', '200']],
		['Gecko 540', ['1000', '2000', '200', '200']],
		['L297', ['500', '4000', '4000', '1000']],
		['PMDX 150', ['1000', '2000', '1000', '1000']],
		['Sherline', ['22000', '22000', '100000', '100000']],
		['Xylotex BS-3', ['2000', '1000', '200', '200']],
		['Parker 750', ['1000', '1000', '1000', '200000']],
		['JVL SMD41/42', ['500', '500', '2500', '2500']],
		['Hobbycnc', ['2000', '2000', '2000', '2000']],
		['Keling 4030', ['5000', '5000', '20000', '20000']]
		]

	for i in range(parent.card['joints']):
		for item in drives:
			getattr(parent, f'driveCB_{i}').addItem(item[0], item[1])

	debug = [
		['Debug Off', '0x00000000'],
		['Debug Configuration', '0x00000002'],
		['Debug Task Issues', '0x00000008'],
		['Debug NML', '0x00000010'],
		['Debug Motion Time', '0x00000040'],
		['Debug Interpreter', '0x00000080'],
		['Debug RCS', '0x00000100'],
		['Debug Interperter List', '0x00000800'],
		['Debug IO Control', '0x00001000'],
		['Debug O Word', '0x00002000'],
		['Debug Remap', '0x00004000'],
		['Debug Python', '0x00008000'],
		['Debug Named Parameters', '0x00010000'],
		['Debug Gdbon Signal', '0x00020000'],
		['Debug Python Task', '0x00040000'],
		['Debug User 1', '0x10000000'],
		['Debug User 2', '0x20000000'],
		['Debug Unconditional', '0x40000000'],
		['Debug All', '0x7FFFFFFF']
		]

	for item in debug:
		parent.debugCB.addItem(item[0], item[1])

		spindle = [
		['None', False],
		['PWM Direction', '1'],
		['Up Down', '2'],
		['PDM Direction', '3'],
		['Direction PWM', '4'],
		['Step Direction', False],
		]

	for item in spindle:
		parent.spindleTypeCB.addItem(item[0], item[1])

	cpuSpeed = [
		['GHz', 1000],
		['MHz', 1]
		]

	for item in cpuSpeed:
		parent.cpuSpeedCB.addItem(item[0], item[1])

	firmware = [
		['Select', False],
		['6 StepGens', '7i95d.bit'],
		['3 StepGens 3 PWM/DIR', '7i95d3pwm.bit']
		]

	for item in firmware:
		parent.firmwareCB.addItem(item[0], item[1])


"""

def setupCombo(combo):
	comboList = []

	# might take a look at the data and see if we can simply use '10.10.10.10'
	if combo == 'ipAddress':
		comboList = [
		['Select', False],
		['10.10.10.10', '"10.10.10.10"'],
		['192.168.1.121', '"192.168.1.121"']
		]

	if combo == 'stepgens':
		comboList = [
		['No Firmware Selected', False],
		]

	if combo == 'stepgens_4':
		comboList = [
		['4 Stepgens', 4],
		['3 Stepgens', 3],
		['2 Stepgens', 2],
		['1 Stepgen', 1],
		['0 Stepgens', 0],
		]

	if combo == 'stepgens_5':
		comboList = [
		['5 Stepgens', 5],
		['4 Stepgens', 4],
		['3 Stepgens', 3],
		['2 Stepgens', 2],
		['1 Stepgen', 1],
		['0 Stepgens', 0],
		]


	if combo == 'stepgens_8':
		comboList = [
		['8 Stepgens', 8],
		['7 Stepgens', 7],
		['6 Stepgens', 6],
		['5 Stepgens', 5],
		['4 Stepgens', 4],
		['3 Stepgens', 3],
		['2 Stepgens', 2],
		['1 Stepgen', 1],
		['0 Stepgens', 0],
		]

	if combo == 'stepgens_9':
		comboList = [
		['9 Stepgens', 9],
		['8 Stepgens', 8],
		['7 Stepgens', 7],
		['6 Stepgens', 6],
		['5 Stepgens', 5],
		['4 Stepgens', 4],
		['3 Stepgens', 3],
		['2 Stepgens', 2],
		['1 Stepgen', 1],
		['0 Stepgens', 0],
		]

	if combo == 'stepgens_10':
		comboList = [
		['10 Stepgens', 10],
		['9 Stepgens', 9],
		['8 Stepgens', 8],
		['7 Stepgens', 7],
		['6 Stepgens', 6],
		['5 Stepgens', 5],
		['4 Stepgens', 4],
		['3 Stepgens', 3],
		['2 Stepgens', 2],
		['1 Stepgen', 1],
		['0 Stepgens', 0],
		]



	if combo == 'encoders':
		comboList = [
		['No Firmware Selected', False],
		]

	if combo == 'encoders_1':
		comboList = [
		['1 Encoder', 1],
		['0 Encoders', 0],
		]

	if combo == 'encoders_2':
		comboList = [
		['2 Encoders', 2],
		['1 Encoder', 1],
		['0 Encoders', 0],
		]

	if combo == 'encoders_3':
		comboList = [
		['3 Encoders', 3],
		['2 Encoders', 2],
		['1 Encoder', 1],
		['0 Encoders', 0],
		]

	if combo == 'encoders_4':
		comboList = [
		['4 Encoders', 4],
		['3 Encoders', 3],
		['2 Encoders', 2],
		['1 Encoder', 1],
		['0 Encoders', 0],
		]

	if combo == 'encoders_6':
		comboList = [
		['6 Encoders', 6],
		['5 Encoders', 5],
		['4 Encoders', 4],
		['3 Encoders', 3],
		['2 Encoders', 2],
		['1 Encoder', 1],
		['0 Encoders', 0],
		]

	if combo == 'encoders_8':
		comboList = [
		['8 Encoders', 8],
		['7 Encoders', 7],
		['6 Encoders', 6],
		['5 Encoders', 5],
		['4 Encoders', 4],
		['3 Encoders', 3],
		['2 Encoders', 2],
		['1 Encoder', 1],
		['0 Encoders', 0],
		]


	if combo == 'encoders_10':
		comboList = [
		['10 Encoders', 10],
		['9 Encoders', 9],
		['8 Encoders', 8],
		['7 Encoders', 7],
		['6 Encoders', 6],
		['5 Encoders', 5],
		['4 Encoders', 4],
		['3 Encoders', 3],
		['2 Encoders', 2],
		['1 Encoder', 1],
		['0 Encoders', 0],
		]

	if combo == 'pwms':
		comboList = [
		['No Firmware Selected', False],
		]

	if combo == 'pwms_0':
		comboList = [
		['0 PWM', 0],
		]

	if combo == 'pwms_1':
		comboList = [
		['1 PWM', 1],
		['0 PWM', 0],
		]

	if combo == 'axis':
		comboList = [
		['Select', False],
		['X', 'X'],
		['Y', 'Y'],
		['Z', 'Z'],
		['A', 'A'],
		['B', 'B'],
		['C', 'C'],
		['U', 'U'],
		['V', 'V'],
		['W', 'W']
		]

	if combo == 'joint':
		comboList = [
		['Select', False],
		['Joint 0', '0'],
		['Joint 1', '1'],
		['Joint 2', '2'],
		['Joint 3', '3'],
		['Joint 4', '4']
		]

	if combo == 'display':
		comboList = [
		['Select', False],
		['Axis', 'axis'],
		['Touchy', 'touchy']
		]

	if combo == 'linearUnits':
		comboList = [
		['Select', False],
		['Imperial', 'inch'],
		['Metric', 'metric']
		]

	if combo == 'angularUnits':
		comboList = [['Degree', 'degree']]


	if combo == 'positionOffset':
		comboList = [
		['Select', False],
		['Relative', 'RELATIVE'],
		['Machine', 'MACHINE']
		]

	if combo == 'positionFeedback':
		comboList = [
		['Select', False],
		['Commanded', 'COMMANDED'],
		['Actual', 'ACTUAL']
		]

	if combo == 'debug':
		comboList = [
		['Debug Off', '0x00000000'],
		['Debug Configuration', '0x00000002'],
		['Debug Task Issues', '0x00000008'],
		['Debug NML', '0x00000010'],
		['Debug Motion Time', '0x00000040'],
		['Debug Interpreter', '0x00000080'],
		['Debug RCS', '0x00000100'],
		['Debug Interperter List', '0x00000800'],
		['Debug IO Control', '0x00001000'],
		['Debug O Word', '0x00002000'],
		['Debug Remap', '0x00004000'],
		['Debug Python', '0x00008000'],
		['Debug Named Parameters', '0x00010000'],
		['Debug Gdbon Signal', '0x00020000'],
		['Debug Python Task', '0x00040000'],
		['Debug User 1', '0x10000000'],
		['Debug User 2', '0x20000000'],
		['Debug Unconditional', '0x40000000'],
		['Debug All', '0x7FFFFFFF']
		]

	if combo == 'boards':
		comboList = [
		['Select', False],
		['7i96 5 Stepgens', '7i96d.bit'],
		['7i96 4 Stepgens 1 PWM', '7i96d_1pwm.bit'],
		['7i96 + 7i76', '7i96_7i76d.bit'],
		['7i96 + 7i77', '7i96_7i77d.bit'],
		['7i96 + 7i78', '7i96_7i78d.bit'],
		['7i96 + 7i85', '7i96_7i85d.bit'],
		['7i96 + 7i89', '7i96_7i89d.bit'],
		]

	if combo == 'config':
		comboList = [
		['Select', False],
		['5 Stepgens', ['5', '0']],
		['4 Stepgens 1 PWM', ['4', '1']]
		]

	if combo == 'firmware':# [Name, firmware]
		comboList = [
		['Select', False],
		['5 StepGens ', '7i96d.bit'],
		['4 StepGens 1 PWM', '7i96d_1pwm.bit'],
		['7i96 + 5abob', '7i96_5abob_d.bit'],
		['7i96 + 6 Encoders', '7i96_6enc_d.bit'],
		['7i96 + 7i76', '7i96_7i76d.bit'],
		['7i96 + 7i77', '7i96_7i77d.bit'],
		['7i96 + 7i78', '7i96_7i78d.bit'],
		['7i96 + 7i85', '7i96_7i85d.bit'],
		['7i96 + 7i85S', '7i96_7i85sd.bit'],
		['7i96 1 PWM + 7i85S', '7i961pwm_7i85s.bit'],
		['7i96 + 7i89', '7i96_7i89d.bit'],
		['7i96 + G540', '7i96_g540dpl.bit']
		]

	if combo == 'sscard':
		comboList = [
		['Select', False],
		['7i64', '7i64'],
		['7i69', '7i69'],
		['7i70', '7i70'],
		['7i71', '7i71'],
		['7i72', '7i72'],
		['7i73', '7i73'],
		['7i84', '7i84'],
		['7i87', '7i87']
		]

	if combo == 'spindle':
		comboList = [
		['None', False],
		['PWM Direction', '1'],
		['Up Down', '2'],
		['PDM Direction', '3'],
		['Direction PWM', '4'],
		['Step Direction', False],
		]

	if combo == 'drive':
		comboList = [
		['Custom', False],
		['Gecko 201', ['500', '4000', '20000', '1000']],
		['Gecko 202', ['500', '4500', '20000', '1000']],
		['Gecko 203v', ['1000', '2000', '200', '200']],
		['Gecko 210', ['500', '4000', '20000', '1000']],
		['Gecko 212', ['500', '4000', '20000', '1000']],
		['Gecko 320', ['3500', '500', '200', '200']],
		['Gecko 540', ['1000', '2000', '200', '200']],
		['L297', ['500', '4000', '4000', '1000']],
		['PMDX 150', ['1000', '2000', '1000', '1000']],
		['Sherline', ['22000', '22000', '100000', '100000']],
		['Xylotex BS-3', ['2000', '1000', '200', '200']],
		['Parker 750', ['1000', '1000', '1000', '200000']],
		['JVL SMD41/42', ['500', '500', '2500', '2500']],
		['Hobbycnc', ['2000', '2000', '2000', '2000']],
		['Keling 4030', ['5000', '5000', '20000', '20000']]
		]

	if combo == 'speed':
		comboList = [
		['GHz', 1000],
		['MHz', 1]
		]


	return comboList
"""
