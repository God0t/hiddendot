from lib.const import EVIL_CHARS
from random import choice

import whois

class HiddenDot(object):

	def __init__ (self, domain):
		self.domain = domain.split (".") [0]
		self.domain_postfix = domain.split (".") [-1]
		self.output = ""
		
	def generate_sample_list (self):
		full_list = list()
		for character in self.domain:
			full_list.append (self._replace (character, self.domain) + "." + self.domain_postfix)
		return full_list
		
	def get_clean_domain (self):
		return self.domain + "." + self.domain_postfix
		
	def check_sample (self, domain):
		try:
			whois.whois (domain)
			return False
		except whois.parser.PywhoisError:
			return True
		
	def _replace (self, char, dom):
		if EVIL_CHARS [char] is not None and char in EVIL_CHARS.keys ():
			return dom.replace (char, choice (EVIL_CHARS [char]))
		else: return dom