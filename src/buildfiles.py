import os
from datetime import datetime

"""
	linuxcncDir = os.path.expanduser('~/linuxcnc')
	test = '~/linuxcnc/configs/' + 'fred'
	print(os.path.expanduser(self.test))
	configsDir = os.path.expanduser('~/linuxcnc/configs')
	gcodeDir = os.path.expanduser('~/linuxcnc/nc_files')
	subroutineDir = os.path.expanduser('~/linuxcnc/subroutines')

"""

def builddirs(parent):
	if not os.path.exists(os.path.expanduser('~/linuxcnc')):
		os.mkdir(os.path.expanduser('~/linuxcnc'))
	if not os.path.exists(os.path.expanduser('~/linuxcnc/configs')):
		os.mkdir(os.path.expanduser('~/linuxcnc/configs'))
	if not os.path.exists(os.path.expanduser('~/linuxcnc/nc_files')):
		os.mkdir(os.path.expanduser('~/linuxcnc/nc_files'))
	if not os.path.exists(os.path.expanduser('~/linuxcnc/subroutines')):
		os.mkdir(os.path.expanduser('~/linuxcnc/subroutines'))
	return True

def buildini(parent):
	buildErrors = []
	buildini.result = ''
	iniFilePath = os.path.join(parent.configPath, parent.configNameUnderscored + '.ini')

	if not os.path.exists(parent.configPath):
		os.mkdir(parent.configPath)

	iniContents = ['# This file was created with the 7i96 Configuration Tool on ']
	iniContents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	iniContents.append('# Changes to most things are ok and will be read by the Configuration Tool\n')

	# build the [EMC] section
	iniContents.append('\n[EMC]\n')
	iniContents.append('VERSION = {}\n'.format(parent.versionLE.text()))
	iniContents.append('MACHINE = {}\n'.format(parent.configNameUnderscored))
	iniContents.append('DEBUG = {}\n'.format(parent.debugCombo.itemData(parent.debugCombo.currentIndex())))

	# build the [HOSTMOT2] section
	iniContents.append('\n[HOSTMOT2]\n')
	iniContents.append('DRIVER = {}\n'.format('hm2_eth'))
	iniContents.append('IPADDRESS = {}\n'.format(parent.ipAddressCB.itemData(parent.ipAddressCB.currentIndex())))
	iniContents.append('BOARD = 7i96\n')
	iniContents.append('STEPGENS = {}\n'.format(str(parent.stepgensSB.value())))
	iniContents.append('ENCODERS = {}\n'.format(str(parent.encodersSB.value())))
	iniContents.append('SSERIAL_PORT = {}\n'.format(str(parent.sserialSB.value())))

	# build the [DISPLAY] section maxFeedOverrideLE
	iniContents.append('\n[DISPLAY]\n')
	iniContents.append('DISPLAY = {}\n'.format(parent.guiCB.itemData(parent.guiCB.currentIndex())))
	iniContents.append('POSITION_OFFSET = {}\n'.format(parent.positionOffsetCB.itemData(parent.positionOffsetCB.currentIndex())))
	iniContents.append('POSITION_FEEDBACK = {}\n'.format(parent.positionFeedbackCB.itemData(parent.positionFeedbackCB.currentIndex())))
	iniContents.append('MAX_FEED_OVERRIDE = {}\n'.format(parent.maxFeedOverrideSB.value()))
	iniContents.append('CYCLE_TIME = {}\n'.format('0.1'))
	iniContents.append('INTRO_GRAPHIC = {}\n'.format('emc2.gif'))
	iniContents.append('INTRO_TIME = {}\n'.format('0'))
	iniContents.append('OPEN_FILE = "{}"\n'.format(''))
	if parent.pyvcpCB.isChecked():
		iniContents.append('PYVCP = {}.xml\n'.format(parent.configNameUnderscored))
	if parent.frontToolLatheCB.isChecked():
		iniContents.append('LATHE = 1\n')
	if parent.frontToolLatheCB.isChecked():
		iniContents.append('BACK_TOOL_LATHE = 1\n')

	# build the [KINS] section
	iniContents.append('\n[KINS]\n')
	if len(set(parent.coordinatesLB.text())) == len(parent.coordinatesLB.text()): # 1 joint for each axis
		iniContents.append('KINEMATICS = {} coordinates={}\n'.format('trivkins', parent.coordinatesLB.text()))
	else: # more than one joint per axis
		iniContents.append('KINEMATICS = {} coordinates={} kinstype=BOTH\n'.format('trivkins', parent.coordinatesLB.text()))
	iniContents.append('JOINTS = {}\n'.format(len(parent.coordinatesLB.text())))

	# build the [EMCIO] section
	iniContents.append('\n[EMCIO]\n')
	iniContents.append('EMCIO = {}\n'.format('io'))
	iniContents.append('CYCLE_TIME = {}\n'.format('0.100'))
	iniContents.append('TOOL_TABLE = tool.tbl\n')

	# build the [RS274NGC] section
	iniContents.append('\n[RS274NGC]\n')
	iniContents.append('PARAMETER_FILE = {}.var\n'.format(parent.configNameUnderscored))

	# build the [EMCMOT] section
	iniContents.append('\n[EMCMOT]\n')
	iniContents.append('EMCMOT = {}\n'.format('motmod'))
	iniContents.append('SERVO_PERIOD = {}\n'.format(parent.servoPeriodSB.value()))

	# build the [TASK] section
	iniContents.append('\n[TASK]\n')
	iniContents.append('TASK = {}\n'.format('milltask'))
	iniContents.append('CYCLE_TIME = {}\n'.format('0.010'))

	# build the [TRAJ] section
	iniContents.append('\n[TRAJ]\n')
	iniContents.append('COORDINATES = {}\n'.format(parent.coordinatesLB.text()))
	iniContents.append('LINEAR_UNITS = {}\n'.format(parent.linearUnitsCB.itemData(parent.linearUnitsCB.currentIndex())))
	iniContents.append('ANGULAR_UNITS = {}\n'.format(parent.angularUnitsCB.itemData(parent.angularUnitsCB.currentIndex())))
	iniContents.append('MAX_LINEAR_VELOCITY = {}\n'.format(parent.maxLinearVel.text()))

	# build the [HAL] section
	iniContents.append('\n[HAL]\n')
	iniContents.append('HALFILE = {}.hal\n'.format(parent.configNameUnderscored))
	iniContents.append('HALFILE = io.hal\n')
	iniContents.append('HALFILE = custom.hal\n')
	iniContents.append('POSTGUI_HALFILE = postgui.hal\n')
	if parent.haluiCB.isChecked():
		iniContents.append('HALUI = halui\n')

	# build the [HALUI] section
	iniContents.append('\n[HALUI]\n')

	# need to loop-a-fy this
	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'X':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_X]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'Y':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_Y]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'Z':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_Z]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'A':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_A]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'B':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_B]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'C':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_C]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'U':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_U]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'V':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_V]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	for item in parent.axisList:
		if getattr(parent,item).itemData(getattr(parent,item).currentIndex()) == 'W':
			jointTab = getattr(parent,item).objectName()[7]
			iniContents.append('\n[AXIS_W]\n')
			iniContents.append('MIN_LIMIT = {}\n'.format(getattr(parent, 'minLimit_' + jointTab).text()))
			iniContents.append('MAX_LIMIT = {}\n'.format(getattr(parent, 'maxLimit_' + jointTab).text()))
			iniContents.append('MAX_VELOCITY = {}\n'.format(getattr(parent, 'maxVelocity_' + jointTab).text()))
			iniContents.append('MAX_ACCELERATION = {}\n'.format(getattr(parent, 'maxAccel_' + jointTab).text()))
			break

	# need to loop-a-fy this section one day
	# build the [JOINT_0] section
	if parent.axisCB_0.itemData(parent.axisCB_0.currentIndex()):
		iniContents.append('\n[JOINT_0]\n')
		iniContents.append('AXIS = {}\n'.format(parent.axisCB_0.itemData(parent.axisCB_0.currentIndex())))
		iniContents.append('MIN_LIMIT = {}\n'.format(parent.minLimit_0.text()))
		iniContents.append('MAX_LIMIT = {}\n'.format(parent.maxLimit_0.text()))
		iniContents.append('MAX_VELOCITY = {}\n'.format(parent.maxVelocity_0.text()))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(parent.maxAccel_0.text()))
		iniContents.append('TYPE = {}\n'.format(parent.axisType_0.text()))
		iniContents.append('SCALE = {}\n'.format(parent.scale_0.text()))
		iniContents.append('STEPGEN_MAX_VEL = {}\n'.format(str(float(parent.maxVelocity_0.text()) * 1.2)))
		iniContents.append('STEPGEN_MAX_ACC = {}\n'.format(str(float(parent.maxAccel_0.text()) * 1.2)))
		if parent.units == 'inches':
			iniContents.append('FERROR = {}\n'.format('0.0002'))
			iniContents.append('MIN_FERROR = {}\n'.format('0.0001'))
		else:
			iniContents.append('FERROR = {}\n'.format('0.0051'))
			iniContents.append('MIN_FERROR = {}\n'.format('0.0025'))
		iniContents.append('DIRSETUP = {}\n'.format(parent.dirSetup_0.text()))
		iniContents.append('DIRHOLD = {}\n'.format(parent.dirHold_0.text()))
		iniContents.append('STEPLEN = {}\n'.format(parent.stepTime_0.text()))
		iniContents.append('STEPSPACE = {}\n'.format(parent.stepSpace_0.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_0.text()))
		iniContents.append('P = {}\n'.format(parent.p_0.text()))
		iniContents.append('I = {}\n'.format(parent.i_0.text()))
		iniContents.append('D = {}\n'.format(parent.d_0.text()))
		iniContents.append('FF0 = {}\n'.format(parent.ff0_0.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_0.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_0.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_0.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_0.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_0.text()))

		if parent.home_0.text():
			iniContents.append('HOME = {}\n'.format(parent.home_0.text()))
		if parent.homeOffset_0.text():
			iniContents.append('HOME_OFFSET = {}\n'.format(parent.homeOffset_0.text()))
		if parent.homeSearchVel_0.text():
			iniContents.append('HOME_SEARCH_VEL = {}\n'.format(parent.homeSearchVel_0.text()))
		if parent.homeLatchVel_0.text():
			iniContents.append('HOME_LATCH_VEL = {}\n'.format(parent.homeLatchVel_0.text()))
		if parent.homeSequence_0.text():
			iniContents.append('HOME_SEQUENCE = {}\n'.format(parent.homeSequence_0.text()))
		iniContents.append('HOME_USE_INDEX = {}\n'.format(parent.homeUseIndex_0.isChecked()))
		iniContents.append('HOME_IGNORE_LIMITS = {}\n'.format(parent.homeIgnoreLimits_0.isChecked()))


	# build the [JOINT_1] section
	if parent.axisCB_1.itemData(parent.axisCB_1.currentIndex()):
		iniContents.append('\n[JOINT_1]\n')
		iniContents.append('AXIS = {}\n'.format(parent.axisCB_1.itemData(parent.axisCB_1.currentIndex())))
		iniContents.append('MIN_LIMIT = {}\n'.format(parent.minLimit_1.text()))
		iniContents.append('MAX_LIMIT = {}\n'.format(parent.maxLimit_1.text()))
		iniContents.append('MAX_VELOCITY = {}\n'.format(parent.maxVelocity_1.text()))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(parent.maxAccel_1.text()))
		iniContents.append('TYPE = {}\n'.format(parent.axisType_1.text()))
		iniContents.append('SCALE = {}\n'.format(parent.scale_1.text()))
		iniContents.append('STEPGEN_MAX_VEL = {}\n'.format(str(float(parent.maxVelocity_1.text()) * 1.2)))
		iniContents.append('STEPGEN_MAX_ACC = {}\n'.format(str(float(parent.maxAccel_1.text()) * 1.2)))
		if parent.units == 'inches':
			iniContents.append('FERROR = {}\n'.format('0.0002'))
			iniContents.append('MIN_FERROR = {}\n'.format('0.0001'))
		else:
			iniContents.append('FERROR = {}\n'.format('0.0051'))
			iniContents.append('MIN_FERROR = {}\n'.format('0.0025'))
		iniContents.append('DIRSETUP = {}\n'.format(parent.dirSetup_1.text()))
		iniContents.append('DIRHOLD = {}\n'.format(parent.dirHold_1.text()))
		iniContents.append('STEPLEN = {}\n'.format(parent.stepTime_1.text()))
		iniContents.append('STEPSPACE = {}\n'.format(parent.stepSpace_1.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_1.text()))
		iniContents.append('P = {}\n'.format(parent.p_1.text()))
		iniContents.append('I = {}\n'.format(parent.i_1.text()))
		iniContents.append('D = {}\n'.format(parent.d_1.text()))
		iniContents.append('FF0 = {}\n'.format(parent.ff0_1.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_1.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_1.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_1.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_1.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_1.text()))
		if parent.home_1.text():
			iniContents.append('HOME = {}\n'.format(parent.home_1.text()))
		if parent.homeOffset_1.text():
			iniContents.append('HOME_OFFSET = {}\n'.format(parent.homeOffset_1.text()))
		if parent.homeSearchVel_1.text():
			iniContents.append('HOME_SEARCH_VEL = {}\n'.format(parent.homeSearchVel_1.text()))
		if parent.homeLatchVel_1.text():
			iniContents.append('HOME_LATCH_VEL = {}\n'.format(parent.homeLatchVel_1.text()))
		if parent.homeSequence_1.text():
			iniContents.append('HOME_SEQUENCE = {}\n'.format(parent.homeSequence_1.text()))
		iniContents.append('HOME_USE_INDEX = {}\n'.format(parent.homeUseIndex_1.isChecked()))
		iniContents.append('HOME_IGNORE_LIMITS = {}\n'.format(parent.homeIgnoreLimits_1.isChecked()))

	# build the [JOINT_2] section
	if parent.axisCB_2.itemData(parent.axisCB_2.currentIndex()):
		iniContents.append('\n[JOINT_2]\n')
		iniContents.append('AXIS = {}\n'.format(parent.axisCB_2.itemData(parent.axisCB_2.currentIndex())))
		iniContents.append('MIN_LIMIT = {}\n'.format(parent.minLimit_2.text()))
		iniContents.append('MAX_LIMIT = {}\n'.format(parent.maxLimit_2.text()))
		iniContents.append('MAX_VELOCITY = {}\n'.format(parent.maxVelocity_2.text()))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(parent.maxAccel_2.text()))
		iniContents.append('TYPE = {}\n'.format(parent.axisType_2.text()))
		iniContents.append('SCALE = {}\n'.format(parent.scale_2.text()))
		iniContents.append('STEPGEN_MAX_VEL = {}\n'.format(str(float(parent.maxVelocity_2.text()) * 1.2)))
		iniContents.append('STEPGEN_MAX_ACC = {}\n'.format(str(float(parent.maxAccel_2.text()) * 1.2)))
		if parent.units == 'inches':
			iniContents.append('FERROR = {}\n'.format('0.0002'))
			iniContents.append('MIN_FERROR = {}\n'.format('0.0001'))
		else:
			iniContents.append('FERROR = {}\n'.format('0.0051'))
			iniContents.append('MIN_FERROR = {}\n'.format('0.0025'))
		iniContents.append('DIRSETUP = {}\n'.format(parent.dirSetup_2.text()))
		iniContents.append('DIRHOLD = {}\n'.format(parent.dirHold_2.text()))
		iniContents.append('STEPLEN = {}\n'.format(parent.stepTime_2.text()))
		iniContents.append('STEPSPACE = {}\n'.format(parent.stepSpace_2.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_2.text()))
		iniContents.append('P = {}\n'.format(parent.p_2.text()))
		iniContents.append('I = {}\n'.format(parent.i_2.text()))
		iniContents.append('D = {}\n'.format(parent.d_2.text()))
		iniContents.append('FF0 = {}\n'.format(parent.ff0_2.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_2.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_2.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_2.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_2.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_2.text()))
		if parent.home_2.text():
			iniContents.append('HOME = {}\n'.format(parent.home_2.text()))
		if parent.homeOffset_2.text():
			iniContents.append('HOME_OFFSET = {}\n'.format(parent.homeOffset_2.text()))
		if parent.homeSearchVel_2.text():
			iniContents.append('HOME_SEARCH_VEL = {}\n'.format(parent.homeSearchVel_2.text()))
		if parent.homeLatchVel_2.text():
			iniContents.append('HOME_LATCH_VEL = {}\n'.format(parent.homeLatchVel_2.text()))
		if parent.homeSequence_2.text():
			iniContents.append('HOME_SEQUENCE = {}\n'.format(parent.homeSequence_2.text()))
		iniContents.append('HOME_USE_INDEX = {}\n'.format(parent.homeUseIndex_2.isChecked()))
		iniContents.append('HOME_IGNORE_LIMITS = {}\n'.format(parent.homeIgnoreLimits_2.isChecked()))

	# build the [JOINT_3] section
	if parent.axisCB_3.itemData(parent.axisCB_3.currentIndex()):
		iniContents.append('\n[JOINT_3]\n')
		iniContents.append('AXIS = {}\n'.format(parent.axisCB_3.itemData(parent.axisCB_3.currentIndex())))
		iniContents.append('MIN_LIMIT = {}\n'.format(parent.minLimit_3.text()))
		iniContents.append('MAX_LIMIT = {}\n'.format(parent.maxLimit_3.text()))
		iniContents.append('MAX_VELOCITY = {}\n'.format(parent.maxVelocity_3.text()))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(parent.maxAccel_3.text()))
		iniContents.append('TYPE = {}\n'.format(parent.axisType_3.text()))
		iniContents.append('SCALE = {}\n'.format(parent.scale_3.text()))
		iniContents.append('STEPGEN_MAX_VEL = {}\n'.format(str(float(parent.maxVelocity_3.text()) * 1.2)))
		iniContents.append('STEPGEN_MAX_ACC = {}\n'.format(str(float(parent.maxAccel_3.text()) * 1.2)))
		if parent.units == 'inches':
			iniContents.append('FERROR = {}\n'.format('0.0002'))
			iniContents.append('MIN_FERROR = {}\n'.format('0.0001'))
		else:
			iniContents.append('FERROR = {}\n'.format('0.0051'))
			iniContents.append('MIN_FERROR = {}\n'.format('0.0025'))
		iniContents.append('DIRSETUP = {}\n'.format(parent.dirSetup_3.text()))
		iniContents.append('DIRHOLD = {}\n'.format(parent.dirHold_3.text()))
		iniContents.append('STEPLEN = {}\n'.format(parent.stepTime_3.text()))
		iniContents.append('STEPSPACE = {}\n'.format(parent.stepSpace_3.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_3.text()))
		iniContents.append('P = {}\n'.format(parent.p_3.text()))
		iniContents.append('I = {}\n'.format(parent.i_3.text()))
		iniContents.append('D = {}\n'.format(parent.d_3.text()))
		iniContents.append('FF0 = {}\n'.format(parent.ff0_3.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_3.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_3.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_3.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_3.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_3.text()))
		if parent.home_3.text():
			iniContents.append('HOME = {}\n'.format(parent.home_3.text()))
		if parent.homeOffset_3.text():
			iniContents.append('HOME_OFFSET = {}\n'.format(parent.homeOffset_3.text()))
		if parent.homeSearchVel_3.text():
			iniContents.append('HOME_SEARCH_VEL = {}\n'.format(parent.homeSearchVel_3.text()))
		if parent.homeLatchVel_3.text():
			iniContents.append('HOME_LATCH_VEL = {}\n'.format(parent.homeLatchVel_3.text()))
		if parent.homeSequence_3.text():
			iniContents.append('HOME_SEQUENCE = {}\n'.format(parent.homeSequence_3.text()))
		iniContents.append('HOME_USE_INDEX = {}\n'.format(parent.homeUseIndex_3.isChecked()))
		iniContents.append('HOME_IGNORE_LIMITS = {}\n'.format(parent.homeIgnoreLimits_3.isChecked()))

	# build the [JOINT_4] section
	if parent.axisCB_4.itemData(parent.axisCB_4.currentIndex()):
		iniContents.append('\n[JOINT_4]\n')
		iniContents.append('AXIS = {}\n'.format(parent.axisCB_4.itemData(parent.axisCB_4.currentIndex())))
		iniContents.append('MIN_LIMIT = {}\n'.format(parent.minLimit_4.text()))
		iniContents.append('MAX_LIMIT = {}\n'.format(parent.maxLimit_4.text()))
		iniContents.append('MAX_VELOCITY = {}\n'.format(parent.maxVelocity_4.text()))
		iniContents.append('MAX_ACCELERATION = {}\n'.format(parent.maxAccel_4.text()))
		iniContents.append('TYPE = {}\n'.format(parent.axisType_4.text()))
		iniContents.append('SCALE = {}\n'.format(parent.scale_4.text()))
		iniContents.append('STEPGEN_MAX_VEL = {}\n'.format(str(float(parent.maxVelocity_4.text()) * 1.2)))
		iniContents.append('STEPGEN_MAX_ACC = {}\n'.format(str(float(parent.maxAccel_4.text()) * 1.2)))
		if parent.units == 'inches':
			iniContents.append('FERROR = {}\n'.format('0.0002'))
			iniContents.append('MIN_FERROR = {}\n'.format('0.0001'))
		else:
			iniContents.append('FERROR = {}\n'.format('0.0051'))
			iniContents.append('MIN_FERROR = {}\n'.format('0.0025'))
		iniContents.append('DIRSETUP = {}\n'.format(parent.dirSetup_4.text()))
		iniContents.append('DIRHOLD = {}\n'.format(parent.dirHold_4.text()))
		iniContents.append('STEPLEN = {}\n'.format(parent.stepTime_4.text()))
		iniContents.append('STEPSPACE = {}\n'.format(parent.stepSpace_4.text()))
		iniContents.append('DEADBAND = {}\n'.format(parent.deadband_4.text()))
		iniContents.append('P = {}\n'.format(parent.p_4.text()))
		iniContents.append('I = {}\n'.format(parent.i_4.text()))
		iniContents.append('D = {}\n'.format(parent.d_4.text()))
		iniContents.append('FF0 = {}\n'.format(parent.ff0_4.text()))
		iniContents.append('FF1 = {}\n'.format(parent.ff1_4.text()))
		iniContents.append('FF2 = {}\n'.format(parent.ff2_4.text()))
		iniContents.append('BIAS = {}\n'.format(parent.bias_4.text()))
		iniContents.append('MAX_OUTPUT = {}\n'.format(parent.maxOutput_4.text()))
		iniContents.append('MAX_ERROR = {}\n'.format(parent.maxError_4.text()))
		if parent.home_4.text():
			iniContents.append('HOME = {}\n'.format(parent.home_4.text()))
		if parent.homeOffset_4.text():
			iniContents.append('HOME_OFFSET = {}\n'.format(parent.homeOffset_4.text()))
		if parent.homeSearchVel_4.text():
			iniContents.append('HOME_SEARCH_VEL = {}\n'.format(parent.homeSearchVel_4.text()))
		if parent.homeLatchVel_4.text():
			iniContents.append('HOME_LATCH_VEL = {}\n'.format(parent.homeLatchVel_4.text()))
		if parent.homeSequence_4.text():
			iniContents.append('HOME_SEQUENCE = {}\n'.format(parent.homeSequence_4.text()))
		iniContents.append('HOME_USE_INDEX = {}\n'.format(parent.homeUseIndex_4.isChecked()))
		iniContents.append('HOME_IGNORE_LIMITS = {}\n'.format(parent.homeIgnoreLimits_4.isChecked()))

	# build the [SPINDLE] section if enabled
	#print(parent.spindleTypeCB.currentText())
	if parent.spindleTypeCB.currentText() != 'Select':
		iniContents.append('\n[SPINDLE]\n')
		iniContents.append('SPINDLE_TYPE = {}\n'.format(parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex())))
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

	# build the [INPUTS] section
	iniContents.append('\n[INPUTS]\n')
	iniContents.append('# DO NOT change the input text\n')
	iniContents.append('INPUT_0 = {}\n'.format(parent.input_0.currentText()))
	iniContents.append('INPUT_JOINT_0 = {}\n'.format(parent.inputJoint_0.currentData()))
	iniContents.append('INPUT_1 = {}\n'.format(parent.input_1.currentText()))
	iniContents.append('INPUT_JOINT_1 = {}\n'.format(parent.inputJoint_1.currentData()))
	iniContents.append('INPUT_2 = {}\n'.format(parent.input_2.currentText()))
	iniContents.append('INPUT_JOINT_2 = {}\n'.format(parent.inputJoint_2.currentData()))
	iniContents.append('INPUT_3 = {}\n'.format(parent.input_3.currentText()))
	iniContents.append('INPUT_JOINT_3 = {}\n'.format(parent.inputJoint_3.currentData()))
	iniContents.append('INPUT_4 = {}\n'.format(parent.input_4.currentText()))
	iniContents.append('INPUT_JOINT_4 = {}\n'.format(parent.inputJoint_4.currentData()))
	iniContents.append('INPUT_5 = {}\n'.format(parent.input_5.currentText()))
	iniContents.append('INPUT_JOINT_5 = {}\n'.format(parent.inputJoint_5.currentData()))
	iniContents.append('INPUT_6 = {}\n'.format(parent.input_6.currentText()))
	iniContents.append('INPUT_JOINT_6 = {}\n'.format(parent.inputJoint_6.currentData()))
	iniContents.append('INPUT_7 = {}\n'.format(parent.input_7.currentText()))
	iniContents.append('INPUT_JOINT_7 = {}\n'.format(parent.inputJoint_7.currentData()))
	iniContents.append('INPUT_8 = {}\n'.format(parent.input_8.currentText()))
	iniContents.append('INPUT_JOINT_8 = {}\n'.format(parent.inputJoint_8.currentData()))
	iniContents.append('INPUT_9 = {}\n'.format(parent.input_9.currentText()))
	iniContents.append('INPUT_JOINT_9 = {}\n'.format(parent.inputJoint_9.currentData()))
	iniContents.append('INPUT_10 = {}\n'.format(parent.input_10.currentText()))
	iniContents.append('INPUT_JOINT_10 = {}\n'.format(parent.inputJoint_10.currentData()))


	# build the [OUTPUTS] section
	iniContents.append('\n[OUTPUTS]\n')
	iniContents.append('# DO NOT change the output text\n')
	iniContents.append('OUTPUT_0 = {}\n'.format(parent.output_0.currentText()))
	iniContents.append('OUTPUT_1 = {}\n'.format(parent.output_1.currentText()))
	iniContents.append('OUTPUT_2 = {}\n'.format(parent.output_2.currentText()))
	iniContents.append('OUTPUT_3 = {}\n'.format(parent.output_3.currentText()))
	iniContents.append('OUTPUT_4 = {}\n'.format(parent.output_4.currentText()))

	# build the [OPTIIONS] section
	iniContents.append('\n[OPTIONS]\n')
	iniContents.append('MANUAL_TOOL_CHANGE = {}\n'.format(parent.manualToolChangeCB.isChecked()))
	iniContents.append('HALUI = {}\n'.format(parent.haluiCB.isChecked()))
	iniContents.append('PYVCP = {}\n'.format(parent.pyvcpCB.isChecked()))
	iniContents.append('GLADEVCP = {}\n'.format(parent.gladevcpCB.isChecked()))
	iniContents.append('LADDER = {}\n'.format(parent.ladderGB.isChecked()))
	if parent.ladderGB.isChecked(): # check for any options
		for option in parent.ladderOptionsList:
			if getattr(parent, option).value() > 0: #******** work to be done here
				iniContents.append('{} = {}\n'.format(getattr(parent, option).property('item'), getattr(parent, option).value()))

	with open(iniFilePath, 'w') as iniFile:
		iniFile.writelines(iniContents)
	buildini.result = 'Sucess {} file was created'.format(iniFilePath)
	return True


