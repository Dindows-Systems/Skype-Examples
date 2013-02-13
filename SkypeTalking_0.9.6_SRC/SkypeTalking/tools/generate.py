from glob import glob
import os
import sys
import txt2tags

def main():
	print "Generating documentation..."
	docfiles = glob(r"..\help\*\*.t2t")
	for f in docfiles:
		print f
		txt2tags.exec_command_line(['-t', 'html', '--encoding=UTF-8', '--toc', f])
	print "Done!"
	print "Compiling language files..."
	lfiles = glob(ur"..\src\locale\*\LC_MESSAGES\*.po")
	for f in lfiles:
		print f
		os.spawnv(os.P_WAIT, ur"%s\python.exe" % sys.exec_prefix, ["python", ur'"%s\Tools\i18n\msgfmt.py"' % sys.exec_prefix, f])
	print "Done!"

if __name__=="__main__": main()