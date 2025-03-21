from tempfile import TemporaryDirectory as __tempdir__
from os import getcwd as __pwd__
from os import chdir as cd
from os import listdir as ls
from os import mkdir
from contextlib import contextmanager as __withibler__

class __tempdirman__:
	__slots__ = ('__tempdir', '__maindir')
	
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

@__withibler__
def enterdir(dir, back):
	cd(dir)
	yield None
	cd(back)

@__withibler__
def tedir(dir, back):
	mkdir(dir)
	with enterdir(dir, back) as man:
		yield man
