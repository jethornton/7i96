import configparser

def load(parent, config):
	card = config.get('SSERIAL', 'ssCardCB')
	if card == '7i64':
		for key in config['SSERIAL']:
			value = config.get('SSERIAL', key)
			if key != 'ssCardCB':
				getattr(parent, key).setText(value)