def buildhal(parent):
	halFilePath = os.path.join(parent.configPath, parent.configNameUnderscored + '.hal')
	halContents = []
	halContents = ['# This file was created with the 7i96 Wizard on ']
	halContents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	halContents.append('# If you make changes to this file DO NOT run the configuration tool again!\n')
	halContents.append('# This file will be replaced with a new file if you do!\n\n')
	# build the standard header
	halContents.append('# kinematics\n')
	halContents.append('loadrt [KINS]KINEMATICS\n\n')
	halContents.append('# motion controller\n')
	halContents.append('loadrt [EMCMOT]EMCMOT ')
	halContents.append('servo_period_nsec=[EMCMOT]SERVO_PERIOD ')
	halContents.append('num_joints=[KINS]JOINTS\n\n')
	halContents.append('# standard components\n')
	halContents.append('loadrt pid num_chan={} \n\n'.format(len(parent.coordinatesLB.text())))
	halContents.append('# hostmot2 driver\n')
	halContents.append('loadrt hostmot2\n\n')
	halContents.append('loadrt [HOSTMOT2](DRIVER) ')
	halContents.append('board_ip=[HOSTMOT2](IPADDRESS) ')
	halContents.append('config="num_encoders=[HOSTMOT2](ENCODERS) ')
	halContents.append('num_stepgens=[HOSTMOT2](STEPGENS) ')
	halContents.append('sserial_port_0=[HOSTMOT2](SSERIAL_PORT)"\n')
	halContents.append('setp hm2_[HOSTMOT2](BOARD).0.watchdog.timeout_ns 25000000\n')
	halContents.append('\n# THREADS\n')
	halContents.append('addf hm2_[HOSTMOT2](BOARD).0.read servo-thread\n')
	halContents.append('addf motion-command-handler servo-thread\n')
	halContents.append('addf motion-controller servo-thread\n')
	halContents.append('setp hm2_[HOSTMOT2](BOARD).0.dpll.01.timer-us -100\n')
	halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.timer-number 1 \n')
	for index in range(len(parent.coordinatesLB.text())):
		halContents.append('addf pid.{}.do-pid-calcs servo-thread\n'.format(str(index)))
	halContents.append('addf hm2_[HOSTMOT2](BOARD).0.write servo-thread\n')
	for index in range(len(parent.coordinatesLB.text())):
		halContents.append('\n# Joint {0}\n'.format(str(index)))
		halContents.append('# axis enable chain\n')
		halContents.append('newsig emcmot.{0}.enable bit\n'.format(str(index)))
		halContents.append('sets emcmot.{0}.enable FALSE\n'.format(str(index)))
		halContents.append('net emcmot.{0}.enable <= joint.{0}.amp-enable-out\n'.format(str(index)))
		halContents.append('net emcmot.{0}.enable => hm2_[HOSTMOT2](BOARD).0.stepgen.0{0}.enable pid.{0}.enable\n\n'.format(str(index)))
		halContents.append('# position command and feedback\n')
		halContents.append('net emcmot.{0}.pos-cmd joint.{0}.motor-pos-cmd => pid.{0}.command\n'.format(str(index)))
		halContents.append('net motor.{0}.pos-fb <= hm2_[HOSTMOT2](BOARD).0.stepgen.0{0}.position-fb joint.{0}.motor-pos-fb pid.{0}.feedback\n'.format(str(index)))
		halContents.append('net motor.{0}.command pid.{0}.output hm2_[HOSTMOT2](BOARD).0.stepgen.0{0}.velocity-cmd\n'.format(str(index)))
		halContents.append('setp pid.{}.error-previous-target true\n\n'.format(str(index)))
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{0}.dirsetup [JOINT_{0}]DIRSETUP\n'.format(str(index)))
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{0}.dirhold [JOINT_{0}]DIRHOLD\n'.format(str(index)))
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{0}.steplen [JOINT_{0}]STEPLEN\n'.format(str(index)))
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{0}.stepspace [JOINT_{0}]STEPSPACE\n'.format(str(index)))
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{0}.position-scale [JOINT_{0}]SCALE\n'.format(str(index)))
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{0}.maxvel [JOINT_{0}]STEPGEN_MAX_VEL\n'.format(str(index)))
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{0}.maxaccel [JOINT_{0}]STEPGEN_MAX_ACC\n'.format(str(index)))
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{}.step_type 0\n'.format(str(index)))
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{}.control-type 1\n\n'.format(str(index)))

		halContents.append('setp pid.{0}.Pgain [JOINT_{0}]P\n'.format(str(index)))
		halContents.append('setp pid.{0}.Igain [JOINT_{0}]I\n'.format(str(index)))
		halContents.append('setp pid.{0}.Dgain [JOINT_{0}]D\n'.format(str(index)))
		halContents.append('setp pid.{0}.bias [JOINT_{0}]BIAS\n'.format(str(index)))
		halContents.append('setp pid.{0}.FF0 [JOINT_{0}]FF0\n'.format(str(index)))
		halContents.append('setp pid.{0}.FF1 [JOINT_{0}]FF1\n'.format(str(index)))
		halContents.append('setp pid.{0}.FF2 [JOINT_{0}]FF2\n'.format(str(index)))
		halContents.append('setp pid.{0}.deadband [JOINT_{0}]DEADBAND\n'.format(str(index)))
		halContents.append('setp pid.{0}.maxoutput [JOINT_{0}]MAX_OUTPUT\n'.format(str(index)))
		halContents.append('setp pid.{0}.maxerror [JOINT_{0}]MAX_ERROR\n'.format(str(index)))

	if parent.spindleTypeCB.currentText() != 'Select':
		halContents.append('\n# Spindle\n')
		halContents.append('setp hm2_7i96.0.pwmgen.00.output-type 0\n')
		halContents.append('setp hm2_7i96.0.pwmgen.00.scale [SPINDLE]MAX_RPM\n')
		halContents.append('setp hm2_7i96.0.pwmgen.pwm_frequency [SPINDLE]PWM_FREQUENCY\n')

	halContents.append('\n# Standard I/O Block - EStop, Etc\n')
	halContents.append('# create a signal for the estop loopback\n')
	halContents.append('net estop-loop iocontrol.0.user-enable-out => iocontrol.0.emc-enable-in\n')
	if parent.manualToolChangeCB.isChecked():
		halContents.append('\n# create signals for tool loading loopback\n')
		halContents.append('net tool-prep-loop iocontrol.0.tool-prepare => iocontrol.0.tool-prepared\n')
		halContents.append('net tool-change-loop iocontrol.0.tool-change => iocontrol.0.tool-changed\n')

	if parent.ladderGB.isChecked():
		halContents.append('\n# # Load Classicladder without GUI\n')
		# this line needs to be built from the options if any are above 0
		ladderOptions = []
		for option in parent.ladderOptionsList:
			if getattr(parent, option).value() > 0:
				ladderOptions.append(getattr(parent, option).property('option') + '=' + str(getattr(parent, option).value()))
		if ladderOptions:
				halContents.append('loadrt classicladder_rt {}\n'.format(' '.join(ladderOptions)))
		else:
			halContents.append('loadrt classicladder_rt\n')
		halContents.append('addf classicladder.0.refresh servo-thread 1\n')

	with open(halFilePath, 'w') as halFile:
		halFile.writelines(halContents)
	return True

