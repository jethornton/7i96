#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os, configparser, platform
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QFileDialog, QLineEdit, QSpinBox, QCheckBox, QComboBox, QLabel, QGroupBox, QDoubleSpinBox, QMessageBox)
import c7i96.buildcombos as buildcombos
import c7i96.loadini as loadini
import c7i96.checkit as checkit
import c7i96.buildfiles as buildfiles
import c7i96.card as card
import c7i96.helptext as helptext
from c7i96.dialog import Ui_Dialog as errorDialog
from c7i96.help import Ui_Dialog as helpDialog
from c7i96.about import Ui_about as aboutDialog

UI_FILE = os.path.join(os.path.dirname(__file__), "c7i96.ui")

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		uic.loadUi(UI_FILE, self)
		self.version = '1.1'
		self.config = configparser.ConfigParser(strict=False)
		self.cwd = os.getcwd()
		#self.linuxcncDir = os.path.expanduser('~/linuxcnc')
		#self.test = '~/linuxcnc/configs/' + 'fred'
		#print(os.path.expanduser(self.test))
		#self.configsDir = os.path.expanduser('~/linuxcnc/configs')
		#self.gcodeDir = os.path.expanduser('~/linuxcnc/nc_files')
		#self.subroutineDir = os.path.expanduser('~/linuxcnc/subroutines')
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
		# for testing
		#self.config.read('/home/john/linuxcnc/configs/fred/fred.ini')
		#self.iniLoad()

		self.show()

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
		pass

	@pyqtSlot()
	def on_actionAbout_triggered(self):
		dialog = QtWidgets.QDialog()
		dialog.ui = aboutDialog()
		dialog.ui.setupUi(dialog)
		#dialog.ui.label.setText(text)
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
		 print('File Save As')

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
		self.testConnectionPB.clicked.connect(self.cardRead)
		self.flashPB.clicked.connect(self.flashCard)
		self.reloadPB.clicked.connect(self.reloadCard)
		self.copyPB.clicked.connect(self.copyOutput)
		self.spindleTypeCB.currentIndexChanged.connect(self.spindleTypeChanged)
		self.linearUnitsCB.currentIndexChanged.connect(self.linearUnitsChanged)
		self.pinsPB.clicked.connect(self.getPins)
		self.cpuPB.clicked.connect(self.cpuInfo)
		self.nicPB.clicked.connect(self.nicInfo)
		self.calcNicPB.clicked.connect(self.calcNic)
		self.readTmaxPB.clicked.connect(self.readTmax)

	def readTmax(self):
		card.readTmax(self)

	def calcNic(self):
		card.nicCalc(self)

	def getPins(self):
		card.pins(self)

	def cardRead(self):
		card.readCard(self)

	def flashCard(self):
		card.flashCard(self)

	def reloadCard(self):
		card.reloadCard(self)

	def cpuInfo(self):
		card.cpuInfo(self)

	def nicInfo(self):
		card.nicInfo(self)


	def copyOutput(self):
		self.qclip.setText(self.outputLB.text())
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
		if self.spindleTypeCB.itemData(self.spindleTypeCB.currentIndex()) == 'openLoop':
			pid = '0'
			self.ff0_s.setText('1')
			self.spindleGB.setEnabled(True)
			self.encoderGB.setEnabled(False)
			self.spindlepidGB.setEnabled(False)
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
			self.spindleGB.setEnabled(False)
			self.encoderGB.setEnabled(False)
			self.spindlepidGB.setEnabled(False)
		self.p_s.setText(pid)
		self.i_s.setText(pid)
		self.d_s.setText(pid)
		self.ff1_s.setText(pid)
		self.ff2_s.setText(pid)
		self.bias_s.setText(pid)
		self.maxOutput_s.setText(pid)
		self.maxError_s.setText(pid)
		self.deadband_s.setText(pid)

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
		#dialog.ui.windowTitle('Configuration Errors')
		dialog.ui.label.setText(text)
		dialog.exec_()

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
