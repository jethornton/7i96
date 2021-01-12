import os, sys, subprocess
from PyQt5.QtWidgets import QInputDialog, QLineEdit

def readCard(parent):
	if not parent.ipAddressCB.currentData():
		parent.outputLB.setText('An IP address must be selected')
		return

	ipAddress = parent.ipAddressCB.currentText()
	command = f"mesaflash --device 7i96 --addr {ipAddress} --readhmid"

	result = subprocess.getstatusoutput(command)
	if result[0] == 0:
		parent.outputLB.setText(result[1])
	else:
		readError = ("An error occoured trying to read the card\n"
								"Make sure the card is powered up\n"
								"Check address jumpers W5 down and W6 up.\n"
								"Reseat the Lan cable")
		parent.outputLB.setText(readError)

def flashCard(parent):
	if not parent.firmwareCB.currentData():
		parent.outputLB.setText('A firmware must be selected')
		return

	if not parent.ipAddressCB.currentData():
		parent.outputLB.setText('An IP address must be selected')
		return

	parent.outputLB.setText('Flashing the 7i96...')
	ipAddress = parent.ipAddressCB.currentText()
	firmware = os.path.join(os.path.dirname(__file__), parent.firmwareCB.currentData())
	command = f"mesaflash --device 7i96 --addr {ipAddress} --write {firmware}"
	result = subprocess.getstatusoutput(command)
	if result[0] == 0:
		parent.outputLB.setText(result[1])
	else:
		readError = ("An error occoured trying to read the card\n"
								"Make sure the card is powered up\n"
								"Check address jumpers W5 down and W6 up.\n"
								"Reseat the Lan cable")
		parent.outputLB.setText(readError)

def reloadCard(parent):
	if not parent.ipAddressCB.currentData():
		parent.outputLB.setText('An IP address must be selected')
		return

	ipAddress = parent.ipAddressCB.currentText()
	command = f"mesaflash --device 7i96 --addr {ipAddress} --reload"

	result = subprocess.getstatusoutput(command)
	if result[0] == 0:
		parent.outputLB.setText("Reload Sucessfull")
	else:
		readError = ("An error occoured trying to read the card\n"
								"Make sure the card is powered up\n"
								"Check address jumpers W5 down and W6 up.\n"
								"Reseat the Lan cable")
		parent.outputLB.setText(readError)

def cpuInfo(parent):
	command = "lscpu"
	result = subprocess.getstatusoutput(command)
	if result[0] == 0:
		parent.infoLB.setText(result[1])
	else:
		readError = ("An error occoured trying to read the cpu info")
		parent.infoLB.setText(readError)

def nicInfo(parent):
	command = "lspci"
	result = subprocess.getstatusoutput(command)
	if result[0] == 0:
		parent.infoLB.setText(result[1])
	else:
		readError = ("An error occoured trying to read the pci bus")
		parent.infoLB.setText(readError)

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
	command = "halcmd show param hm2*.tmax"
	result = subprocess.getstatusoutput(command)
	if result[0] == 0:
		parent.tMaxLB.setText(result[1])
	else:
		readError = ("An error occoured trying to read the pci bus")
		parent.tMaxLB.setText(readError)

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

