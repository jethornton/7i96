def iniList():
	# Section, Item, Object Name
	iniList = []
	iniList.append(['EMC', 'VERSION', 'versionLE'])
	iniList.append(['EMC', 'MACHINE', 'configName'])
	iniList.append(['EMC', 'DEBUG', 'debugCombo'])

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

	"""
	iniList.append(['INPUTS', 'INPUT_0', 'input_0'])
	iniList.append(['INPUTS', 'INPUT_1', 'input_1'])
	iniList.append(['INPUTS', 'INPUT_2', 'input_2'])
	iniList.append(['INPUTS', 'INPUT_3', 'input_3'])
	iniList.append(['INPUTS', 'INPUT_4', 'input_4'])
	iniList.append(['INPUTS', 'INPUT_5', 'input_5'])
	iniList.append(['INPUTS', 'INPUT_6', 'input_6'])
	iniList.append(['INPUTS', 'INPUT_7', 'input_7'])
	iniList.append(['INPUTS', 'INPUT_8', 'input_8'])
	iniList.append(['INPUTS', 'INPUT_9', 'input_9'])
	iniList.append(['INPUTS', 'INPUT_10', 'input_10'])

	iniList.append(['INPUTS', 'INPUT_DIR_0', 'inputInvert_0'])
	iniList.append(['INPUTS', 'INPUT_DIR_1', 'inputInvert_1'])
	iniList.append(['INPUTS', 'INPUT_DIR_2', 'inputInvert_2'])
	iniList.append(['INPUTS', 'INPUT_DIR_3', 'inputInvert_3'])
	iniList.append(['INPUTS', 'INPUT_DIR_4', 'inputInvert_4'])
	iniList.append(['INPUTS', 'INPUT_DIR_5', 'inputInvert_5'])
	iniList.append(['INPUTS', 'INPUT_DIR_6', 'inputInvert_6'])
	iniList.append(['INPUTS', 'INPUT_DIR_7', 'inputInvert_7'])
	iniList.append(['INPUTS', 'INPUT_DIR_8', 'inputInvert_8'])
	iniList.append(['INPUTS', 'INPUT_DIR_9', 'inputInvert_9'])
	iniList.append(['INPUTS', 'INPUT_DIR_10', 'inputInvert_10'])


	iniList.append(['INPUTS', 'INPUT_JOINT_0', 'inputJoint_0'])
	iniList.append(['INPUTS', 'INPUT_JOINT_1', 'inputJoint_1'])
	iniList.append(['INPUTS', 'INPUT_JOINT_2', 'inputJoint_2'])
	iniList.append(['INPUTS', 'INPUT_JOINT_3', 'inputJoint_3'])
	iniList.append(['INPUTS', 'INPUT_JOINT_4', 'inputJoint_4'])
	iniList.append(['INPUTS', 'INPUT_JOINT_5', 'inputJoint_5'])
	iniList.append(['INPUTS', 'INPUT_JOINT_6', 'inputJoint_6'])
	iniList.append(['INPUTS', 'INPUT_JOINT_7', 'inputJoint_7'])
	iniList.append(['INPUTS', 'INPUT_JOINT_8', 'inputJoint_8'])
	iniList.append(['INPUTS', 'INPUT_JOINT_9', 'inputJoint_9'])
	iniList.append(['INPUTS', 'INPUT_JOINT_10', 'inputJoint_10'])

	iniList.append(['OUTPUTS', 'OUTPUT_0', 'output_0'])
	iniList.append(['OUTPUTS', 'OUTPUT_1', 'output_1'])
	iniList.append(['OUTPUTS', 'OUTPUT_2', 'output_2'])
	iniList.append(['OUTPUTS', 'OUTPUT_3', 'output_3'])
	iniList.append(['OUTPUTS', 'OUTPUT_4', 'output_4'])
	"""
	iniList.append(['OPTIONS', 'INTRO_GRAPHIC', 'splashScreenCB'])
	iniList.append(['OPTIONS', 'MANUAL_TOOL_CHANGE', 'manualToolChangeCB'])
	iniList.append(['OPTIONS', 'HALUI', 'haluiCB'])
	iniList.append(['OPTIONS', 'PYVCP', 'pyvcpCB'])
	iniList.append(['OPTIONS', 'GLADEVCP', 'gladevcpCB'])
	iniList.append(['OPTIONS', 'LADDER', 'ladderGB'])
	iniList.append(['OPTIONS', 'LADDER_RUNGS', 'ladderRungsSB'])
	iniList.append(['BACKUP', 'BACKUP', 'backupCB'])

	return iniList

#iniList.append(['', '', ''])
