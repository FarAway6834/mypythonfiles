from zipfile import ZipFile as zip
from tarfile import open as tar

def gentz(s):
  def tz(file, mode = f'r:{s}z', wv = f'w:{s}z', v = 'w'):
	  if mode == v: mode = wv
	  return tar(file, mode)
  tz.__name__ = f't{s}z'
  return tz
