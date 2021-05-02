import os, configparser
from PyQt5.QtWidgets import (QFileDialog, QLabel, QLineEdit, QSpinBox,
	QDoubleSpinBox, QCheckBox, QGroupBox, QComboBox, QPushButton)

from lib7i96 import loadss

config = configparser.ConfigParser(strict=False)
config.optionxform = str

def openini(parent, fileName = ''):
	parent.tabWidget.setCurrentIndex(0)
	parent.outputPTE.clear()
	if not fileName:
		if os.path.isdir(os.path.expanduser('~/linuxcnc/configs')):
			configsDir = os.path.expanduser('~/linuxcnc/configs')
		else:
			configsDir = os.path.expanduser('~/')
		fileName = QFileDialog.getOpenFileName(parent,
		caption="Select Configuration INI File", directory=configsDir,
		filter='*.ini', options=QFileDialog.DontUseNativeDialog,)
		if fileName:
			parent.outputPTE.appendPlainText(f'Loading {fileName[0]}')
			iniFile = (fileName[0])
	else: # we passed a file name and path for testing
		iniFile = (fileName)

	if config.read(iniFile):
		if config.has_option('7i96', 'VERSION'):
			iniVersion = config['7i96']['VERSION']
			if iniVersion == parent.version:
				loadini(parent)
			else:
				msg = (f'The ini file version is {iniVersion}\n'
					'The Configuration Tool version is {parent.version}\n'
					'Try and open the ini?')
				if parent.errorMsg(msg, 'Version Difference'):
					loadini(parent)
		else:
			msg = ('This ini file may have been built with an older version\n'
				'Try and open?')
			if parent.errorMsg(msg, 'No Version'):
				loadini(parent)

def loadini(parent):
	# Section, Item, Object Name
	iniList = []
	#iniList.append(['EMC', 'VERSION', 'versionLE'])
	iniList.append(['EMC', 'MACHINE', 'configName'])
	iniList.append(['EMC', 'DEBUG', 'debugCB'])

	#iniList.append(['HOSTMOT2', 'DRIVER', 'driverCB'])
	iniList.append(['HOSTMOT2', 'IPADDRESS', 'ipAddressCB'])
	#iniList.append(['HOSTMOT2', 'BOARD', 'boardCB'])
	#iniList.append(['HOSTMOT2', 'STEPGENS', 'stepgensSB'])
	#iniList.append(['HOSTMOT2', 'ENCODERS', 'encodersSB'])
	#iniList.append(['HOSTMOT2', 'SSERIAL_PORT', 'sserialSB'])

	iniList.append(['DISPLAY', 'DISPLAY', 'guiCB'])
	iniList.append(['DISPLAY', 'POSITION_OFFSET', 'positionOffsetCB'])
	iniList.append(['DISPLAY', 'POSITION_FEEDBACK', 'positionFeedbackCB'])
	iniList.append(['DISPLAY', 'MAX_FEED_OVERRIDE', 'maxFeedOverrideSB'])

	iniList.append(['EMCMOT', 'SERVO_PERIOD', 'servoPeriodSB'])

	iniList.append(['TRAJ', 'LINEAR_UNITS', 'linearUnitsCB'])
	iniList.append(['TRAJ', 'COORDINATES', 'coordinatesLB'])
	iniList.append(['TRAJ', 'MAX_LINEAR_VELOCITY', 'maxLinearVel'])

	for i in range(parent.card['joints']):
		iniList.append([f'JOINT_{i}', 'AXIS', f'axisCB_{i}'])
		iniList.append([f'JOINT_{i}', 'STEPLEN', f'stepTime_{i}'])
		iniList.append([f'JOINT_{i}', 'STEPSPACE', f'stepSpace_{i}'])
		iniList.append([f'JOINT_{i}', 'DIRSETUP', f'dirSetup_{i}'])
		iniList.append([f'JOINT_{i}', 'DIRHOLD', f'dirHold_{i}'])
		iniList.append([f'JOINT_{i}', 'MIN_LIMIT', f'minLimit_{i}'])
		iniList.append([f'JOINT_{i}', 'MAX_LIMIT', f'maxLimit_{i}'])
		iniList.append([f'JOINT_{i}', 'MAX_VELOCITY', f'maxVelocity_{i}'])
		iniList.append([f'JOINT_{i}', 'MAX_ACCELERATION', f'maxAccel_{i}'])
		iniList.append([f'JOINT_{i}', 'SCALE', f'scale_{i}'])
		iniList.append([f'JOINT_{i}', 'HOME', f'home_{i}'])
		iniList.append([f'JOINT_{i}', 'HOME_OFFSET', f'homeOffset_{i}'])
		iniList.append([f'JOINT_{i}', 'HOME_SEARCH_VEL', f'homeSearchVel_{i}'])
		iniList.append([f'JOINT_{i}', 'HOME_LATCH_VEL', f'homeLatchVel_{i}'])
		iniList.append([f'JOINT_{i}', 'HOME_USE_INDEX', f'homeUseIndex_{i}'])
		iniList.append([f'JOINT_{i}', 'HOME_IGNORE_LIMITS', f'homeIgnoreLimits_{i}'])
		iniList.append([f'JOINT_{i}', 'HOME_SEQUENCE', f'homeSequence_{i}'])
		iniList.append([f'JOINT_{i}', 'P', f'p_{i}'])
		iniList.append([f'JOINT_{i}', 'I', f'i_{i}'])
		iniList.append([f'JOINT_{i}', 'D', f'd_{i}'])
		iniList.append([f'JOINT_{i}', 'FF0', f'ff0_{i}'])
		iniList.append([f'JOINT_{i}', 'FF1', f'ff1_{i}'])
		iniList.append([f'JOINT_{i}', 'FF2', f'ff2_{i}'])
		iniList.append([f'JOINT_{i}', 'DEADBAND', f'deadband_{i}'])
		iniList.append([f'JOINT_{i}', 'BIAS', f'bias_{i}'])
		iniList.append([f'JOINT_{i}', 'MAX_OUTPUT', f'maxOutput_{i}'])
		iniList.append([f'JOINT_{i}', 'MAX_ERROR', f'maxError_{i}'])

	iniList.append(['SPINDLE', 'SPINDLE_TYPE', 'spindleTypeCB'])
	iniList.append(['SPINDLE', 'SCALE', 'spindleScale'])
	iniList.append(['SPINDLE', 'PWM_FREQUENCY', 'pwmFrequencySB'])
	iniList.append(['SPINDLE', 'MAX_RPM', 'spindleMaxRpm'])
	iniList.append(['SPINDLE', 'MIN_RPM', 'spindleMinRpm'])
	iniList.append(['SPINDLE', 'DEADBAND', 'deadband_s'])
	iniList.append(['SPINDLE', 'P', 'p_s'])
	iniList.append(['SPINDLE', 'I', 'i_s'])
	iniList.append(['SPINDLE', 'D', 'd_s'])
	iniList.append(['SPINDLE', 'FF0', 'ff0_s'])
	iniList.append(['SPINDLE', 'FF1', 'ff1_s'])
	iniList.append(['SPINDLE', 'FF2', 'ff2_s'])
	iniList.append(['SPINDLE', 'BIAS', 'bias_s'])
	iniList.append(['SPINDLE', 'MAX_ERROR', 'maxError_s'])

	for i in range(parent.card['inputs']):
		iniList.append(['INPUT_PB', f'INPUT_PB_{i}', f'inputPB_{i}'])
		iniList.append(['INPUT_PB', f'INPUT_INVERT_{i}', f'inputInvertCB_{i}'])

	for i in range(parent.card['outputs']):
		iniList.append(['OUTPUT_PB', f'OUTPUT_PB_{i}', f'outputPB_{i}'])

	iniList.append(['OPTIONS', 'INTRO_GRAPHIC', 'introGraphicLE'])
	iniList.append(['OPTIONS', 'INTRO_GRAPHIC_TIME', 'splashScreenSB'])
	iniList.append(['OPTIONS', 'MANUAL_TOOL_CHANGE', 'manualToolChangeCB'])
	iniList.append(['OPTIONS', 'CUSTOM_HAL', 'customhalCB'])
	iniList.append(['OPTIONS', 'POST_GUI_HAL', 'postguiCB'])
	iniList.append(['OPTIONS', 'SHUTDOWN_HAL', 'shutdownCB'])
	iniList.append(['OPTIONS', 'HALUI', 'haluiCB'])
	iniList.append(['OPTIONS', 'PYVCP', 'pyvcpCB'])
	iniList.append(['OPTIONS', 'GLADEVCP', 'gladevcpCB'])
	iniList.append(['OPTIONS', 'LADDER', 'ladderGB'])
	iniList.append(['OPTIONS', 'LADDER_RUNGS', 'ladderRungsSB'])
	iniList.append(['OPTIONS', 'BACKUP', 'backupCB'])
	iniList.append(['SSERIAL', 'SS_CARD', 'ssCardCB'])

