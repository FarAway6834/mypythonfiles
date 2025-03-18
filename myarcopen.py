from zipfile import ZipFile as zip
from tarfile import open as tar

o = open

def gentz(s):
	def tz(file, mode = 'r', wv = f'w:{s}z', rv = f'r:{s}z', r = 'r', w = 'w'):
		match mode:
			case r: mode = rv;
			case w: mode = wv;
			case _: pass
		return tar(file, mode)
	tz.__name__ = f't{s}z'
	return tz

txz, tgz = map(gentz, 'xg')

def open(f, mode = 'r'):
	file = (lambda x, y : (x == 'tar', y))(*f.split('.')[-2:])
	match file:
		case (True, 'gz') | (False, 'tgz') | (True, 'tgz'): return tgz(f, mode = mode)
		case (True, 'xz') | (False, 'txz') | (True, 'txz'): return txz(f, mode = mode)
		case (True, 'whl') | (False, 'whl') | (True, 'zip') | (False, 'zip'): return zip(f, mode = mode)
		case _: return o(f)
