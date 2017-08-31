
import sys
import subprocess

def run(dirs):
	badconf = 0
	for x in dirs:
		try:
			f = open(x+"/App.nam", "r")
			print("[*]Checking file App.nam...")
			if f.read() == "Test App":
				print("[!]File App.nam is not configured...")
				badconf += 1
			f.close()
		except:
			pass
		try:
			f = open(x+"/App.ver", "r")
			print("[*]Checking file App.ver...")
			if f.read() == "1.0.0t":
				badconf += 1
				print("[!]File App.ver is not configured...")
			f.close()
		except:
			pass
		try:
			f = open(x+"/CRYfw.ver", "r")
			f.close()
		except:
			print("[!]File CRYfw.ver doesn't exists!")
			badconf+=1
	if badconf != 0:
		print("[*]Some files are not well configured or doesn't exists, configure/create them them with FAWC configure")

if __name__="__main__":
	if sys.argv[1] = "configure":
		print("[*]Configuring CRYFrameWork files...")
		CRYDir = sys.argv[2]
		try:
			f = open(CRYDir+"/AppData/App.nam", "w")
			f.write(input("[*]Insert App name: "))
			f.close()
		except:
			raise IOError("Could not Open File in "+ CRYDir + "/AppData")
		try:
			f = open(CRYDir+"/AppData/App.ver", "w")
			f.write(input("[*]Insert App Version: "))
			f.close()
		except:
			raise IOError("Could not open file in "+ CRYDir + "/AppData")
		try:  
			subprocess.check_output("mkdir " + CRYDir + "/temp")
			subprocess.check_output("curl http://raw.github.com/CRY0gen/CRYFrameWork/CRYData/CRYfw.ver -o "+ CRYDir+"/temp/CRYfw.ver.o", shell=True)
			f = open(CRYDir+"/temp/CRYfw.ver.o", "r")
			tmp = f.read()
			tmp = tmp.decode("utf-8")
			f.close()
			f = open(CRYDir+"temp/CRYfw.ver", "w")
			f.write(tmp)
			f.close()
			print("[°]CRYfw.ver successfully configured...")
		except :
			raise ("Could not configure CRYfw.ver, is curl installed?")
	else:
		print("Usage: FAWC configure <path>")
		print("Example: FAWC configure $HOME/CRYFrameWork ")
		exit()
