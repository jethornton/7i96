import os
from datetime import datetime

def build(parent):
	for i in range(11):
		inputText = getattr(parent, 'inputPB_' + str(i)).text()
		if inputText ==  'E-Stop':
			external_estop = True
			break
		else:
			external_estop = False
	halFilePath = os.path.join(parent.configPath, parent.configNameUnderscored + '.hal')
	parent.outputPTE.appendPlainText(f'Building {halFilePath}')

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
	halContents.append('num_pwmgens=[HOSTMOT2](PWMS) ')
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

	if parent.spindleTypeCB.itemData(parent.spindleTypeCB.currentIndex()):
		halContents.append('\n# Spindle\n')
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.pwmgen.00.output-type [SPINDLE]OUTPUT_TYPE\n')
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.pwmgen.00.scale [SPINDLE]MAX_RPM\n')
		halContents.append('setp hm2_[HOSTMOT2](BOARD).0.pwmgen.pwm_frequency [SPINDLE]PWM_FREQUENCY\n')
		halContents.append('net spindle-on spindle.0.on => hm2_[HOSTMOT2](BOARD).0.pwmgen.00.enable\n')
		halContents.append('net spindle-speed spindle.0.speed-out => hm2_[HOSTMOT2](BOARD).0.pwmgen.00.value\n')

	halContents.append('\n# Standard I/O Block - EStop, Etc\n')
	halContents.append('# create a signal for the estop loopback\n')
	for index in range(11):
		inputText = getattr(parent, 'input_' + str(index)).currentText()

	if external_estop:
		halContents.append('loadrt estop_latch\n')
		halContents.append('addf estop-latch.0 servo-thread\n')
	else:
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

	try:
		with open(halFilePath, 'w') as halFile:
			halFile.writelines(halContents)
	except OSError:
		parent.outputPTE.appendPlainText(f'OS error\n {traceback.print_exc()}')
