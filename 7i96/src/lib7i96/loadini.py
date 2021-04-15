def iniList():
	# Section, Item, Object Name
	iniList = []
	iniList.append(['EMC', 'VERSION', 'versionLE'])
	iniList.append(['EMC', 'MACHINE', 'configName'])
	iniList.append(['EMC', 'DEBUG', 'debugCB'])

	iniList.append(['HOSTMOT2', 'DRIVER', 'driverCB'])
	iniList.append(['HOSTMOT2', 'IPADDRESS', 'ipAddressCB'])
	iniList.append(['HOSTMOT2', 'BOARD', 'boardCB'])
	iniList.append(['HOSTMOT2', 'STEPGENS', 'stepgensSB'])
	iniList.append(['HOSTMOT2', 'ENCODERS', 'encodersCB'])
	iniList.append(['HOSTMOT2', 'SSERIAL_PORT', 'sserialSB'])
	iniList.append(['HOSTMOT2', 'FIRMWARE', 'firmwareCB'])

	iniList.append(['DISPLAY', 'DISPLAY', 'guiCB'])
	iniList.append(['DISPLAY', 'POSITION_OFFSET', 'positionOffsetCB'])
	iniList.append(['DISPLAY', 'POSITION_FEEDBACK', 'positionFeedbackCB'])
	iniList.append(['DISPLAY', 'MAX_FEED_OVERRIDE', 'maxFeedOverrideSB'])
	iniList.append(['DISPLAY', 'INTRO_TIME', 'splashScreenSB'])

	iniList.append(['EMCMOT', 'SERVO_PERIOD', 'servoPeriodSB'])

	iniList.append(['TRAJ', 'LINEAR_UNITS', 'linearUnitsCB'])
	iniList.append(['TRAJ', 'COORDINATES', 'coordinatesLB'])
	iniList.append(['TRAJ', 'MAX_LINEAR_VELOCITY', 'maxLinearVel'])

	for i in range(5):
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

	iniList.append(['SPINDLE', 'OUTPUT_TYPE', 'spindleTypeCB'])
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

	for i in range(11):
		iniList.append(['INPUTS', f'INPUT_{i}', f'input_{i}'])

	for i in range(11):
		iniList.append(['INPUTS', f'INPUT_JOINT_{i}', f'inputJoint_{i}'])

	for i in range(11):
		iniList.append(['INPUTS', f'INPUT_DIR_{i}', f'inputInvert_{i}'])

	for i in range(6):
		iniList.append(['OUTPUTS', f'OUTPUT_{i}', f'output_{i}'])

	iniList.append(['OPTIONS', 'INTRO_GRAPHIC', 'splashScreenCB'])
	iniList.append(['OPTIONS', 'MANUAL_TOOL_CHANGE', 'manualToolChangeCB'])
	iniList.append(['OPTIONS', 'HALUI', 'haluiCB'])
	iniList.append(['OPTIONS', 'PYVCP', 'pyvcpCB'])
	iniList.append(['OPTIONS', 'GLADEVCP', 'gladevcpCB'])
	iniList.append(['OPTIONS', 'LADDER', 'ladderGB'])
	iniList.append(['OPTIONS', 'LADDER_RUNGS', 'ladderRungsSB'])
	iniList.append(['OPTIONS', 'BACKUP', 'backupCB'])

	iniList.append(['SSERIAL', 'SS_CARD', 'smartSerialCardCB'])


	return iniList

#iniList.append(['', '', ''])
