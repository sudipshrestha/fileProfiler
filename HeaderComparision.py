#!/bin/sh
# Script For.
# Developer - SUDIP SHRESTHA 


from ConfigReader import *
from HeaderReader import *


class HeaderComparision():
	rdColns = HeaderReader()
	file_headers = rdColns.readHeaders()
	db_headers = rdColns.readTableColumns()
	def compareHeaders(self):
		for  i in range(len(self.db_headers)):
			if(self.db_headers[i]<>self.file_headers[i]):
				print "Table Column : " + self.db_headers[i] + " No Matching With File Header : " + self.file_headers[i] 
			
			else:
				print("Table Column exactly matching with File Headers")