#iniList.append(['', '', ''])
	# iniList section, item, value
	for item in iniList:
		if config.has_option(item[0], item[1]):
			if isinstance(getattr(parent, item[2]), QLabel):
				getattr(parent, item[2]).setText(config[item[0]][item[1]])
			elif isinstance(getattr(parent, item[2]), QLineEdit):
				getattr(parent, item[2]).setText(config[item[0]][item[1]])
			elif isinstance(getattr(parent, item[2]), QSpinBox):
				getattr(parent, item[2]).setValue(abs(int(config[item[0]][item[1]])))
			elif isinstance(getattr(parent, item[2]), QDoubleSpinBox):
				getattr(parent, item[2]).setValue(float(config[item[0]][item[1]]))
			elif isinstance(getattr(parent, item[2]), QCheckBox):
				getattr(parent, item[2]).setChecked(eval(config[item[0]][item[1]]))
			elif isinstance(getattr(parent, item[2]), QGroupBox):
				getattr(parent, item[2]).setChecked(eval(config[item[0]][item[1]]))
			elif isinstance(getattr(parent, item[2]), QComboBox):
				index = getattr(parent, item[2]).findData(config[item[0]][item[1]])
				if index >= 0:
					getattr(parent, item[2]).setCurrentIndex(index)
			elif isinstance(getattr(parent, item[2]), QPushButton):
				getattr(parent, item[2]).setText(config[item[0]][item[1]])
			else:
				print(item[2])

	parent.outputPTE.appendPlainText('INI file Loaded')

	if config.has_section('SSERIAL'):
		card = config.get('SSERIAL', 'ssCardCB')
		index = parent.ssCardCB.findText(card)
		if index > 0:
			parent.ssCardCB.setCurrentIndex(index)
		loadss.load(parent, config)
	parent.outputPTE.appendPlainText('Smart Serial file Loaded')
