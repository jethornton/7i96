import os
from datetime import datetime

def build(parent):
	halFilePath = os.path.join(parent.configPath, parent.configNameUnderscored + '.hal')
	parent.outputPTE.appendPlainText(f'Building {halFilePath}')

	halContents = []
	halContents = ['# This file was created with the 7i95 Configuration Tool on ']
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
	halContents.append(f'loadrt pid num_chan={parent.axes} \n\n')
	halContents.append('# hostmot2 driver\n')
	halContents.append('loadrt hostmot2\n\n')
	halContents.append('loadrt [HOSTMOT2](DRIVER) ')
	halContents.append('board_ip=[HOSTMOT2](IPADDRESS) ')
	halContents.append('config="num_encoders=[HOSTMOT2](ENCODERS) ')
	halContents.append('num_stepgens=[HOSTMOT2](STEPGENS) ')
	halContents.append('num_pwmgens=[HOSTMOT2](PWMS) ')
	halContents.append('sserial_port_0=[HOSTMOT2](SSERIAL_PORT)"\n')
	halContents.append('setp hm2_[HOSTMOT2](BOARD).0.watchdog.timeout_ns 25000000\n')
	halContents.append('\n# THREADS\n')
	halContents.append('addf hm2_[HOSTMOT2](BOARD).0.read servo-thread\n')
	halContents.append('addf motion-command-handler servo-thread\n')
	halContents.append('addf motion-controller servo-thread\n')
	halContents.append('setp hm2_[HOSTMOT2](BOARD).0.dpll.01.timer-us -100\n')
	halContents.append('setp hm2_[HOSTMOT2](BOARD).0.stepgen.timer-number 1 \n')
	for i in range(len(parent.coordinatesLB.text())):
		halContents.append(f'addf pid.{i}.do-pid-calcs servo-thread\n')
	halContents.append('addf hm2_[HOSTMOT2](BOARD).0.write servo-thread\n')
	for i in range(parent.axes):
		halContents.append(f'\n# Joint {i}\n')
		halContents.append('# axis enable chain\n')
		halContents.append(f'newsig emcmot.{i}.enable bit\n')
		halContents.append(f'sets emcmot.{i}.enable FALSE\n')
		halContents.append(f'net emcmot.{i}.enable <= joint.{i}.amp-enable-out\n')
		halContents.append(f'net emcmot.{i}.enable => hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.enable pid.{i}.enable\n\n')
		halContents.append('# position command and feedback\n')
		halContents.append(f'net emcmot.{i}.pos-cmd joint.{i}.motor-pos-cmd => pid.{i}.command\n')
		halContents.append(f'net motor.{i}.pos-fb <= hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.position-fb joint.{i}.motor-pos-fb pid.{i}.feedback\n')
		halContents.append(f'net motor.{i}.command pid.{i}.output hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.velocity-cmd\n')
		halContents.append(f'setp pid.{i}.error-previous-target true\n\n')
		halContents.append(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.dirsetup [JOINT_{i}]DIRSETUP\n')
		halContents.append(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.dirhold [JOINT_{i}]DIRHOLD\n')
		halContents.append(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.steplen [JOINT_{i}]STEPLEN\n')
		halContents.append(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.stepspace [JOINT_{i}]STEPSPACE\n')
		halContents.append(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.position-scale [JOINT_{i}]SCALE\n')
		halContents.append(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.maxvel [JOINT_{i}]STEPGEN_MAX_VEL\n')
		halContents.append(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.maxaccel [JOINT_{i}]STEPGEN_MAX_ACC\n')
		halContents.append(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.step_type 0\n')
		halContents.append(f'setp hm2_[HOSTMOT2](BOARD).0.stepgen.0{i}.control-type 1\n\n')

		halContents.append(f'setp pid.{i}.Pgain [JOINT_{i}]P\n')
		halContents.append(f'setp pid.{i}.Igain [JOINT_{i}]I\n')
		halContents.append(f'setp pid.{i}.Dgain [JOINT_{i}]D\n')
		halContents.append(f'setp pid.{i}.bias [JOINT_{i}]BIAS\n')
		halContents.append(f'setp pid.{i}.FF0 [JOINT_{i}]FF0\n')
		halContents.append(f'setp pid.{i}.FF1 [JOINT_{i}]FF1\n')
		halContents.append(f'setp pid.{i}.FF2 [JOINT_{i}]FF2\n')
		halContents.append(f'setp pid.{i}.deadband [JOINT_{i}]DEADBAND\n')
		halContents.append(f'setp pid.{i}.maxoutput [JOINT_{i}]MAX_OUTPUT\n')
		halContents.append(f'setp pid.{i}.maxerror [JOINT_{i}]MAX_ERROR\n')

	if parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex()):
		halContents.append('\n# Spindle\n')
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.pwmgen.00.output-type [SPINDLE]OUTPUT_TYPE\n')
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.pwmgen.00.scale [SPINDLE]MAX_RPM\n')
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.pwmgen.pwm_frequency [SPINDLE]PWM_FREQUENCY\n')
		halContents.append('net spindle-on spindle.0.on => hm2_[HOSTMOT2](BOARD).0.pwmgen.00.enable\n')
		halContents.append('net spindle-speed spindle.0.speed-out => hm2_[HOSTMOT2](BOARD).0.pwmgen.00.value\n')

	halContents.append('\n# Standard I/O Block - EStop, Etc\n')
	halContents.append('# create a signal for the estop loopback\n')

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
				halContents.append(f'loadrt classicladder_rt {" ".join(ladderOptions)}\n')
		else:
			halContents.append('loadrt classicladder_rt\n')
		halContents.append('addf classicladder.0.refresh servo-thread 1\n')

	try:
		with open(halFilePath, 'w') as halFile:
			halFile.writelines(halContents)
	except OSError:
		parent.outputPTE.appendPlainText(f'OS error\n {traceback.print_exc()}')