"""
def buildio(parent):
	ioFilePath = os.path.join(parent.configPath, 'io.hal')
	ioContents = []
	ioContents = ['# This file was created with the 7i96 Wizard on ']
	ioContents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	ioContents.append('# If you make changes to this file your screwed\n\n')

	ioContents = ['\n']
	ioContents.append('\n')
	try:
		with open(ioFilePath, 'w') as toolFile:
			ioContents.writelines(toolContents)
	except FileExistsError:
		pass
	return True
"""

def buildmisc(parent):

	# if Axis is the GUI add the shutup file
	if parent.guiCB.currentData() == 'axis':
		shutupFilepath = os.path.expanduser('~/.axisrc')
		shutupContents = ['root_window.tk.call("wm","protocol",".","WM_DELETE_WINDOW","destroy .")']
		try: # if this file exists don't write over it
			with open(shutupFilepath, 'x') as shutupFile:
				shutupFile.writelines(shutupContents)
		except FileExistsError:
			pass


	customFilePath = os.path.join(parent.configPath, 'custom.hal')
	customContents = []
	customContents = ['# Place any HAL commands in this file that you want to run before the GUI.\n']
	customContents.append('# This file will not be written over by the configuration tool.\n')
	try: # if this file exists don't write over it
		with open(customFilePath, 'x') as customFile:
			customFile.writelines(customContents)
	except FileExistsError:
		pass

	# create the postgui.hal file if not there
	postguiFilePath = os.path.join(parent.configPath, 'postgui.hal')
	postguiContents = []
	postguiContents = ['# Place any HAL commands in this file that you want to run AFTER the GUI finishes loading.\n']
	postguiContents.append('# GUI HAL pins are not visible until after the GUI loads.\n')
	postguiContents.append('# This file will not be written over by the configuration tool.\n')
	try: # if this file exists don't write over it
		with open(postguiFilePath, 'x') as postguiFile:
			postguiFile.writelines(postguiContents)
	except FileExistsError:
		pass

	# create the tool file if not there
	toolFilePath = os.path.join(parent.configPath, 'tool.tbl')
	toolContents = []
	toolContents = [';\n']
	toolContents.append('T1 P1\n')
	try: # if this file exists don't write over it
		with open(toolFilePath, 'x') as toolFile:
			toolFile.writelines(toolContents)
	except FileExistsError:
		pass

	# create the var file if not there
	varFilePath = os.path.join(parent.configPath, parent.configNameUnderscored + '.var')
	try: #
		open(varFilePath, 'x')
	except FileExistsError:
		pass

	# create the pyvcp panel if checked and not there
	if parent.pyvcpCB.isChecked():
		pyvcpFilePath = os.path.join(parent.configPath, parent.configNameUnderscored + '.xml')
		pyvcpContents = ["<?xml version='1.0' encoding='UTF-8'?>\n"]
		pyvcpContents.append('<pyvcp>\n')
		pyvcpContents.append('<!--\n')
		pyvcpContents.append('Build your PyVCP panel between the <pyvcp></pyvcp> tags.\n')
		pyvcpContents.append('Make sure your outside the comment tags.\n')
		pyvcpContents.append('The contents of this file will not be overwritten\n')
		pyvcpContents.append('when you run this wizard again.\n')
		pyvcpContents.append('-->\n')
		pyvcpContents.append('	<label>\n')
		pyvcpContents.append('		<text>"This is a Sample Label:"</text>\n')
		pyvcpContents.append('		<font>("Helvetica",10)</font>\n')
		pyvcpContents.append('	</label>\n')
		pyvcpContents.append('</pyvcp>\n')
		try: # if this file exists don't write over it
			with open(pyvcpFilePath, 'x') as pyvcpFile:
				pyvcpFile.writelines(pyvcpContents)
		except FileExistsError:
			pass

	# create the clp file if selected
	if parent.ladderGB.isChecked():
		ladderFilePath = os.path.join(parent.configPath, parent.configNameUnderscored + '.clp')
		ladderContents = """_FILES_CLASSICLADDER
_FILE-symbols.csv
#VER=1.0
_/FILE-symbols.csv
_FILE-modbusioconf.csv
#VER=1.0
_/FILE-modbusioconf.csv
_FILE-com_params.txt
MODBUS_MASTER_SERIAL_PORT=
MODBUS_MASTER_SERIAL_SPEED=9600
MODBUS_ELEMENT_OFFSET=0
MODBUS_MASTER_SERIAL_USE_RTS_TO_SEND=0
MODBUS_MASTER_TIME_INTER_FRAME=100
MODBUS_MASTER_TIME_OUT_RECEIPT=500
MODBUS_MASTER_TIME_AFTER_TRANSMIT=0
MODBUS_DEBUG_LEVEL=0
MODBUS_MAP_COIL_READ=0
MODBUS_MAP_COIL_WRITE=0
MODBUS_MAP_INPUT=0
MODBUS_MAP_HOLDING=0
MODBUS_MAP_REGISTER_READ=0
MODBUS_MAP_REGISTER_WRITE=0
_/FILE-com_params.txt
_FILE-timers_iec.csv
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
1,0,0
_/FILE-timers_iec.csv
_FILE-timers.csv
1,0
1,0
1,0
1,0
1,0
1,0
1,0
1,0
1,0
1,0
_/FILE-timers.csv
_FILE-counters.csv
0
0
0
0
0
0
0
0
0
0
_/FILE-counters.csv
_FILE-sections.csv
#VER=1.0
#NAME000=Prog1
000,0,-1,0,0,0
_/FILE-sections.csv
_FILE-arithmetic_expressions.csv
#VER=2.0
_/FILE-arithmetic_expressions.csv
_FILE-rung_0.csv
#VER=2.0
#LABEL=
#COMMENT=
#PREVRUNG=0
#NEXTRUNG=0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0 , 0-0-0/0
_/FILE-rung_0.csv
_FILE-ioconf.csv
#VER=1.0
_/FILE-ioconf.csv
_FILE-monostables.csv
1,0
1,0
1,0
1,0
1,0
1,0
1,0
1,0
1,0
1,0
_/FILE-monostables.csv
_FILE-sequential.csv
#VER=1.0
_/FILE-sequential.csv
_FILE-general.txt
PERIODIC_REFRESH=50
SIZE_NBR_RUNGS=100
SIZE_NBR_BITS=500
SIZE_NBR_WORDS=100
SIZE_NBR_TIMERS=10
SIZE_NBR_MONOSTABLES=10
SIZE_NBR_COUNTERS=10
SIZE_NBR_TIMERS_IEC=10
SIZE_NBR_PHYS_INPUTS=15
SIZE_NBR_PHYS_OUTPUTS=15
SIZE_NBR_ARITHM_EXPR=100
SIZE_NBR_SECTIONS=10
SIZE_NBR_SYMBOLS=100
_/FILE-general.txt
_/FILES_CLASSICLADDER
"""

		try: # if this file exists don't write over it
			with open(ladderFilePath, 'x') as ladderFile:
				ladderFile.writelines(ladderContents)
		except FileExistsError:
			pass
	return True

