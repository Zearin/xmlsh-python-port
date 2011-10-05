#!/usr/bin/env python -3
# -*- coding: UTF-8 -*-

#	NOTE
#	The shebang's `-3' option warns about Python3 incompatibilities
#	that 2to3.py cannot easily fix.  
#
#	It should remain in order to facilitate easier migration to Python3
#	at a future date.

#---------------------------
#	Standard Library Modules
#---------------------------
import os, sys
import string, unicodedata
import readline, rlcompleter

from optparse import make_option
import optparse

import subprocess
import xml

from decorator import decorator


#---------------------------
#	Non-Standard Lib Modules
#---------------------------
#	Bi-directional communication with Java	
#import py4j.java_gateway
#import JavaGateway
#	Awesome CLI module :D
from cmd2 import Cmd, options, __version__



class XMLSH(Cmd):
	'''Attempt at implementing XMLSH front-end in Python.'''
	
	#====================================================================================
	#	VARIABLES
	#====================================================================================
	
	#	
	#	Shell Settings
	#
	echo	= False
	colors	= True
	debug	= True
	prompt	= str(os.getcwd() + '\n<xmlsh> ')

	intro   = 	"\n" + "xmlsh (using cmd2 {0})".format(__version__ ) + "\n\n"


	#
	#	Shortcuts (useful for aliasing characters illegal in function names)
	#
	shortcuts	= {
		':'	:	'colon',
		'['	:	'test'
	}


	
	#	Adapted from Py4J author Bart’s Gist on Github:
	#	
	#	https://gist.github.com/1070311
	
#	@privateMethod
#	def _start_java():
#		# Note: I assume that my_library.jar contains the library you want to expose with your CLI program.
# 		ARGS = ['java', 
# 				'-cp', 
#  				
#				'/Users/amrogers/Developer/Applications/Tools/xmlsh/:'						+ \ 
#				'/Users/amrogers/Developer/Applications/Tools/xmlsh/bin:'					+ \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/bin/xmlsh-1.1.jar:'		+ \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/log4j-1.2.7.jar:'	+ \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/saxon9he.jar:' 		+ \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/xercesImpl.jar:'	+ \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/jline-0.9.94.jar:' 	+ \
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/woodstox-core-asl-4.0.3.jar:' + \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/stax2-api-3.0.1.jar:'	+ \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/stax-utils.jar:' 	+ \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/jing.jar:' 			+ \
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/trang.jar:' 		+ \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/saxon.jar:' 		+ \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/tagsoup-1.2.jar:' 	+ \ 
# 				'/Users/amrogers/Developer/Applications/Tools/xmlsh/lib/xom-1.2.6.jar' 		+ \ 
# 				'/path/to/my/class_dir:/path/to/py4j-java.jar', 
#
# 				'p1.MyApplication']
#
# 		p = subprocess.Popen( ARGS )
# 		self.poutput( 'Java Started: {0}'.format(p.pid) )
	
	
# 	def _stop_java():
# 		gateway = JavaGateway()
# 		gateway.shutdown()
#		# Two alternatives:
#		# (1) You could call a method on the Java side that calls System.exit(0);
#		# (2) You could save the pid from start_java and kill the process, but you need to handle mac, linux, and 
#		#     windows...
	


	#====================================================================================
	#	METHODS	
	#====================================================================================
	
		
	#	HOOK methods
	#	------------

	def precmd(self, line):
		self.poutput("\n")
		return line

	#def postcmd(self, stop, line):
	#	#self.poutput("\n")
	#	stop = False
	#	return line

	def preloop(self):
		return

	def postloop(self):
		#self.poutput("Closing down Java...\n\n")
		#self.poutput("Exiting shell...\n\n")
		return



	@decorator
	def streaming(self):
		'''
			Decorator available simply for marking streaming functions.
			It has no other impact.
		'''
		pass



	#	COMMAND methods
	#	---------------
	@options([make_option(
					'-v'    ,	'--verbose', 
					action	=	'store_true', 
					help	=	'Even more blah!') ])
	def do_blah(self, arg, opts):
		'''Dummy command.  Supposed to print “blah!”'''
		
		output = self.colorize( self.colorize("blah!\n",'bold'), 'magenta' )
		
		if opts.verbose:
			self.poutput( output )
			self.poutput( output )
			return
		else:
			self.poutput( output )
			return	
	
	

	#@options([make_option(
	#		 ) ])
	def do_colon(self):
		''''''
		pass


	#	@FIXME
	#		On the CLI this is the character “[”.
	def do_test(self):
		''''''
		pass
	
	
	def do_break(self):
		''''''
		pass
	

	def do_cd(self):
		''''''
		pass
	
	
	def do_continue(self):
		''''''
		pass
	
	
	@streaming
	def do_csv2xml(self):
		''''''
		pass
	
	
	def do_declare(self):
		''''''
		pass
	

	def do_echo(self):
		''''''
		pass	
	
	
	def do_eval(self):
		''''''
		pass
	
	
