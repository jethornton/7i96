#!/usr/bin/env python3

import sys, os, configparser, platform, subprocess
from functools import partial
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt, QProcess
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QLineEdit, QSpinBox, QCheckBox, QComboBox, QLabel, QGroupBox, QDoubleSpinBox, QMessageBox, QInputDialog)

"""
# for local testing
import buildcombos
import loadini
import checkit
import buildfiles
import card
import pcinfo
#import extcmd
from extcmd import ext_cmd as extCmd
import helptext
from dialog import Ui_Dialog as errorDialog
from help import Ui_Dialog as helpDialog
from about import Ui_about as aboutDialog

"""
# for installed deb
import c7i96.buildcombos as buildcombos
import c7i96.loadini as loadini
import c7i96.checkit as checkit
import c7i96.buildfiles as buildfiles
import c7i96.card as card
import c7i96.pcinfo as pcinfo
from c7i96.extcmd import ext_cmd as extCmd
import c7i96.helptext as helptext
from c7i96.dialog import Ui_Dialog as errorDialog
from c7i96.help import Ui_Dialog as helpDialog
from c7i96.about import Ui_about as aboutDialog


UI_FILE = os.path.join(os.path.dirname(__file__), "c7i96.ui")

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		uic.loadUi(UI_FILE, self)
		self.version = '1.2.3'
		self.config = configparser.ConfigParser(strict=False)
		self.setWindowTitle('7i96 Configuration Tool Version {}'.format(self.version))
		self.configNameUnderscored = ''
		self.checkConfig = checkit.config
		self.builddirs = buildfiles.builddirs
		self.buildini = buildfiles.buildini
		self.buildhal = buildfiles.buildhal
		self.buildio = buildfiles.buildio
		self.buildmisc = buildfiles.buildmisc
		self.pcStats = platform.uname()
		self.qclip = QtWidgets.QApplication.clipboard()
		self.helpInfo = helptext.descriptions
		self.buildCB()
		self.setupConnections()
		self.axisList = ['axisCB_0', 'axisCB_1', 'axisCB_2', 'axisCB_3', 'axisCB_4']
		self.ladderOptionsList = ['ladderRungsSB', 'ladderBitsSB', 'ladderWordsSB',
			'ladderTimersSB', 'iecTimerSB', 'ladderMonostablesSB', 'ladderCountersSB',
			'ladderInputsSB', 'ladderOutputsSB', 'ladderExpresionsSB',
			'ladderSectionsSB', 'ladderSymbolsSB', 'ladderS32InputsSB',
			'ladderS32OuputsSB', 'ladderFloatInputsSB', 'ladderFloatOutputsSB']
		self.units = False
		self.extcmd = extCmd()
		self.results = ""

		self.checks()

		self.show()


	def checks(self):
		try:
			subprocess.run('mesaflash', check=True, capture_output=True)
		except FileNotFoundError:
			t = "Mesaflash not found go to\nhttps://github.com/LinuxCNC/mesaflash\nfor installation instructions."
			self.outputPTE.appendPlainText(t)
			self.testConnectionPB.setEnabled(False)
			self.flashPB.setEnabled(False)
			self.reloadPB.setEnabled(False)

	# Auto connected menu action callbacks
	@pyqtSlot()
	def on_actionFileNew_triggered(self):
		print('File New')

	@pyqtSlot()
	def on_actionOpen_triggered(self):
		if os.path.isdir(os.path.expanduser('~/linuxcnc/configs')):
			configsDir = os.path.expanduser('~/linuxcnc/configs')
		else:
			configsDir = os.path.expanduser('~/')
		fileName = QFileDialog.getOpenFileName(self,
		caption="Select Configuration INI File", directory=configsDir,
		filter='*.ini', options=QFileDialog.DontUseNativeDialog,)
		if fileName:
			iniFile = (fileName[0])
			if self.config.read(iniFile):
				self.iniLoad()

	@pyqtSlot()
	def on_actionSave_triggered(self):
		self.on_actionBuild_triggered()

	@pyqtSlot()
	def on_actionSavePins_triggered(self):
		card.saveHalPins(self)

	@pyqtSlot()
	def on_actionSaveSignals_triggered(self):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Information)
		msgBox.setWindowTitle("Save Configuration Signals")
		if self.configName.text() == '':
			msgBox.setText("A Configuration must be loaded!")
			msgBox.setStandardButtons(QMessageBox.Ok)
			returnValue = msgBox.exec()
			if returnValue == QMessageBox.Ok:
				return
		if "0x48414c32" in subprocess.getoutput('ipcs'):
			self.saveSigs()
		else:
			msgBox.setText("With your configuration\nrunning in Linuxcnc\npress OK")
			msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
			returnValue = msgBox.exec()
			if returnValue == QMessageBox.Ok:
				self.saveSigs()

	def savePins(self):
		fp = os.path.join(self.configPath, self.configNameUnderscored + '-pins.txt')
		with open(fp, 'w') as f:
			f.writelines(subprocess.getoutput("halcmd show pin"))

	def saveSigs(self):
		fp = os.path.join(self.configPath, self.configNameUnderscored + '-sigs.txt')
		with open(fp, 'w') as f:
			f.writelines(subprocess.getoutput("halcmd show sig"))

	@pyqtSlot()
	def on_actionAbout_triggered(self):
		dialog = QtWidgets.QDialog()
		dialog.ui = aboutDialog()
		dialog.ui.setupUi(dialog)
		dialog.ui.versionLB.setText('Version {}'.format(self.version))
		dialog.ui.systemLB.setText(self.pcStats.system)
		dialog.ui.releaseLB.setText('Kernel {}'.format(self.pcStats.release))
		dialog.ui.machineLB.setText('Processor {}'.format(self.pcStats.machine))
		if sys.maxsize > 2**32: # test for 64bit OS
			dialog.ui.bitsLB.setText('64 bit OS')
		else:
			dialog.ui.bitsLB.setText('32 bit OS')
		dialog.exec_()

	@pyqtSlot()
	def on_actionCheck_triggered(self):
		if self.checkConfig(self):
			QMessageBox.about(self, 'Configuration', '		Checked OK		')
		else:
			self.errorDialog(self.checkConfig.result)

	@pyqtSlot()
	def on_actionBuild_triggered(self):
		if not self.checkConfig(self):
			self.errorDialog(self.checkConfig.result)
			return

		result = self.builddirs(self)
		if result:
			result = self.buildini(self)
		else:
			self.statusbar.showMessage('Build Directories Failed')
			return
		if result:
			result = self.buildhal(self)
		else:
			self.statusbar.showMessage('Build INI File Failed')
			return
		if result:
			result = self.buildio(self)
		else:
			self.statusbar.showMessage('Build HAL Files Failed')
			return
		if result:
			result = self.buildmisc(self)
		else:
			self.statusbar.showMessage('Build I/O Files Failed')
			return
		if result:
			self.statusbar.showMessage('Build Files Completed')
		else:
			self.statusbar.showMessage('Build Misc Files Failed')

	@pyqtSlot()
	def on_actionSaveAs_triggered(self):
		text, ok = QInputDialog.getText(self, 'Input Dialog','Enter New Configuration Name:')
		self.configName.setText(text)
		self.on_actionBuild_triggered()

	@pyqtSlot()
	def on_actionExit_triggered(self):
		exit()

	@pyqtSlot()
	def on_actionTabHelp_triggered(self):
		self.help(self.tabWidget.currentIndex())

	@pyqtSlot()
	def on_actionBuildHelp_triggered(self):
		self.help(20)

	@pyqtSlot()
	def on_actionPCHelp_triggered(self):
		self.help(30)

	def setupConnections(self):
		self.configName.textChanged[str].connect(self.onConfigNameChanged)
		self.maxLinearVel.textChanged[str].connect(self.onMaxLinearVelChanged)
		self.boardsCB.currentIndexChanged.connect(self.boardsChanged)

		for i in range(5):
			getattr(self, 'axisCB_' + str(i)).currentIndexChanged.connect(self.onAxisChanged)
		for i in range(5):
			getattr(self, 'scale_' + str(i)).textChanged.connect(self.updateAxisInfo)
		for i in range(5):
			getattr(self, 'maxVelocity_' + str(i)).textChanged.connect(self.updateAxisInfo)
		for i in range(5):
			getattr(self, 'maxAccel_' + str(i)).textChanged.connect(self.updateAxisInfo)
		for i in range(5):
			getattr(self, 'pidDefault_' + str(i)).clicked.connect(self.pidSetDefault)
		for i in range(5):
			getattr(self, 'driveCB_' + str(i)).currentIndexChanged.connect(self.driveChanged)

		self.pidDefault_s.clicked.connect(self.pidSetDefault)
		self.copyPB.clicked.connect(self.copyOutput)
		self.copyInfoPB.clicked.connect(self.copyInfo)
		self.spindleTypeCB.currentIndexChanged.connect(self.spindleTypeChanged)
		self.linearUnitsCB.currentIndexChanged.connect(self.linearUnitsChanged)
		self.cpuPB.clicked.connect(partial(pcinfo.cpuInfo, self))
		self.nicPB.clicked.connect(partial(pcinfo.nicInfo, self))
		self.calcNicPB.clicked.connect(partial(pcinfo.nicCalc, self))
		self.readTmaxPB.clicked.connect(partial(pcinfo.readTmax, self))
		#     obj.signal.connect(partial(fun, args1, arg2, ... ))
		self.readCardPB.clicked.connect(partial(card.readCard, self))
		self.flashPB.clicked.connect(partial(card.flashCard, self))
		self.reloadPB.clicked.connect(partial(card.reloadCard, self))
		self.pinsPB.clicked.connect(partial(card.getCardPins, self))

	def copyOutput(self):
		self.qclip.setText(self.outputPTE.toPlainText())
		self.statusbar.showMessage('Output copied to clipboard')

	def copyInfo(self): # this is a QPlainTextEdit
		self.qclip.setText(self.infoTE.toPlainText())
		self.statusbar.showMessage('Output copied to clipboard')

	def isNumber(self, s):
		try:
			s[-1].isdigit()
			float(s)
			return True
		except ValueError:
			return False

	def onConfigNameChanged(self, text):
		# update the iniDictionary when text is changed
		if text:
			self.configNameUnderscored = text.replace(' ','_').lower()
			self.configPath = os.path.expanduser('~/linuxcnc/configs') + '/' + self.configNameUnderscored
			self.pathLabel.setText(self.configPath)
		else:
			self.pathLabel.setText('')

	def onMaxLinearVelChanged(self, text):
		if text:
			fpm = str(float(text) * 60)
			self.maxVelocityLbl.setText(f'{fpm} IPM')

	def linearUnitsChanged(self):
		if self.linearUnitsCB.itemData(self.linearUnitsCB.currentIndex()) == 'inch':
			for i in range(5):
				getattr(self, 'minLimit_' + str(i)).setToolTip('inches')
				getattr(self, 'maxLimit_' + str(i)).setToolTip('inches')
				getattr(self, 'maxVelocity_' + str(i)).setToolTip('inches per second')
				getattr(self, 'maxAccel_' + str(i)).setToolTip('inches per second per second')
				self.units = 'inches'
		if self.linearUnitsCB.itemData(self.linearUnitsCB.currentIndex()) == 'metric':
			for i in range(5):
				getattr(self, 'minLimit_' + str(i)).setToolTip('millimeters')
				getattr(self, 'maxLimit_' + str(i)).setToolTip('millimeters')
				getattr(self, 'maxVelocity_' + str(i)).setToolTip('millimeters per second')
				getattr(self, 'maxAccel_' + str(i)).setToolTip('millimeters per second per second')
				self.units = 'mm'
		if self.linearUnitsCB.itemData(self.linearUnitsCB.currentIndex()):
			self.axisTab.setEnabled(True)
			self.joint0tab.setEnabled(True)
		else:
			self.axisTab.setEnabled(False)

	def boardsChanged(self):
		bitfile = self.boardsCB.itemData(self.boardsCB.currentIndex())
		index = self.firmwareCB.findData(bitfile)
		if index >= 0:
			self.firmwareCB.setCurrentIndex(index)

	def configChanged(self):
		print(self.configCB.itemData(self.configCB.currentIndex()))

	def onAxisChanged(self):
		coordList = []
		for item in self.axisList:
			if getattr(self,item).itemData(getattr(self,item).currentIndex()):
				jointTab = getattr(self,item).objectName()[7]
				axisLetter = getattr(self,item).itemData(getattr(self,item).currentIndex())
				coordList.append(axisLetter)
				if axisLetter in ['X', 'Y', 'Z', 'U', 'V', 'W']:
					getattr(self, 'axisType_' + jointTab).setText('LINEAR')
				elif axisLetter in ['A', 'B', 'C']:
					getattr(self, 'axisType_' + jointTab).setText('ANGULAR')
				else:
					getattr(self, 'axisType_' + jointTab).setText('')
		self.coordinatesLB.setText(''.join(coordList))
		self.stepgensSB.setValue(len(coordList))

	def driveChanged(self):
		timing = self.sender().itemData(self.sender().currentIndex())
		joint = self.sender().objectName()[-1]
		if timing:
			getattr(self, 'stepTime_' + joint).setText(timing[0])
			getattr(self, 'stepSpace_' + joint).setText(timing[1])
			getattr(self, 'dirSetup_' + joint).setText(timing[2])
			getattr(self, 'dirHold_' + joint).setText(timing[3])
			getattr(self, 'stepTime_' + joint).setEnabled(False)
			getattr(self, 'stepSpace_' + joint).setEnabled(False)
			getattr(self, 'dirSetup_' + joint).setEnabled(False)
			getattr(self, 'dirHold_' + joint).setEnabled(False)
		else:
			getattr(self, 'stepTime_' + joint).setEnabled(True)
			getattr(self, 'stepSpace_' + joint).setEnabled(True)
			getattr(self, 'dirSetup_' + joint).setEnabled(True)
			getattr(self, 'dirHold_' + joint).setEnabled(True)

	def updateAxisInfo(self):
		if self.sender().objectName() == 'actionOpen':
			return
		joint = self.sender().objectName()[-1]
		scale = getattr(self, 'scale_' + joint).text()
		if scale and self.isNumber(scale):
			scale = float(scale)
		else:
			return

		maxVelocity = getattr(self, 'maxVelocity_' + joint).text()
		if maxVelocity and self.isNumber(maxVelocity):
			maxVelocity = float(maxVelocity)
		else:
			return

		maxAccel = getattr(self, 'maxAccel_' + joint).text()
		if maxAccel and self.isNumber(maxAccel):
			maxAccel = float(maxAccel)
		else:
			return

		if not self.units:
			self.errorDialog('Machine Tab:\nLinear Units must be selected')
			return
		accelTime = maxVelocity / maxAccel
		getattr(self, 'timeJoint_' + joint).setText('{:.2f} seconds'.format(accelTime))
		accelDistance = accelTime * 0.5 * maxVelocity
		getattr(self, 'distanceJoint_' + joint).setText('{:.2f} {}'.format(accelDistance, self.units))
		stepRate = scale * maxVelocity
		getattr(self, 'stepRateJoint_' + joint).setText('{:.0f} pulses'.format(abs(stepRate)))

	def spindleTypeChanged(self): 
		#print(self.spindleTypeCB.itemData(self.spindleTypeCB.currentIndex()))
		if self.spindleTypeCB.itemData(self.spindleTypeCB.currentIndex()):
			self.spindleGB.setEnabled(True)
			self.spindleInfoGB.setEnabled(True)
			self.encoderGB.setEnabled(False)
			self.spindlepidGB.setEnabled(False)
			if self.spindleTypeCB.itemData(self.spindleTypeCB.currentIndex()) == '1':
				self.spindleInfo1Lbl.setText("PWM on Step 4")
				self.spindleInfo2Lbl.setText("Direction on Dir 4")
			if self.spindleTypeCB.itemData(self.spindleTypeCB.currentIndex()) == '2':
				self.spindleInfo1Lbl.setText("UP on Step 4")
				self.spindleInfo2Lbl.setText("Down on Dir 4")
			if self.spindleTypeCB.itemData(self.spindleTypeCB.currentIndex()) == '3':
				self.spindleInfo1Lbl.setText("PDM on Step 4")
				self.spindleInfo2Lbl.setText("Direction on Dir 4")
			if self.spindleTypeCB.itemData(self.spindleTypeCB.currentIndex()) == '4':
				self.spindleInfo1Lbl.setText("Direction on Step 4")
				self.spindleInfo2Lbl.setText("PWM on Dir 4")

		else:
			self.spindleGB.setEnabled(False)
			self.spindleInfoGB.setEnabled(False)
			self.encoderGB.setEnabled(False)
			self.spindlepidGB.setEnabled(False)
			self.spindleInfo1Lbl.setText("No Spindle")
			self.spindleInfo2Lbl.setText("")
			self.spindleInfo3Lbl.setText("")
			self.spindleInfo4Lbl.setText("")


		"""
		pid = '0'
		if self.spindleTypeCB.itemData(self.spindleTypeCB.currentIndex()) == 'openLoop':
			pid = '0'
			self.ff0_s.setText('1')

			self.spindle = True
		if self.spindleTypeCB.itemData(self.spindleTypeCB.currentIndex()) == 'closedLoop':
			self.spindle = True
			pid = '0'
			self.ff0_s.setText('1')
			self.spindleGB.setEnabled(True)
			self.encoderGB.setEnabled(True)
			self.spindlepidGB.setEnabled(True)
		if not self.spindleTypeCB.itemData(self.spindleTypeCB.currentIndex()):
			self.spindle = False
			pid = ''
			self.ff0_s.setText('')

		self.p_s.setText(pid)
		self.i_s.setText(pid)
		self.d_s.setText(pid)
		self.ff1_s.setText(pid)
		self.ff2_s.setText(pid)
		self.bias_s.setText(pid)
		self.maxOutput_s.setText(pid)
		self.maxError_s.setText(pid)
		self.deadband_s.setText(pid)
		"""

	def pidSetDefault(self):
		tab = self.sender().objectName()[-1]
		if not self.linearUnitsCB.itemData(self.linearUnitsCB.currentIndex()):
			QMessageBox.warning(self,'Warning', 'Machine Tab\nLinear Units\nmust be selected', QMessageBox.Ok)
			return
		getattr(self, 'p_' + tab).setText('1000')
		getattr(self, 'i_' + tab).setText('0')
		getattr(self, 'd_' + tab).setText('0')
		getattr(self, 'ff0_' + tab).setText('0')
		getattr(self, 'ff1_' + tab).setText('1')
		getattr(self, 'ff2_' + tab).setText('0.00013')
		getattr(self, 'bias_' + tab).setText('0')
		getattr(self, 'maxOutput_' + tab).setText('0')
		if self.linearUnitsCB.itemData(self.linearUnitsCB.currentIndex()) == 'inch':
			maxError = '0.0005'
		else:
			maxError = '0.0127'
		getattr(self, 'maxError_' + tab).setText(maxError)
		getattr(self, 'deadband_' + tab).setText('0')

	def buildCB(self):
		for item in buildcombos.setupCombo('ipAddress'):
			self.ipAddressCB.addItem(item[0], item[1])
		for item in buildcombos.setupCombo('encoders'):
			self.encodersCB.addItem(item[0], item[1])
		for item in buildcombos.setupCombo('boards'):
			self.boardsCB.addItem(item[0], item[1])
		for item in buildcombos.setupCombo('display'):
			self.guiCB.addItem(item[0], item[1])
		for item in buildcombos.setupCombo('linearUnits'):
			self.linearUnitsCB.addItem(item[0], item[1])
		for item in buildcombos.setupCombo('angularUnits'):
			self.angularUnitsCB.addItem(item[0], item[1])
		for item in buildcombos.setupCombo('positionOffset'):
			self.positionOffsetCB.addItem(item[0], item[1])
		for item in buildcombos.setupCombo('positionFeedback'):
			self.positionFeedbackCB.addItem(item[0], item[1])
		for item in buildcombos.setupCombo('firmware'):
			self.firmwareCB.addItem(item[0], item[1])
		for item in buildcombos.setupCombo('spindle'):
			self.spindleTypeCB.addItem(item[0], item[1])
		for i in range(5):
			for item in buildcombos.setupCombo('axis'):
				getattr(self, 'axisCB_' + str(i)).addItem(item[0], item[1])
		for i in range(11):
			for item in buildcombos.setupCombo('input'):
				getattr(self, 'input_' + str(i)).addItem(item[0], item[1])
		for i in range(11):
			for item in buildcombos.setupCombo('joint'):
				getattr(self, 'inputJoint_' + str(i)).addItem(item[0], item[1])
		for i in range(6):
			for item in buildcombos.setupCombo('output'):
				getattr(self, 'output_' + str(i)).addItem(item[0], item[1])
		for item in buildcombos.setupCombo('debug'):
			self.debugCombo.addItem(item[0], item[1])
		for i in range(5):
			for item in buildcombos.setupCombo('drive'):
				getattr(self, 'driveCB_' + str(i)).addItem(item[0], item[1])
		for item in buildcombos.setupCombo('speed'):
			self.speedCB.addItem(item[0], item[1])

	def iniLoad(self):
		# iniList section, item, value
		for item in loadini.iniList():
			if self.config.has_option(item[0], item[1]):
				if isinstance(getattr(self, item[2]), QLabel):
					getattr(self, item[2]).setText(self.config[item[0]][item[1]])
				if isinstance(getattr(self, item[2]), QLineEdit):
					getattr(self, item[2]).setText(self.config[item[0]][item[1]])
				if isinstance(getattr(self, item[2]), QSpinBox):
					getattr(self, item[2]).setValue(abs(int(self.config[item[0]][item[1]])))
				if isinstance(getattr(self, item[2]), QDoubleSpinBox):
					getattr(self, item[2]).setValue(float(self.config[item[0]][item[1]]))
				if isinstance(getattr(self, item[2]), QCheckBox):
					getattr(self, item[2]).setChecked(eval(self.config[item[0]][item[1]]))
				if isinstance(getattr(self, item[2]), QGroupBox):
					getattr(self, item[2]).setChecked(eval(self.config[item[0]][item[1]]))
					#print(self.config[item[0]][item[1]])
				if isinstance(getattr(self, item[2]), QComboBox):
					index = getattr(self, item[2]).findData(self.config[item[0]][item[1]])
					if index >= 0:
						getattr(self, item[2]).setCurrentIndex(index)

	def errorDialog(self, text):
		dialog = QtWidgets.QDialog()
		dialog.ui = errorDialog()
		dialog.ui.setupUi(dialog)
		dialog.ui.label.setText(text)
		dialog.exec_()

	def errorMsg(self, text, title=None):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Warning)
		msgBox.setWindowTitle(title)
		msgBox.setText(text)
		msgBox.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
		returnValue = msgBox.exec()
		if returnValue == QMessageBox.Ok:
			return True
		else:
			return False

	def errorMsgOk(self, text, title=None):
		msgBox = QMessageBox()
		msgBox.setIcon(QMessageBox.Warning)
		msgBox.setWindowTitle(title)
		msgBox.setText(text)
		msgBox.setStandardButtons(QMessageBox.Ok)
		returnValue = msgBox.exec()
		if returnValue == QMessageBox.Ok:
			return True
		else:
			return False

	def help(self, index):
		dialog = QtWidgets.QDialog()
		dialog.ui = helpDialog()
		dialog.ui.setupUi(dialog)
		dialog.ui.label.setText(self.helpInfo(index))
		dialog.exec_()

def main():
	app = QApplication(sys.argv)
	ex = MainWindow()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