def buildio(parent):
	ioFilePath = os.path.join(parent.configPath, 'io.hal')
	ioContents = []
	ioContents = ['# This file was created with the 7i96 Wizard on ']
	ioContents.append(datetime.now().strftime('%b %d %Y %H:%M:%S') + '\n')
	ioContents.append('# If you make changes to this file your screwed\n\n')

	# build the inputs
	for index in range(11):
		inputText = getattr(parent, 'input_' + str(index)).currentText()
		inputJoint = getattr(parent, 'inputJoint_' + str(index)).currentData()
		if inputText == 'Home':
			ioContents.append('net home-joint-{0} joint.{0}.home-sw-in <= hm2_7i96.0.gpio.0{1:02}.in\n'.format(inputJoint, index))
		elif inputText == 'Both Limit':
			ioContents.append('net limits-joint-{0} joint.{0}.neg-lim-sw-in <= hm2_7i96.0.gpio.0{1:02}.in\n'.format(inputJoint, index))
			ioContents.append('net limits-joint-{0} joint.{0}.pos-lim-sw-in\n'.format(inputJoint))
		elif inputText == 'Min Limit':
			ioContents.append('net min-limit-joint-{0} joint.{0}.neg-lim-sw-in <= hm2_7i96.0.gpio.0{1:02}.in\n'.format(inputJoint, index))
		elif inputText == 'Max Limit':
			ioContents.append('net max-limit-joint-{0} joint.{0}.pos-lim-sw-in <= hm2_7i96.0.gpio.0{1:02}.in\n'.format(inputJoint, index))
		elif inputText == 'Home & Limit':
			ioContents.append('net home-limit-joint-{0} joint.{0}.home-sw-in <= hm2_7i96.0.gpio.0{1:02}.in\n'.format(inputJoint, index))
			ioContents.append('net home-limit-joint-{0} joint.{0}.neg-lim-sw-in\n'.format(inputJoint))
			ioContents.append('net home-limit-joint-{0} joint.{0}.pos-lim-sw-in\n'.format(inputJoint))
		elif inputText == 'Min Limit & Home':
			ioContents.append('net min-limit-home-joint-{0} joint.{0}.neg-lim-sw-in <= hm2_7i96.0.gpio.0{1:02}.in\n'.format(inputJoint, index))
			ioContents.append('net min-limit-home-joint-{0} joint.{0}.home-sw-in\n'.format(inputJoint))
		elif inputText == 'Max Limit & Home':
			ioContents.append('net max-limit-home-joint-{0} joint.{0}.pos-lim-sw-in <= hm2_7i96.0.gpio.0{1:02}.in\n'.format(inputJoint, index))
			ioContents.append('net max-limit-home-joint-{0} joint.{0}.home-sw-in\n'.format(inputJoint))
		elif inputText == 'Probe':
			ioContents.append('net probe-input motion.probe-input <= hm2_7i96.0.gpio.0{:02}.in\n'.format(index))
		elif inputText == 'Digital In 0':
			ioContents.append('net digital-input-0 motion.digital-in-00 <= hm2_7i96.0.gpio.0{:02}.in\n'.format(index))
		elif inputText == 'Digital In 1':
			ioContents.append('net digital-input-1 motion.digital-in-01 <= hm2_7i96.0.gpio.0{:02}.in\n'.format(index))
		elif inputText == 'Digital In 2':
			ioContents.append('net digital-input-2 motion.digital-in-02 <= hm2_7i96.0.gpio.0{:02}.in\n'.format(index))
		elif inputText == 'Digital In 3':
			ioContents.append('net digital-input-3 motion.digital-in-03 <= hm2_7i96.0.gpio.0{:02}.in\n'.format(index))

	# build the outputs
	for index in range(5):
		outputText = getattr(parent, 'output_' + str(index)).currentText()
		if outputText == 'Coolant Flood':
			ioContents.append('net flood-output iocontrol.0.coolant-flood => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Coolant Mist':
			ioContents.append('net mist-output iocontrol.0.coolant-mist => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Spindle On':
			ioContents.append('net spindle-on spindle.0.on => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Spindle CW':
			ioContents.append('net spindle-cw spindle.0.forward => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Spindle CCW':
			ioContents.append('net spindle-ccw spindle.0.reverse => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Spindle Brake':
			ioContents.append('net spindle-brake spindle.0.brake => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'E-Stop Out':
			ioContents.append('net estop-loop hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Digital Out 0':
			ioContents.append('net digital-out-0 motion.digital-out-00 => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Digital Out 1':
			ioContents.append('net digital-out-2 motion.digital-out-01 => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Digital Out 2':
			ioContents.append('net digital-out-2 motion.digital-out-02 => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))
		if outputText == 'Digital Out 3':
			ioContents.append('net digital-out-3 motion.digital-out-03 => hm2_7i96.0.ssr.00.out-0{}\n'.format(index))

	with open(ioFilePath, 'w') as ioFile:
		ioFile.writelines(ioContents)
	return True


