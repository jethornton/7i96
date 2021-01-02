from PyQt5 import QtWidgets

def config(parent):
	configErrors = []
	qclip = QtWidgets.QApplication.clipboard()
	tabError = False
	nextHeader = 0

	# check the Machine Tab for errors
	if not parent.configName.text():
		tabError = True
		configErrors.append('\tA configuration name must be entered')
	if not parent.versionLE.text():
		tabError = True
		configErrors.append('\tA version must be entered, use 1.1')
	if parent.linearUnitsCB.currentText() == 'Select':
		tabError = True
		configErrors.append('\tLinear Units must be selected')
	if not parent.maxLinearVel.text():
		tabError = True
		configErrors.append('\tMaximum Linear Velocity must be set')
	if parent.ipAddressCB.currentText() == 'Select':
		tabError = True
		configErrors.append('\tAn IP address must be selected, 10.10.10.10 is recommended')

	if tabError:
		configErrors.insert(nextHeader, 'Machine Tab:')
		nextHeader = len(configErrors)
		tabError = False
	# end of Machine Tab

	# check the Display Tab for errors
	if parent.guiCB.currentText() == 'Select':
		tabError = True
		configErrors.append('\tA GUI must be selected')
	if parent.positionOffsetCB.currentText() == 'Select':
		tabError = True
		configErrors.append('\tA Position Offset must be selected')
	if parent.positionFeedbackCB.currentText() == 'Select':
		tabError = True
		configErrors.append('\tA Position Feedback must be selected')
	if parent.maxFeedOverrideSB.value() == 0.0:
		tabError = True
		configErrors.append('\tThe Max Feed Override must be greater than zero, 1.2 is suggested')
	if parent.frontToolLatheCB.isChecked() and parent.backToolLatheCB.isChecked():
		configErrors.append('\tOnly one lathe display option can be checked')
		tabError = True
	if tabError:
		configErrors.insert(nextHeader, 'Display Tab:')
		nextHeader = len(configErrors)
		tabError = False
	# end of Display Tab

	# check the Axis Tab for errors
	if len(parent.coordinatesLB.text()) == 0:
		tabError = True
		configErrors.append('\tAt least one Joint must be configured starting with Joint 0')
	else: #check the joints
		# make this a loop getattr(parent, '_' + str(index))
		for index in range(5):
			if getattr(parent, 'axisCB_' + str(index)).currentText() != 'Select':
				if not getattr(parent, 'scale_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe Scale must be specified for Joint {}'.format(index))
				if not getattr(parent, 'minLimit_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for Mininum Limit Joint {} must be specified'.format(index))
				if not getattr(parent, 'maxLimit_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe Maximum Limit for Joint {} must be specified'.format(index))
				if not getattr(parent, 'maxVelocity_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for Maximum Velocity for Joint {} must be specified'.format(index))
				if not getattr(parent, 'maxAccel_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for Maximum Acceleration for Joint {} must be specified'.format(index))
				if not getattr(parent, 'p_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for P for Joint {} must be specified'.format(index))
				if not getattr(parent, 'i_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for I for Joint {} must be specified'.format(index))
				if not getattr(parent, 'd_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for D for Joint {} must be specified'.format(index))
				if not getattr(parent, 'ff0_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for FF0 for Joint {} must be specified'.format(index))
				if not getattr(parent, 'ff1_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for FF1 for Joint {} must be specified'.format(index))
				if not getattr(parent, 'ff2_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for FF2 for Joint {} must be specified'.format(index))
				if not getattr(parent, 'stepTime_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for Step Time for Joint {} must be specified'.format(index))
				if not getattr(parent, 'stepSpace_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for Step Space for Joint {} must be specified'.format(index))
				if not getattr(parent, 'dirSetup_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for Direction Setup for Joint {} must be specified'.format(index))
				if not getattr(parent, 'dirHold_' + str(index)).text():
					tabError = True
					configErrors.append('\tThe for Direction Hold for Joint {} must be specified'.format(index))
				# add sanity check for home entries
				if getattr(parent, 'home_' + str(index)).text():
					if not isNumber(getattr(parent, 'home_' + str(index)).text()):
						tabError = True
						configErrors.append('\tThe for Home Location for Joint {} must be a number'.format(index))
				if getattr(parent, 'homeOffset_' + str(index)).text():
					if not isNumber(getattr(parent, 'homeOffset_' + str(index)).text()):
						tabError = True
						configErrors.append('\tThe for Home Offset for Joint {} must be a number'.format(index))
				if getattr(parent, 'homeSearchVel_' + str(index)).text():
					if not isNumber(getattr(parent, 'homeSearchVel_' + str(index)).text()):
						tabError = True
						configErrors.append('\tThe for Home Search Velocity for Joint {} must be a number'.format(index))
				if getattr(parent, 'homeLatchVel_' + str(index)).text():
					if not isNumber(getattr(parent, 'homeLatchVel_' + str(index)).text()):
						tabError = True
						configErrors.append('\tThe for Home Latch Velocity for Joint {} must be a number'.format(index))
				if getattr(parent, 'homeSequence_' + str(index)).text():
					if not isNumber(getattr(parent, 'homeSequence_' + str(index)).text()):
						tabError = True
						configErrors.append('\tThe for Home Sequence for Joint {} must be a number'.format(index))


	if tabError:
		configErrors.insert(nextHeader, 'Axis Tab:')
		nextHeader = len(configErrors)
		tabError = False
	# end of Axis Tab

	if configErrors:
		config.result = '\n'.join(configErrors)
		#print(config.result)
		qclip.setText(config.result)
		return False
	else:
		config.result = 'Configuration checked OK'
		return True

def isNumber(x):
	try:
		float(x)
		return True
	except ValueError:
		return False
