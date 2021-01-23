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
	if not parent.linearUnitsCB.currentData():
		tabError = True
		configErrors.append('\tLinear Units must be selected')
	if not parent.maxLinearVel.text():
		tabError = True
		configErrors.append('\tMaximum Linear Velocity must be set')
	if not parent.ipAddressCB.currentData():
		tabError = True
		configErrors.append('\tAn IP address must be selected, 10.10.10.10 is recommended')

	if tabError:
		configErrors.insert(nextHeader, 'Machine Tab:')
		nextHeader = len(configErrors)
		tabError = False
	# end of Machine Tab

	# check the Display Tab for errors
	if not parent.guiCB.currentData():
		tabError = True
		configErrors.append('\tA GUI must be selected')
	if not parent.positionOffsetCB.currentData():
		tabError = True
		configErrors.append('\tA Position Offset must be selected')
	if not parent.positionFeedbackCB.currentData():
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
			if getattr(parent, 'axisCB_' + str(index)).currentData():
				if not getattr(parent, 'scale_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe Scale must be specified for Joint {index}')
				if not getattr(parent, 'minLimit_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for Mininum Limit Joint {index} must be specified')
				if not getattr(parent, 'maxLimit_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe Maximum Limit for Joint {index} must be specified')
				if not getattr(parent, 'maxVelocity_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for Maximum Velocity for Joint {index} must be specified')
				if not getattr(parent, 'maxAccel_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for Maximum Acceleration for Joint {index} must be specified')
				if not getattr(parent, 'p_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for P for Joint {index} must be specified')
				if not getattr(parent, 'i_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for I for Joint {index} must be specified')
				if not getattr(parent, 'd_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for D for Joint {index} must be specified')
				if not getattr(parent, 'ff0_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for FF0 for Joint {index} must be specified')
				if not getattr(parent, 'ff1_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for FF1 for Joint {index} must be specified')
				if not getattr(parent, 'ff2_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for FF2 for Joint {index} must be specified')
				if not getattr(parent, 'stepTime_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for Step Time for Joint {index} must be specified')
				if not getattr(parent, 'stepSpace_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for Step Space for Joint {index} must be specified')
				if not getattr(parent, 'dirSetup_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for Direction Setup for Joint {index} must be specified')
				if not getattr(parent, 'dirHold_' + str(index)).text():
					tabError = True
					configErrors.append(f'\tThe for Direction Hold for Joint {index} must be specified')
				# add sanity check for home entries
				if getattr(parent, 'home_' + str(index)).text():
					if not isNumber(getattr(parent, 'home_' + str(index)).text()):
						tabError = True
						configErrors.append(f'\tThe for Home Location for Joint {index} must be a number')
				if getattr(parent, 'homeOffset_' + str(index)).text():
					if not isNumber(getattr(parent, 'homeOffset_' + str(index)).text()):
						tabError = True
						configErrors.append(f'\tThe for Home Offset for Joint {index} must be a number')
				if getattr(parent, 'homeSearchVel_' + str(index)).text():
					if not isNumber(getattr(parent, 'homeSearchVel_' + str(index)).text()):
						tabError = True
						configErrors.append(f'\tThe for Home Search Velocity for Joint {index} must be a number')
				if getattr(parent, 'homeLatchVel_' + str(index)).text():
					if not isNumber(getattr(parent, 'homeLatchVel_' + str(index)).text()):
						tabError = True
						configErrors.append(f'\tThe for Home Latch Velocity for Joint {index} must be a number')
				if getattr(parent, 'homeSequence_' + str(index)).text():
					if not isNumber(getattr(parent, 'homeSequence_' + str(index)).text()):
						tabError = True
						configErrors.append(f'\tThe for Home Sequence for Joint {index} must be a number')


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
