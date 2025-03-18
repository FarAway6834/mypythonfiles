from zipfile import ZipFile as zip
from tarfile import open as tar

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
