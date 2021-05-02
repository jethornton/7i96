import os, subprocess
from PyQt5.QtWidgets import QMessageBox, QApplication

def isNumber(s):
	try:
		s[-1].isdigit()
		float(s)
		return True
	except ValueError:
		return False

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
	for i in range(parent.card['joints']):
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

def updateAxisInfo(parent):
	if parent.sender().objectName() == 'actionOpen':
		return
	joint = parent.sender().objectName()[-1]
	scale = getattr(parent, 'scale_' + joint).text()
	if scale and isNumber(scale):
		scale = float(scale)
	else:
		return

	maxVelocity = getattr(parent, 'maxVelocity_' + joint).text()
	if maxVelocity and isNumber(maxVelocity):
		maxVelocity = float(maxVelocity)
	else:
		return

	maxAccel = getattr(parent, 'maxAccel_' + joint).text()
	if maxAccel and isNumber(maxAccel):
		maxAccel = float(maxAccel)
	else:
		return

	if not parent.linearUnitsCB.currentData():
		parent.errorDialog('Machine Tab:\nLinear Units must be selected')
		return
	accelTime = maxVelocity / maxAccel
	getattr(parent, 'timeJoint_' + joint).setText(f'{accelTime:.2f} seconds')
	accelDistance = accelTime * 0.5 * maxVelocity
	getattr(parent, 'distanceJoint_' + joint).setText(f'{accelDistance:.2f} {parent.linearUnitsCB.currentData()}')
	stepRate = scale * maxVelocity
	getattr(parent, 'stepRateJoint_' + joint).setText(f'{abs(stepRate):.0f} pulses')

def spindleTypeChanged(parent): 
	#print(parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex()))
	if parent.spindleTypeCB.currentData():
		parent.spindleGB.setEnabled(True)
		parent.spindleInfoGB.setEnabled(True)
		parent.encoderGB.setEnabled(True)
		parent.spindlepidGB.setEnabled(True)
		if parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex()) == '1':
			parent.spindleInfo1Lbl.setText("PWM on Step 4")
			parent.tb2p3LB.setText("PWM +")
			parent.tb2p2LB.setText("PWM -")
			parent.spindleInfo2Lbl.setText("Direction on Dir 4")
			parent.tb2p5LB.setText("Direction +")
			parent.tb2p4LB.setText("Direction -")
			parent.spindleInfo3Lbl.setText("Select Enable on the Outputs tab")
		if parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex()) == '2':
			parent.spindleInfo1Lbl.setText("UP on Step 4")
			parent.tb2p3LB.setText("UP +")
			parent.tb2p2LB.setText("UP -")
			parent.spindleInfo2Lbl.setText("Down on Dir 4")
			parent.tb2p5LB.setText("DOWN +")
			parent.tb2p4LB.setText("DOWN -")
			parent.spindleInfo3Lbl.setText("Select Enable on the Outputs tab")
		if parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex()) == '3':
			parent.spindleInfo1Lbl.setText("PDM on Step 4")
			parent.tb2p3LB.setText("PDM +")
			parent.tb2p2LB.setText("PDM -")
			parent.spindleInfo2Lbl.setText("Direction on Dir 4")
			parent.tb2p5LB.setText("Direction +")
			parent.tb2p4LB.setText("Direction -")
			parent.spindleInfo3Lbl.setText("Select Enable on the Outputs tab")
		if parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex()) == '4':
			parent.spindleInfo1Lbl.setText("Direction on Step 4")
			parent.tb2p3LB.setText("Direction +")
			parent.tb2p2LB.setText("Direction -")
			parent.spindleInfo2Lbl.setText("PWM on Dir 4")
			parent.tb2p5LB.setText("PWM +")
			parent.tb2p4LB.setText("PWM -")
			parent.spindleInfo3Lbl.setText("Select Enable on the Outputs tab")


def fileNew(parent):
	parent.errorMsgOk('Close the Tool,\n Then open', 'Info!')

def fileSaveAs(parent):
	parent.errorMsgOk('Change the Name,\n Then Save', 'Info!')

def copyOutput(parent):
	qclip = QApplication.clipboard()
	qclip.setText(parent.outputPTE.toPlainText())
	parent.statusbar.showMessage('Output copied to clipboard')
