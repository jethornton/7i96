
def checkit(parent):
	parent.tabWidget.setCurrentIndex(0)
	configErrors = []
	tabError = False
	nextHeader = 0

	# check the Machine Tab for errors
	if not parent.configName.text():
		tabError = True
		configErrors.append('\tA configuration name must be entered')
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
		# make this a loop getattr(parent, f'_{i}')
		for i in range(parent.card['joints']):
			if getattr(parent, f'axisCB_{i}').currentText() != 'Select':
				if not getattr(parent, f'scale_{i}').text():
					tabError = True
					configErrors.append(f'\tThe Scale must be specified for Joint {i}')
				if not getattr(parent, f'minLimit_{i}').text():
					tabError = True
					configErrors.append(f'\tThe Mininum Limit for Joint {i} must be specified')
				if not getattr(parent, f'maxLimit_{i}').text():
					tabError = True
					configErrors.append(f'\tThe Maximum Limit for Joint {i} must be specified')
				if not getattr(parent, f'maxVelocity_{i}').text():
					tabError = True
					configErrors.append(f'\tThe Maximum Velocity for Joint {i} must be specified')
				if not getattr(parent, f'maxAccel_{i}').text():
					tabError = True
					configErrors.append(f'\tThe Maximum Acceleration for Joint {i} must be specified')
				if not getattr(parent, f'p_{i}').text():
					tabError = True
					configErrors.append(f'\tThe P for Joint {i} must be specified')
				if not getattr(parent, f'i_{i}').text():
					tabError = True
					configErrors.append(f'\tThe I for Joint {i} must be specified')
				if not getattr(parent, f'd_{i}').text():
					tabError = True
					configErrors.append(f'\tThe D for Joint {i} must be specified')
				if not getattr(parent, f'ff0_{i}').text():
					tabError = True
					configErrors.append(f'\tThe FF0 for Joint {i} must be specified')
				if not getattr(parent, f'ff1_{i}').text():
					tabError = True
					configErrors.append(f'\tThe FF1 for Joint {i} must be specified')
				if not getattr(parent, f'ff2_{i}').text():
					tabError = True
					configErrors.append(f'\tThe FF2 for Joint {i} must be specified')
				if not getattr(parent, f'stepTime_{i}').text():
					tabError = True
					configErrors.append(f'\tThe Step Time for Joint {i} must be specified')
				if not getattr(parent, f'stepSpace_{i}').text():
					tabError = True
					configErrors.append(f'\tThe Step Space for Joint {i} must be specified')
				if not getattr(parent, f'dirSetup_{i}').text():
					tabError = True
					configErrors.append(f'\tThe Direction Setup for Joint {i} must be specified')
				if not getattr(parent, f'dirHold_{i}').text():
					tabError = True
					configErrors.append(f'\tThe Direction Hold for Joint {i} must be specified')
				# add sanity check for home entries
				if getattr(parent, f'home_{i}').text():
					if not isNumber(getattr(parent, f'home_{i}').text()):
						tabError = True
						configErrors.append(f'\tThe Home Location for Joint {i} must be a number')
				if getattr(parent, f'homeOffset_{i}').text():
					if not isNumber(getattr(parent, f'homeOffset_{i}').text()):
						tabError = True
						configErrors.append(f'\tThe Home Offset for Joint {i} must be a number')
				if getattr(parent, f'homeSearchVel_{i}').text():
					if not isNumber(getattr(parent, f'homeSearchVel_{i}').text()):
						tabError = True
						configErrors.append(f'\tThe Home Search Velocity for Joint {i} must be a number')
				if getattr(parent, f'homeLatchVel_{i}').text():
					if not isNumber(getattr(parent, f'homeLatchVel_{i}').text()):
						tabError = True
						configErrors.append(f'\tThe Home Latch Velocity for Joint {i} must be a number')
				if getattr(parent, f'homeSequence_{i}').text():
					if not isNumber(getattr(parent, f'homeSequence_{i}').text()):
						tabError = True
						configErrors.append(f'\tThe Home Sequence for Joint {i} must be a number')

	if tabError:
		configErrors.insert(nextHeader, 'Axis Tab:')
		nextHeader = len(configErrors)
		tabError = False
	# end of Axis Tab

	parent.outputPTE.clear()
	if configErrors:
		checkit.result = '\n'.join(configErrors)
		parent.outputPTE.setPlainText(checkit.result)
		return False
	else:
		parent.outputPTE.setPlainText('Configuration checked OK')
		return True
	
def isNumber(x):
	try:
		float(x)
		return True
	except ValueError:
		return False