# 	def do_exit(self):
# 		pass
	
	
	def do_false(self):
		return False
	
	
	@streaming
	def do_fixed2xml(self):
		''''''
		pass
	
	
	#def do_help(self):
	#	pass
	
	
	def do_http(self):
		''''''
		pass
	
	
	def do_httpserver(self):
		''''''
		pass
	
	
	def do_httpsession(self):
		''''''
		pass
	
	
	def do_import(self):
		''''''
		pass
	
	
	def do_jcall(self):
		''''''
		pass
	
	
	def do_jobs(self):
		''''''
		pass
	
	
	def do_log(self):
		''''''
		pass
	
	
	def do_QName(self):
		''''''
		pass
	
	
	def do_quote(self):
		''''''
		pass
	
	
	def do_read(self):
		''''''
		pass
	
	
	def do_require(self):
		''''''
		pass
	
	
	def do_return(self):
		''''''
		pass
	
	
	def do_rngconvert(self):
		''''''
		pass
	
	
	def do_rngvalidate(self):
		''''''
		pass
	
	
	def do_set(self):
		''''''
		pass
	
	
	def do_shift(self):
		''''''
		pass
	
	
	def do_source(self):
		''''''
		pass
	
	
	def do_test(self):
		''''''
		pass
	
	
	def do_throw(self):
		''''''
		pass
	
	
	def do_tie(self):
		''''''
		pass


	def do_true(self):
		return True
	
	
	def do_unset(self):
		''''''
		pass
	
	
	def do_wait(self):
		''''''
		pass
	
	
	def do_xaddattribute(self):
		''''''
		pass
	
	
	def do_xaddbase(self):
		''''''
		pass
	
	
	def do_xbase(self):
		''''''
		pass
	
	
	@streaming
	def do_xcat(self):
		''''''
		pass
	
	
	@streaming
	def do_xcmp(self):
		''''''
		pass
	
	
	@streaming
	def do_xdelattribute(self):
		''''''
		pass
		
		
	def do_xdelete(self):
		''''''
		pass
	
	
	def do_xecho(self):
		''''''
		pass
	
	
	def do_xed(self):
		''''''
		pass
	
	
	def do_xfile(self):
		''''''
		pass
	
	
	def do_xgetopts(self):
		''''''
		pass
	
	
	def do_xgrep(self):
		''''''
		pass
	
	
	@streaming
	def do_xidentity(self):
		''''''
		pass
	
	
	def do_xinclude(self):
		''''''
		pass
	
	
	def do_xls(self):
		''''''
		pass
	
	
	@streaming
	def do_xmd5sum(self):
		''''''
		pass
	
	
	def do_xml2csv(self):
		''''''
		pass
	
	
	#def do_xmlsh(self):
	#	pass
	
	
	def do_xmove(self):
		''''''
		pass
	
	
	def do_xpath(self):
		''''''
		pass
	
	
	def do_xproperties(self):
		''''''
		pass
	
	
	def do_xpwd(self):
		''''''
		pass
	
	
	def do_xquery(self):
		''''''
		pass
	
	
	def do_xread(self):
		''''''
		pass
	
	
	def do_xsdvalidate(self):
		''''''
		pass
	
	
	def do_xslt(self):
		''''''
		pass
	
	
	def do_xslt1(self):
		''''''
		pass
	
	
	@streaming
	def do_xsplit(self):
		''''''
		pass
	
	
	def do_xsql(self):
		''''''
		pass
	
	
	@streaming
	def do_xtee(self):
		''''''
		pass
	
	
	def do_xtype(self):
		''''''
		pass
	
	
	@streaming
	def do_xunzip(self):
		''''''
		pass
	
	
	def do_xuri(self):
		''''''
		pass
	
	
	def do_xvalidate(self):
		''''''
		pass
	
	
	def do_xversion(self):
		''''''
		pass
	
	
	def do_xwhich(self):
		''''''
		pass
	
	
	@streaming
	def do_xzip(self):
		''''''
		pass


# 	XPROC
# 		STEPS
# 			p:pipeline
# 			p:for-each
# 			p:viewport
# 			p:choose
# 			p:when
# 			p:otherwise
# 			p:group
# 			p:try
# 		REQUIRED
# 			p:add-attribute
# 			p:add-xml-base
# 			p:compare
# 			p:count
# 			p:delete
# 			p:directory-list
# 			p:error
# 			p:escape-markup
# 			p:filter
# 			p:http-request
# 			p:identity
# 			p:insert
# 			p:label-elements
# 			p:load
# 			p:make-absolute-uris
# 			p:namespace-rename
# 			p:pack
# 			p:parameters
# 			p:rename
# 			p:replace
# 			p:set-attributes
# 			p:sink
# 			p:split-sequence
# 			p:store
# 			p:string-replace
# 			p:unescape-markup
# 			p:unwrap
# 			p:wrap
# 			p:wrap-sequence
# 			p:xinclude
# 			p:xslt
# 		OPTIONAL
# 			p:exec
# 			p:hash
# 			p:uuid
# 			p:validate-with-relax-ng
# 			p:validate-with-schematron
# 			p:validate-with-xml-schema
# 			p:www-form-urldecode
# 			p:www-form-urlencode
# 			p:xquery
# 			p:xsl-formatter

#-----------------------------------------------------------------------------------------
#	HERE BEGINS THE PROGRAM! :D
#-----------------------------------------------------------------------------------------
xmlsh = XMLSH()
xmlsh.prompt = xmlsh.colorize( xmlsh.prompt, 'bold' )
xmlsh.cmdloop( )
