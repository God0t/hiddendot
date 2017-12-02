from lib.hdot import HiddenDot
from lib.utils.colors import *

from sys import argv
from json import dumps


def init_opt ():
	from optparse import OptionParser
	
	p = OptionParser ("--dictionary <dictionary file>")
	p.add_option ("-d", "--dictionary", dest="dictionary", help="Dictionary with target domains", type="string")
	
	return p.parse_args()
	
def main ():

	options = init_opt () [0]
	
	if not options.dictionary:
		print (ERROR + "%s -d <dictionary file>" % argv [0])
		exit (1)
	
	dictionary = open(options.dictionary)
	out = list()
	
	for domain in dictionary.readlines ():
		domain_fixed = domain.strip ("\n\r")
		
		print (INFO + "Working on %s ..." % domain_fixed)
		hd = HiddenDot (domain_fixed)
		
		
		for sample in hd.generate_sample_list():
			print (INFO + "Sample is %s" % sample)
			
			if hd.check_sample(sample):
				print (SUCCESS + "Success! Domain %s is available!!!" % sample)
				out.append(sample)
				break
				
			else:
				print (FAIL + "Sorry, domain %s is not available :(" % sample)	
			
	dictionary.close()
		
	print()
	print (SUCCESS + "----- Available domains ----- ")
	for domain in out: print (domain)
	
if __name__ == "__main__":
	
	main ()