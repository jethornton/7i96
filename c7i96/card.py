import os, sys, subprocess, time
from PyQt5.QtWidgets import QInputDialog, QLineEdit

def check_ip(parent):
	if not parent.ipAddressCB.currentData():
		parent.errorMsgOk('An IP address must be selected', 'Error!')
		return False
	return True

def readCard(parent):
	if check_ip(parent):
		ipAddress = parent.ipAddressCB.currentText()
		arguments = ["--device", "7i96", "--addr", ipAddress, "--readhmid"]
		parent.extcmd.job(cmd="mesaflash", args=arguments, dest=parent.outputPTE)

def flashCard(parent):
	if check_ip(parent):
		if parent.firmwareCB.currentData():
			parent.statusbar.showMessage('Flashing the 7i96...')
			ipAddress = parent.ipAddressCB.currentText()
			firmware = os.path.join(os.path.dirname(__file__), parent.firmwareCB.currentData())
			arguments = ["--device", "7i96", "--addr", ipAddress, "--write", firmware]
			parent.extcmd.job(cmd="mesaflash", args=arguments, dest=parent.outputPTE)
		else:
			parent.errorMsgOk('A firmware must be selected', 'Error!')

def reloadCard(parent):
	if check_ip(parent):
		ipAddress = parent.ipAddressCB.currentText()
		arguments = ["--device", "7i96", "--addr", ipAddress, "--reload"]
		parent.extcmd.job(cmd="mesaflash", args=arguments, dest=parent.outputPTE)

def getCardPins(parent):
	if check_ip(parent):
		with open('temp.hal', 'w') as f:
			f.write('loadrt hostmot2\n')
			f.write(f'loadrt hm2_eth board_ip={parent.ipAddressCB.currentData()}\n')
			f.write('quit')
		arguments = ["-f", "temp.hal"]
		parent.extcmd.job(cmd="halrun", args=arguments, dest=parent.pinsPTE, clean='temp.hal')

def saveHalPins(parent):
	if parent.configName.text() == '':
		parent.errorMsgOk('A Configuration\nmust be loaded', 'Error')
		return
	if not "0x48414c32" in subprocess.getoutput('ipcs'):
		parent.errorMsgOk(f'LinuxCNC must be running\nthe {parent.configName.text()} configuration', 'Error')
		return
	parent.results = subprocess.getoutput("halcmd show pin")
	fp = os.path.join(parent.configPath, parent.configNameUnderscored + '-pins.txt')
	with open(fp, 'w') as f:
		f.writelines(parent.results)

def saveHalSigs(parent):
	if parent.configName.text() == '':
		parent.errorMsgOk('A Configuration\nmust be loaded', 'Error')
		return
	if not "0x48414c32" in subprocess.getoutput('ipcs'):
		parent.errorMsgOk(f'LinuxCNC must be running\nthe {parent.configName.text()} configuration', 'Error')
		return
	parent.results = subprocess.getoutput("halcmd show sig")
	fp = os.path.join(parent.configPath, parent.configNameUnderscored + '-sigs.txt')
	with open(fp, 'w') as f:
		f.writelines(parent.results)
