#!/bin/sh
# Script For.
# Developer - SUDIP SHRESTHA 

import ConfigParser

class ConfigReader():
	global config
	def readConfig(self):
		
		self.config = ConfigParser.RawConfigParser()
		self.config.read('config.ini')