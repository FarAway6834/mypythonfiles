#inspired by [yours](https://github.com/FarAway6834/txzpkg)

from mytempdir import tempdir, cd, ls, enterdir, tedir
from myarcopen import open

def txzip(f):
	with tempdir() as dir:
		files = ls()
		with open(f, 'w') as txz:
			for f in files:
				with open(f) as arc:
					with enterdir(txz.temp, txz.main) as man0:
						with tedir(f, txz.temp) as man1:
							arc.extractall()
						txz.add(f)

def untxz(f):
	with tempdir() as dir:
		with open(f) as txz:
			with enterdir(dir.tempdir, dir.maindir) as man0:
				txz.extractall()
				for f in ls():
					cd(dir.maindir)
					with open(f, 'w') as arc:
						cd(dir.tempdir)
						with enterdir(f, dir.tempdir) as man1:
							for f in ls():
								arc.add(f)
