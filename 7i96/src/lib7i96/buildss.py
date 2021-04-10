import os
from datetime import datetime

def build(parent):
	filePath = os.path.join(parent.configPath, 'sserial.hal')
	parent.outputPTE.appendPlainText(f'Building {filePath}')
	contents = []
	contents = ['# This file was created with the 7i96 Wizard on ']
	contents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	contents.append('# If you make changes to this file DO NOT use the Configuration Tool\n\n')
	if parent.smartSerialCardCB.currentIndex() > 0:
		contents.append(f'# Configuration file for the {parent.smartSerialCardCB.currentText()} Smart Serial Card\n\n')

	if parent.smartSerialCardCB.currentText() == '7i64':
		for i in range(24):
			if getattr(parent, 'ss7i64in_' + str(i)).currentData():
				inPin = getattr(parent, 'ss7i84in_' + str(i)).currentData()
				contents.append(f'net ss7i64in_{i} hm2_7i96.0.7i64.0.0.input-{i:02} <= {inPin}\n')
		for i in range(24):
			if getattr(parent, 'ss7i64out_' + str(i)).currentData():
				outPin = getattr(parent, 'ss7i84out_' + str(i)).currentData()
				contents.append(f'net ss7i64out_{i} hm2_7i96.0.7i64.0.0.output-{i:02} => {outPin}\n')

	elif parent.smartSerialCardCB.currentText() == '7i69':
		for i in range(24):
			if getattr(parent, 'ss7i69in_' + str(i)).currentData():
				inPin = getattr(parent, 'ss7i69in_' + str(i)).currentData()
				contents.append(f'net ss7i69in_{i} hm2_7i96.0.7i69.0.0.input-{i:02} <= {inPin}\n')
		for i in range(24):
			if getattr(parent, 'ss7i69out_' + str(i)).currentData():
				outPin = getattr(parent, 'ss7i69out_' + str(i)).currentData()
				contents.append(f'net ss7i69out_{i} hm2_7i96.0.7i69.0.0.output-{i:02} => {outPin}\n')

	elif parent.smartSerialCardCB.currentText() == '7i70':
		for i in range(48):
			if getattr(parent, 'ss7i70in_' + str(i)).currentData():
				inPin = getattr(parent, 'ss7i70in_' + str(i)).currentData()
				contents.append(f'net ss7i70in_{i} hm2_7i96.0.7i70.0.0.input-{i:02} <= {inPin}\n')

	elif parent.smartSerialCardCB.currentText() == '7i71':
		for i in range(48):
			if getattr(parent, 'ss7i71out_' + str(i)).currentData():
				inPin = getattr(parent, 'ss7i71out_' + str(i)).currentData()
				contents.append(f'net ss7i71out_{i} hm2_7i96.0.7i71.0.0.output-{i:02} <= {inPin}\n')

	elif parent.smartSerialCardCB.currentText() == '7i72':
		for i in range(48):
			if getattr(parent, 'ss7i72out_' + str(i)).currentData():
				inPin = getattr(parent, 'ss7i72out_' + str(i)).currentData()
				contents.append(f'net ss7i72out_{i} hm2_7i96.0.7i72.0.0.output-{i:02} <= {inPin}\n')
	elif parent.smartSerialCardCB.currentText() == '7i73':
		pass

	elif parent.smartSerialCardCB.currentText() == '7i84':
		for i in range(32):
			if getattr(parent, 'ss7i84in_' + str(i)).currentData():
				inPin = getattr(parent, 'ss7i84in_' + str(i)).currentData()
				contents.append(f'net ss7i84in_{i} hm2_7i96.0.7i84.0.0.input-{i:02} <= {inPin}\n')
		for i in range(16):
			if getattr(parent, 'ss7i84out_' + str(i)).currentData():
				outPin = getattr(parent, 'ss7i84out_' + str(i)).currentData()
				contents.append(f'net ss7i84out_{i} hm2_7i96.0.7i84.0.0.output-{i:02} => {outPin}\n')

	elif parent.smartSerialCardCB.currentText() == '7i87':
		pass

	try:
		with open(filePath, 'w') as f:
			f.writelines(contents)
	except OSError:
		parent.outputPTE.appendPlainText(f'OS error\n {traceback.print_exc()}')
