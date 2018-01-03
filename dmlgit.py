import git
import os
import sys


print("sys.platform is " + sys.platform)
if sys.platform.lower() == "win32":
	dmlauto = r"c:\webdev\dmlauto"
	dmlreact = r"c:\webdev\dmlreact"
elif sys.platform.lower() == "linux":
	dmlauto = "home/xxx"
else:
	print("Unsupported OS, success not guarenteed")

curr_dir = os.getcwd()
git_dirs = (curr_dir, dmlauto, dmlreact)

for git_dir in git_dirs:
	g = git.cmd.Git(git_dir)
	#g.add(update=True)
	#g.commit()
	try:
		g.push()
	except git.exc.GitCommandError:
		g.pull()
	#g.checkout()
