#!/bin/sh
# A Detailed Data Profiler Tool
# Developer - SUDIP SHRESTHA 

import os
from HeaderReader import *
from HeaderComparision import *
from ConfigReader import *





# Learn the properties of csv so as to use it data = csv.reader(f)




		
class __main__():
	cnfRead = ConfigReader()
	cnfRead.readConfig()
	
	cmpHeader = HeaderComparision()
	#cmpHeader.file_headers
	cmpHeader.compareHeaders()
#main()	