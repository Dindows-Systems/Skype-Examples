from glob import glob
import os
import shutil
import sys
import versionInfo

###Globals
BuildDir=os.path.join(os.getcwdu(), "build")
DistDir=os.path.join(os.getcwdu(), "dist")
OutputDir=os.path.join(os.getcwdu(), "SkypeTalking")
SetupDir=os.path.join(os.getcwdu(), 'SkypeTalkingBinary')
InnoScript=r"..\installer\SkypeTalking.iss"
InnoExec=r'"C:\Program Files\Inno Setup 5\ISCC.exe"'
SevenZipExec=r'"c:\Program Files\7-Zip\7z.exe"'
GenerateTool=os.path.join(os.path.abspath('..'), 'tools', 'generate.py')
###EndGlobals

def removeOld():
	print "Checking for older existing distributions..."
	if os.path.exists(BuildDir):
		print "Removing directory %s..."%os.path.dirname(BuildDir)
		shutil.rmtree(BuildDir)
	if os.path.exists(DistDir):
		print "Removing directory %s..."%os.path.dirname(DistDir)
		shutil.rmtree(DistDir)
	if os.path.exists(OutputDir):
		print "Removing directory %s..."%os.path.dirname(OutputDir)
		shutil.rmtree(OutputDir)

def buildNew():
	IgnoreItems=shutil.ignore_patterns("*.po", "*.t2t")
	print "Building Distribution. Please wait..."
	os.system(GenerateTool)
	setup()
	print "Copying files..."
	os.chdir(DistDir)
	shutil.copy("../../contributors.txt", os.getcwdu())
	shutil.copy("../../license.txt", os.getcwdu())
	shutil.copytree("../../help", "help", ignore=IgnoreItems)
	shutil.copytree(os.path.join([path for path in sys.path if path.endswith('site-packages')][0],'accessible_output','lib'), "lib", ignore=IgnoreItems)
	shutil.copytree("../locale", "locale", ignore=IgnoreItems)
	shutil.copytree(DistDir, OutputDir)
	os.chdir(os.path.dirname(__file__))
	shutil.rmtree(BuildDir)
	shutil.rmtree(DistDir)
	os.remove(os.path.join(OutputDir, "w9xpopen.exe"))

def buildSetup():
	try:
		os.system(InnoExec+" "+InnoScript)
	except:
		print "Error running Inno Setup..."

def makePortableArchive():
	args="a -sfx7z.sfx .\\SkypeTalkingBinary\\SkypeTalking_%s_Portable.exe SkypeTalking\\"%versionInfo.version[0]
	try:
		os.system(SevenZipExec+" "+args)
	except:
		print "Error running 7zip."

def main():
	removeOld()
	buildNew()
	buildSetup()
	makePortableArchive()

def setup():
	sys.argv.append('py2exe')
	from distutils.core import setup
	import py2exe
	setup(
		name = versionInfo.name,
		version = "0.9",
		description = versionInfo.description,
		url = versionInfo.url,
		license = versionInfo.license,
		author = versionInfo.author,
		author_email = versionInfo.author_email,
		platforms = [versionInfo.platform],
		data_files = [("",[versionInfo.name+".ico",
							"gdiplus.dll",
							"Microsoft.VC90.CRT.manifest",
							"msvcp90.dll",
							"msvcr90.dll"])],
		windows=[{
				"script": "SkypeTalking.pyw",
				"uac_info": ("asInvoker", False),
				"dest_base": versionInfo.name,
				"icon_resources": [(0, versionInfo.name+".ico")]}],
		options={
			"py2exe":{"bundle_files":3,
				"optimize":2,
				"excludes":["win32ui", "pywin.dialogs", "pywin.debugger.dbgcon", "tkinter", "tk", "Tkconstants", "Tkinter", "tcl", "_imagingtk", "PIL._imagingtk", "ImageTk", "PIL.ImageTk", "FixTk"],
				"includes":["win32com", "win32event", "win32api", ],
				"dll_excludes": ["powrprof.dll", "mswsock.dll"]}})

if __name__=="__main__":
	main()