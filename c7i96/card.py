import os, sys, subprocess
from PyQt5.QtWidgets import QInputDialog, QLineEdit

def readCard(parent):

	result = subprocess.run([parent.mesaflash], stdout=subprocess.PIPE,\
	stderr=subprocess.PIPE, universal_newlines=True)
	#print(result.returncode)
	if result.returncode != 0:
		if result.stderr.find("`LIBPCI_3.5' not found"):
			parent.outputLB.setText('Library libpci-dev is not installed, install from\
a terminal with\nsudo apt-get install libpci-dev')
			return

	if parent.ipAddressCB.currentText() == 'None':
		parent.outputLB.setText('An IP address must be selected')
		return
	ipAddress = parent.ipAddressCB.currentText()
	command = [parent.mesaflash, "--device", "7i92", "--addr", ipAddress, "--readhmid"]

	try:
		output = subprocess.check_output(command, stderr=subprocess.PIPE)
		parent.outputLB.setText(output.decode(sys.getfilesystemencoding()))
		return output.decode(sys.getfilesystemencoding())
	except subprocess.CalledProcessError as e:
		print('exit code: {}'.format(e.returncode))
		print('stdout: {}'.format(e.output.decode(sys.getfilesystemencoding())))
		parent.outputLB.setText(e.output.decode(sys.getfilesystemencoding()))
		return e.output.decode(sys.getfilesystemencoding())

def flashCard(parent):
	if not parent.firmwareCB.currentData():
		parent.outputLB.setText('A firmware must be selected')
		return

	if not parent.ipAddressCB.currentData():
		parent.outputLB.setText('An IP address must be selected')
		return
	parent.statusbar.showMessage('Flashing the 7i92...')
	parent.outputLB.setText('')
	ipAddress = parent.ipAddressCB.currentText()
	firmware = os.path.join(os.path.dirname(__file__), parent.firmwareCB.currentData())
	command = [parent.mesaflash, '--device', '7i92', '--addr', ipAddress, '--write', firmware]
	output = []

	with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
		for line in proc.stdout:
			output.append(line.decode())
	print('flash done')
	parent.outputLB.setText(''.join(output))
	parent.statusbar.clearMessage()

def reloadCard(parent):
	if not parent.ipAddressCB.currentData():
		parent.outputLB.setText('An IP address must be selected')
		return

	ipAddress = parent.ipAddressCB.currentText()
	command = [parent.mesaflash, '--device', '7i92', '--addr', ipAddress, '--reload']
	output = []

	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	process.communicate()[0]
	if process.returncode == 0:
		parent.outputLB.setText('Reload Sucessful')
	elif process.returncode == 255:
		parent.outputLB.setText('No 7i92 board found')
	else:
		parent.outputLB.setText('Reload returned an error code of {}'.format(process.returncode))

def cpuInfo(parent):
	output = []
	with subprocess.Popen('lscpu', stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
		for line in proc.stdout:
			output.append(line.decode())
	parent.infoLB.setText(''.join(output))

def nicInfo(parent):
	# subprocess.check_output(('ps', '-A')) and then str.find on the output.
	ps = subprocess.Popen('lspci', stdout=subprocess.PIPE)
	output = subprocess.check_output(('grep', 'Ethernet'), stdin=ps.stdout)
	#print(type(output))
	parent.infoLB.setText(''.join(output.decode("utf-8")))

def nicCalc(parent):
	if parent.tMaxLE.text() != '' and parent.cpuSpeedLE.text() != '':
		tMax = int(int(parent.tMaxLE.text()) / 1000)
		cpuSpeed = float(parent.cpuSpeedLE.text()) * parent.speedCB.itemData(parent.speedCB.currentIndex())
		packetTime = tMax / cpuSpeed
		parent.packetTimeLB.setText('{:.1%}'.format(packetTime))
		threshold = (cpuSpeed * 0.7) / cpuSpeed
		parent.thresholdLB.setText('{:.0%}'.format(threshold))
	else:
		errorText = []
		if parent.cpuSpeedLE.text() == '':
			errorText.append('CPU Speed can not be empty')
		if parent.tMaxLE.text() == '':
			errorText.append('tMax can not be empty')
		parent.errorDialog('\n'.join(errorText))

def readTmax(parent):
	command = ['halcmd', 'show', 'param', 'hm2*.tmax']
	try:
		output = subprocess.check_output(command, stderr=subprocess.PIPE)
		parent.tMaxLB.setText(output.decode(sys.getfilesystemencoding()))
		#return output.decode(sys.getfilesystemencoding())
	except subprocess.CalledProcessError as e:
		#print('exit code: {}'.format(e.returncode))
		#print('stdout: {}'.format(e.output.decode(sys.getfilesystemencoding())))
		parent.tMaxLB.setText('LinuxCNC must be running to get tmax')
		#return e.output.decode(sys.getfilesystemencoding())

def pins(parent):
	if not parent.ipAddressCB.currentData():
		parent.pinsLB.setText('An IP address must be selected')
		return

	with open('temp.hal', 'w') as f:
		f.write('loadrt hostmot2\n')
		f.write('loadrt hm2_eth board_ip={}\n'.format(parent.ipAddressCB.currentData()))
		f.write('quit')

	command = ['halrun', '-f', 'temp.hal']
	output = []
	with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) as proc:
		for line in proc.stdout:
			output.append(line.decode())
	data = ''.join(output)
	if data.find('PWMGen'):
		parent.tb2p2LB.setText('PWM -')
		parent.tb2p3LB.setText('PWM +')
		parent.tb2p4LB.setText('Direction -')
		parent.tb2p5LB.setText('Direction +')
	parent.pinsLB.setText(data)

	os.remove('temp.hal')

