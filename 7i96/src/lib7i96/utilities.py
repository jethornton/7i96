import os, subprocess
from PyQt5.QtWidgets import QMessageBox

def checks(parent):
	try:
		subprocess.check_output('mesaflash', encoding='UTF-8')
	except FileNotFoundError:
		t = ('Mesaflash not found go to\n'
			'https://github.com/LinuxCNC/mesaflash\n'
			'for installation instructions.')
		parent.outputPTE.appendPlainText(t)
		parent.readPB.setEnabled(False)
		parent.flashPB.setEnabled(False)
		parent.reloadPB.setEnabled(False)

def axisChanged(parent):
	joint = parent.sender().objectName()[-1]
	axis = parent.sender().currentText()
	if axis in ['X', 'Y', 'Z', 'U', 'V', 'W']:
		getattr(parent, f'axisType_{joint}').setText('LINEAR')
	elif axis in ['A', 'B', 'C']:
		getattr(parent, f'axisType_{joint}').setText('ANGULAR')
	else:
		getattr(parent, f'axisType_{joint}').setText('')
	coordList = []
	for i in range(6):
		axisLetter = getattr(parent, f'axisCB_{i}').currentText()
		if axisLetter != 'Select':
			coordList.append(axisLetter)
		parent.coordinatesLB.setText(''.join(coordList))
		parent.axes = len(parent.coordinatesLB.text())

def configNameChanged(parent, text):
	if text:
		parent.configNameUnderscored = text.replace(' ','_').lower()
		parent.configPath = os.path.expanduser('~/linuxcnc/configs') + '/' + parent.configNameUnderscored
		parent.pathLabel.setText(parent.configPath)
	else:
		parent.pathLabel.setText('')

def pidSetDefault(parent):
	tab = parent.sender().objectName()[-1]
	if not parent.linearUnitsCB.currentData():
		QMessageBox.warning(parent,'Warning', 'Machine Tab\nLinear Units\nmust be selected', QMessageBox.Ok)
		return
	p = int(1000/(int(parent.servoPeriodSB.cleanText())/1000000))
	getattr(parent, 'p_' + tab).setText(f'{p}')
	getattr(parent, 'i_' + tab).setText('0')
	getattr(parent, 'd_' + tab).setText('0')
	getattr(parent, 'ff0_' + tab).setText('0')
	getattr(parent, 'ff1_' + tab).setText('1')
	getattr(parent, 'ff2_' + tab).setText('0.00013')
	getattr(parent, 'bias_' + tab).setText('0')
	getattr(parent, 'maxOutput_' + tab).setText('0')
	if parent.linearUnitsCB.itemData(parent.linearUnitsCB.currentIndex()) == 'inch':
		maxError = '0.0005'
	else:
		maxError = '0.0127'
	getattr(parent, 'maxError_' + tab).setText(maxError)
	getattr(parent, 'deadband_' + tab).setText('0')

def driveChanged(parent):
	timing = parent.sender().itemData(parent.sender().currentIndex())
	joint = parent.sender().objectName()[-1]
	if timing:
		getattr(parent, 'stepTime_' + joint).setText(timing[0])
		getattr(parent, 'stepSpace_' + joint).setText(timing[1])
		getattr(parent, 'dirSetup_' + joint).setText(timing[2])
		getattr(parent, 'dirHold_' + joint).setText(timing[3])
		getattr(parent, 'stepTime_' + joint).setEnabled(False)
		getattr(parent, 'stepSpace_' + joint).setEnabled(False)
		getattr(parent, 'dirSetup_' + joint).setEnabled(False)
		getattr(parent, 'dirHold_' + joint).setEnabled(False)
	else:
		getattr(parent, 'stepTime_' + joint).setEnabled(True)
		getattr(parent, 'stepSpace_' + joint).setEnabled(True)
		getattr(parent, 'dirSetup_' + joint).setEnabled(True)
		getattr(parent, 'dirHold_' + joint).setEnabled(True)

def plcOptions():
	return ['ladderRungsSB', 'ladderBitsSB', 'ladderWordsSB',
	'ladderTimersSB', 'iecTimerSB', 'ladderMonostablesSB', 'ladderCountersSB',
	'ladderInputsSB', 'ladderOutputsSB', 'ladderExpresionsSB',
	'ladderSectionsSB', 'ladderSymbolsSB', 'ladderS32InputsSB',
	'ladderS32OuputsSB', 'ladderFloatInputsSB', 'ladderFloatOutputsSB']
