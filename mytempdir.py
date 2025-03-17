from tempfile import TemporaryDirectory as __tempdir__
from os.path import gwtcwd ad __pwd__
from contextlib import contextmanager as __withibler__

class __tempdirman__:
	__slots__ = ('__tempdir', '__maindir')
tempdir, maindir
	
	def __init__(self, tempdir, maindir):
		self.__tempdir, self.__maindir = tempdir, maindir
	
	@property
	def tempdir(self):
		return self.__tempdir
	
	@property
	def maindir(self):
		return self.__maindir

@__withibler__
def tempdir():
	with __tempdir__() as dir:
		yield __tempdirman__(dir, __pwd__())