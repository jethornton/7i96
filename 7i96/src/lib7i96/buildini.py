import os
from datetime import datetime

def build(parent):
	buildErrors = []
	iniFilePath = os.path.join(parent.configPath, parent.configNameUnderscored + '.ini')
	parent.outputPTE.appendPlainText(f'Building {iniFilePath}')

	if os.path.isfile(iniFilePath):
		pass

	if not os.path.exists(parent.configPath):
		try:
			os.mkdir(parent.configPath)
		except OSError:
			parent.outputPTE.appendPlainText(f'OS error\n {traceback.print_exc()}')

	iniContents = ['# This file was created with the 7i96 Configuration Tool on ']
	iniContents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	iniContents.append('# Changes to most things are ok and will be read by the Configuration Tool\n')

	# build the [7I96] section
	iniContents.append('\n[7I96]\n')
	iniContents.append(f'VERSION = {parent.version}\n')

	# build the [EMC] section
	iniContents.append('\n[EMC]\n')
	iniContents.append(f'VERSION = {parent.versionLE.text()}\n')
	iniContents.append(f'MACHINE = {parent.configNameUnderscored}\n')
	iniContents.append(f'DEBUG = {parent.debugCB.currentData()}\n')

	# build the [HOSTMOT2] section
	iniContents.append('\n[HOSTMOT2]\n')
	iniContents.append('DRIVER = hm2_eth\n')
	iniContents.append(f'IPADDRESS = {parent.ipAddressCB.currentData()}\n')
	iniContents.append('BOARD = 7i96\n')
	iniContents.append(f'STEPGENS = {str(parent.stepgensCB.currentData())}\n')
	iniContents.append(f'ENCODERS = {str(parent.encodersCB.currentData())}\n')
	iniContents.append(f'PWMS = {str(parent.pwmsCB.currentData())}\n')
	iniContents.append(f'SSERIAL_PORT = {str(parent.sserialSB.value())}\n')
	iniContents.append(f'FIRMWARE = {parent.firmwareCB.currentData()}\n')

	# build the [DISPLAY] section maxFeedOverrideLE
	iniContents.append('\n[DISPLAY]\n')
	iniContents.append(f'DISPLAY = {parent.guiCB.itemData(parent.guiCB.currentIndex())}\n')
	iniContents.append(f'POSITION_OFFSET = {parent.positionOffsetCB.currentData()}\n')
	iniContents.append(f'POSITION_FEEDBACK = {parent.positionFeedbackCB.currentData()}\n')
	iniContents.append(f'MAX_FEED_OVERRIDE = {parent.maxFeedOverrideSB.value()}\n')
	iniContents.append('CYCLE_TIME = 0.1\n')
	if parent.splashScreenCB.isChecked():
		iniContents.append(f'INTRO_GRAPHIC = {parent.introGraphicLE.text()}\n')
		iniContents.append(f'INTRO_TIME = {parent.splashScreenSB.value()}\n')
	iniContents.append('OPEN_FILE = "{}"\n'.format(''))
	if parent.pyvcpCB.isChecked():
		iniContents.append(f'PYVCP = {parent.configNameUnderscored}.xml\n')
	if parent.frontToolLatheCB.isChecked():
		iniContents.append('LATHE = 1\n')
	if parent.frontToolLatheCB.isChecked():
		iniContents.append('BACK_TOOL_LATHE = 1\n')

	# build the [KINS] section
	iniContents.append('\n[KINS]\n')
	if len(set(parent.coordinatesLB.text())) == len(parent.coordinatesLB.text()): # 1 joint for each axis
		iniContents.append('KINEMATICS = {} coordinates={}\n'.format('trivkins', parent.coordinatesLB.text()))
	else: # more than one joint per axis
		iniContents.append(f'KINEMATICS = trivkins coordinates={parent.coordinatesLB.text()} kinstype=BOTH\n')
	iniContents.append(f'JOINTS = {len(parent.coordinatesLB.text())}\n')

	# build the [EMCIO] section
	iniContents.append('\n[EMCIO]\n')
	iniContents.append('EMCIO = iov2\n')
	iniContents.append('CYCLE_TIME = 0.100\n')
	iniContents.append('TOOL_TABLE = tool.tbl\n')

	# build the [RS274NGC] section
	iniContents.append('\n[RS274NGC]\n')
	iniContents.append(f'PARAMETER_FILE = {parent.configNameUnderscored}.var\n')

	# build the [EMCMOT] section
	iniContents.append('\n[EMCMOT]\n')
	iniContents.append('EMCMOT = motmod\n')
	iniContents.append(f'SERVO_PERIOD = {parent.servoPeriodSB.value()}\n')

	# build the [TASK] section
	iniContents.append('\n[TASK]\n')
	iniContents.append('TASK = milltask\n')
	iniContents.append('CYCLE_TIME = 0.010\n')

	# build the [TRAJ] section
	iniContents.append('\n[TRAJ]\n')
	iniContents.append(f'COORDINATES = {parent.coordinatesLB.text()}\n')
	iniContents.append(f'LINEAR_UNITS = {parent.linearUnitsCB.currentData()}\n')
	iniContents.append(f'ANGULAR_UNITS = {parent.angularUnitsCB.currentData()}\n')
	iniContents.append(f'MAX_LINEAR_VELOCITY = {parent.maxLinearVel.text()}\n')

	# build the [HAL] section
	iniContents.append('\n[HAL]\n')
	iniContents.append(f'HALFILE = {parent.configNameUnderscored}.hal\n')
	iniContents.append('HALFILE = io.hal\n')
	if parent.ssCardCB.currentData():
		iniContents.append('HALFILE = sserial.hal\n')
	if parent.customhalCB.isChecked():
		iniContents.append('HALFILE = custom.hal\n')
	if parent.postguiCB.isChecked():
		iniContents.append('POSTGUI_HALFILE = postgui.hal\n')
	if parent.shutdownCB.isChecked():
		iniContents.append('SHUTDOWN = shutdown.hal\n')
	if parent.haluiCB.isChecked():
		iniContents.append('HALUI = halui\n')

	# build the [HALUI] section
	iniContents.append('\n[HALUI]\n')

	# build the axes
	for index in range(5):
		axis = getattr(parent,'axisCB_' + str(index)).currentData()
		if axis:
			jointTab = getattr(parent,'axisCB_' + str(index)).objectName()[7]
			iniContents.append(f'\n[AXIS_{axis}]\n')
			iniContents.append(f'MIN_LIMIT = {getattr(parent, "minLimit_" + jointTab).text()}\n')
			iniContents.append(f'MAX_LIMIT = {getattr(parent, "maxLimit_" + jointTab).text()}\n')
			iniContents.append(f'MAX_VELOCITY = {getattr(parent, "maxVelocity_" + jointTab).text()}\n')
			iniContents.append(f'MAX_ACCELERATION = {getattr(parent, "maxAccel_" + jointTab).text()}\n')

	# build the [JOINT_n] sections
	for i in range(5):
		if getattr(parent, "axisCB_" + str(i)).currentData():
			iniContents.append(f'\n[JOINT_{i}]\n')
			iniContents.append(f'AXIS = {getattr(parent, "axisCB_" + str(i)).currentData()}\n')
			iniContents.append(f'MIN_LIMIT = {getattr(parent, "minLimit_" + str(i)).text()}\n')
			iniContents.append(f'MAX_LIMIT = {getattr(parent, "maxLimit_" + str(i)).text()}\n')
			iniContents.append(f'MAX_VELOCITY = {getattr(parent, "maxVelocity_" + str(i)).text()}\n')
			iniContents.append(f'MAX_ACCELERATION = {getattr(parent, "maxAccel_" + str(i)).text()}\n')
			iniContents.append(f'TYPE = {getattr(parent, "axisType_" + str(i)).text()}\n')
			if parent.reverse_0.isChecked():
				iniContents.append(f'SCALE = -{getattr(parent, "scale_" + str(i)).text()}\n')
			else:
				iniContents.append(f'SCALE = {getattr(parent, "scale_" + str(i)).text()}\n')
			iniContents.append(f'STEPGEN_MAX_VEL = {str(float(getattr(parent, "maxVelocity_" + str(i)).text()) * 1.2)}\n')
			iniContents.append(f'STEPGEN_MAX_ACC = {str(float(getattr(parent, "maxAccel_" + str(i)).text()) * 1.2)}\n')
			if parent.units == 'inches':
				iniContents.append('FERROR = 0.0002\n')
				iniContents.append('MIN_FERROR = 0.0001\n')
			else:
				iniContents.append('FERROR = 0.0051\n')
				iniContents.append('MIN_FERROR = 0.0025\n')
			iniContents.append(f'DIRSETUP = {getattr(parent, "dirSetup_" + str(i)).text()}\n')
			iniContents.append(f'DIRHOLD = {getattr(parent, "dirHold_" + str(i)).text()}\n')
			iniContents.append(f'STEPLEN = {getattr(parent, "stepTime_" + str(i)).text()}\n')
			iniContents.append(f'STEPSPACE = {getattr(parent, "stepSpace_" + str(i)).text()}\n')
			iniContents.append(f'DEADBAND = {getattr(parent, "deadband_" + str(i)).text()}\n')
			iniContents.append(f'P = {getattr(parent, "p_" + str(i)).text()}\n')
			iniContents.append(f'I = {getattr(parent, "i_" + str(i)).text()}\n')
			iniContents.append(f'D = {getattr(parent, "d_" + str(i)).text()}\n')
			iniContents.append(f'FF0 = {getattr(parent, "ff0_" + str(i)).text()}\n')
			iniContents.append(f'FF1 = {getattr(parent, "ff1_" + str(i)).text()}\n')
			iniContents.append(f'FF2 = {getattr(parent, "ff2_" + str(i)).text()}\n')
			iniContents.append(f'BIAS = {getattr(parent, "bias_" + str(i)).text()}\n')
			iniContents.append(f'MAX_OUTPUT = {getattr(parent, "maxOutput_" + str(i)).text()}\n')
			iniContents.append(f'MAX_ERROR = {getattr(parent, "maxError_" + str(i)).text()}\n')

	# build the [SPINDLE] section if enabled
	#print(parent.spindleTypeCB.currentText())
	if parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex()):
		iniContents.append('\n[SPINDLE]\n')
		iniContents.append('OUTPUT_TYPE = {}\n'.format(parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex())))
		iniContents.append('SCALE = {}\n'.format(parent.spindleScale.text()))
		iniContents.append('PWM_FREQUENCY = {}\n'.format(parent.pwmFrequencySB.value()))
		iniContents.append('MAX_RPM = {}\n'.format(parent.spindleMaxRpm.text()))
		iniContents.append('MIN_RPM = {}\n'.format(parent.spindleMinRpm.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_s.text()))
		iniContents.append('P = {}\n'.format(parent.p_s.text()))
		iniContents.append('I = {}\n'.format(parent.i_s.text()))
		iniContents.append('D = {}\n'.format(parent.d_s.text()))
		iniContents.append('FF0 = {}\n'.format(parent.ff0_s.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_s.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_s.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_s.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_s.text()))

	iniContents.append('\n# Everything below this line is only used to\n')
	iniContents.append('# setup the Configuration Tool when loading the ini.\n')

	# build the [INPUTS] section
	iniContents.append('\n[INPUTS]\n')
	iniContents.append('# DO NOT change the inputs text\n')
	for i in range(11):
		iniContents.append(f'INPUT_{i} = {getattr(parent, "input_" + str(i)).currentText()}\n')
		iniContents.append(f'INPUT_DIR_{i} = {getattr(parent, "inputInvert_" + str(i)).currentText()}\n')
		iniContents.append(f'INPUT_JOINT_{i} = {getattr(parent, "inputJoint_" + str(i)).currentData()}\n')

	# build the [OUTPUTS] section
	iniContents.append('\n[OUTPUTS]\n')
	iniContents.append('# DO NOT change the outputs text\n')
	for i in range(5):
		iniContents.append(f'OUTPUT_{i} = {getattr(parent, "output_" + str(i)).currentText()}\n')

	# build the [OPTIONS] section
	iniContents.append('\n[OPTIONS]\n')
	iniContents.append('# DO NOT change the options text\n')
	iniContents.append(f'INTRO_GRAPHIC = {parent.splashScreenCB.isChecked()}\n')
	iniContents.append(f'MANUAL_TOOL_CHANGE = {parent.manualToolChangeCB.isChecked()}\n'.format())
	iniContents.append(f'HALUI = {parent.haluiCB.isChecked()}\n')
	iniContents.append(f'PYVCP = {parent.pyvcpCB.isChecked()}\n')
	iniContents.append(f'GLADEVCP = {parent.gladevcpCB.isChecked()}\n')
	iniContents.append(f'LADDER = {parent.ladderGB.isChecked()}\n')
	iniContents.append(f'BACKUP = {parent.backupCB.isChecked()}\n')
	if parent.ladderGB.isChecked(): # check for any options
		for option in parent.ladderOptionsList:
			if getattr(parent, option).value() > 0: #******** work to be done here
				iniContents.append('{} = {}\n'.format(getattr(parent, option).property('item'), getattr(parent, option).value()))

	# build the [SSERIAL] section
	if parent.ssCardCB.currentData():
		iniContents.append('\n[SSERIAL]\n')
		iniContents.append('# DO NOT change the sserial text\n')
		iniContents.append(f'ssCardCB = {parent.ssCardCB.currentText()}\n')
	if parent.ssCardCB.currentText() == '7i64':
		# 24 ss7i64in_
		# 24 ss7i64out_
		for i in range(24):
			iniContents.append(f'ss7i64in_{i} = {getattr(parent, "ss7i64in_" + str(i)).currentData()}\n')
		for i in range(24):
			iniContents.append(f'ss7i64out_{i} = {getattr(parent, "ss7i64out_" + str(i)).currentData()}\n')

	elif parent.ssCardCB.currentText() == '7i69':
		print('here')
		# 24 ss7i69in_
		# 24 ss7i69out_
		for i in range(24):
			iniContents.append(f'SS_INPUT_{i} = {getattr(parent, "ss7i69in_" + str(i)).currentData()}\n')
		for i in range(24):
			iniContents.append(f'SS_OUTPUT_{i} = {getattr(parent, "ss7i69out_" + str(i)).currentData()}\n')

	elif parent.ssCardCB.currentText() == '7i70':
		# 48 ss7i70in_
		for i in range(48):
			iniContents.append(f'SS_INPUT_{i} = {getattr(parent, "ss7i70in_" + str(i)).currentData()}\n')

	elif parent.ssCardCB.currentText() == '7i71':
		# 48 ss7i71out_
		for i in range(48):
			iniContents.append(f'SS_OUTPUT_{i} = {getattr(parent, "ss7i71out_" + str(i)).currentData()}\n')

	elif parent.ssCardCB.currentText() == '7i72':
		# 48 ss7i72out_
		for i in range(48):
			iniContents.append(f'SS_OUTPUT_{i} = {getattr(parent, "ss7i72out_" + str(i)).currentData()}\n')

	elif parent.ssCardCB.currentText() == '7i73':
		# 16 ss7i73key_
		# 12 ss7i73lcd_
		# 16 ss7i73in_
		# 2 ss7i73out_
		for i in range(16):
			iniContents.append(f'SS_KEY_{i} = {getattr(parent, "ss7i73key_" + str(i)).currentData()}\n')
		for i in range(12):
			iniContents.append(f'SS_LCD_{i} = {getattr(parent, "ss7i73lcd_" + str(i)).currentData()}\n')
		for i in range(16):
			iniContents.append(f'SS_INPUT_{i} = {getattr(parent, "ss7i73in_" + str(i)).currentData()}\n')
		for i in range(2):
			iniContents.append(f'SS_OUTPUT_{i} = {getattr(parent, "ss7i73out_" + str(i)).currentData()}\n')

	elif parent.ssCardCB.currentText() == '7i84':
		# 32 ss7i84in_
		# 16 ss7i84out_
		for i in range(32):
			iniContents.append(f'SS_INPUT_{i} = {getattr(parent, "ss7i84in_" + str(i)).currentData()}\n')
		for i in range(16):
			iniContents.append(f'SS_OUTPUT_{i} = {getattr(parent, "ss7i84out_" + str(i)).currentData()}\n')

	elif parent.ssCardCB.currentText() == '7i87':
		# 8 ss7i87in_
		for i in range(8):
			iniContents.append(f'SS_INPUT_{i} = {getattr(parent, "ss7i87in_" + str(i)).currentData()}\n')

	try:
		with open(iniFilePath, 'w') as iniFile:
			iniFile.writelines(iniContents)
	except OSError:
		parent.outputPTE.appendPlainText(f'OS error\n {traceback.print_exc()}')
