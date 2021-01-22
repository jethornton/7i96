import os
from PyQt5.QtCore import QProcess

class extjob:
	def __init__(self, cmd, args=None):
		super().__init__()
		self.stdout = None
		self.p = QProcess()
		self.p.readyReadStandardOutput.connect(self.handle_stdout)
		self.p.readyReadStandardError.connect(self.handle_stderr)
		self.p.errorOccurred.connect(self.handle_error)
		self.p.stateChanged.connect(self.handle_state)
		# Clean up once complete.
		self.p.finished.connect(self.process_finished)
		if args is None:
			self.p.start(cmd)
		else:
			self.p.start(cmd, args)


	def handle_stderr(self):
		data = self.p.readAllStandardError()
		stderr = bytes(data).decode("utf8")
		print('here')
		return stderr

	def handle_stdout(self):
		data = self.p.readAllStandardOutput()
		self.stdout = bytes(data).decode("utf8")

	def handle_state(self, state):
		states = {   
			QProcess.NotRunning: 'Not running',
			QProcess.Starting: 'Starting',
			QProcess.Running: 'Running',
		}
		state_name = states[state]
		#if not self.p.errorOccurred:
		#	self.message(f"State changed: {state_name}")

	def process_finished(self):
		return self.stdout

	def handle_error(self):
		errors = {
			0:'Failed to Start',
			1:'Crashed',
			2:'Timedout',
			3:'ReadError',
			4:'WriteError',
			5:'UnknownError',
			}
		self.message(f"{self.p.program()} had the following error:\nerrors.get(self.p.error())")
