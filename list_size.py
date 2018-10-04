import urllib
import argparse
size = 0
comp = 0
ucomp = 0
def to_gb(x):
	return int(x) / 1024 / 1024 / 1024
def to_mb(x):
	return int(x) / 1024 / 1024 
def check(loc):
	global size, comp, ucomp
	f = open(loc,'r').readlines()
	for i in f:
		try:
			o = urllib.urlopen(i.replace('\n',''))
			size = size + int(o.info()['Content-Length'])
			print i.replace('\n','')+ "  " + str(to_mb(o.info()['Content-Length']))
			comp = comp + 1
		except Exception as e:
			print "ERROR"
			print i
			print e
			ucomp = ucomp + 1
			pass
	print "\n"
	print "################################"
	print "fullsize(Gb) = " + str(to_gb(size))
	print "fullsize(Mb) = " + str(to_mb(size)) 
	print "succes = " + str(comp)
	print "fail = " + str(ucomp)
parser = argparse.ArgumentParser()
parser.add_argument("loc", help="find command")
args = parser.parse_args()
check(str(args.loc))