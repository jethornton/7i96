import configparser

def load(parent, config):
	card = config.get('SSERIAL', 'ssCardCB')
	if card == '7i64':
		for key in config['SSERIAL']:
			cb = config.get('SSERIAL', key)
			#print(key, cb)
			if not cb:
				index = getattr(parent, key).findText('Signal Only')
			else:
				index = getattr(parent, key).findData(cb)
			if index > 0:
				getattr(parent, key).setCurrentIndex(index)
