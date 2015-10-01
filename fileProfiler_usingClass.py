#!/bin/sh
# A Detailed Data Profiler Tool
# Developer - SUDIP SHRESTHA 

import MySQLdb
import os
import csv
import ConfigParser




class configReader():
	global config
	def readConfig(self):
		
		self.config = ConfigParser.RawConfigParser()
		self.config.read('config.ini')



# Learn the properties of csv so as to use it data = csv.reader(f)

class readColumns():
	global rdcnfg 
	rdcnfg = configReader()
	rdcnfg.readConfig()
	def readHeaders(self):
		file = rdcnfg.config.get('csv', 'csv.filename')
		
		headers = []
		with open(file,'r') as f:
			data = csv.reader(f)
			counter = 0
			for line in data:

				if counter == int(rdcnfg.config.get('csv','csv.topBlankOffset')):
					print counter
					headers = line
					break
				counter += 1
		return headers

	def readTableColumns(self):
		host = rdcnfg.config.get('database', 'database.host')
		username = rdcnfg.config.get('database', 'database.user')
		password = rdcnfg.config.get('database', 'database.password')
		dbname = rdcnfg.config.get('database', 'database.dbname')

		db = MySQLdb.connect(host, username, password, dbname)
		cursor = db.cursor()
		tablecolumncollection=[]
		query  = "select raw_column_field from test_db.data_validation where client_name='Teletech' and  raw_table_name='zzz_teletech_candidate_raw'" 
		#print(query)
		cursor.execute(query)
		tablecolumnlist=[]
		tablecolumncollection  = cursor.fetchall()
		for column in tablecolumncollection:
			tablecolumnlist.append(column[0])
		db.close()
		return tablecolumnlist

class compareHeaders():
	rdColns = readColumns()
	file_headers = rdColns.readHeaders()
	db_headers = rdColns.readTableColumns()
	def compareHeaders(self):
		for  i in range(len(self.db_headers)):
			if(self.db_headers[i]<>self.file_headers[i]):
				print "Table Column : " + self.db_headers[i] + " No Matching With File Header : " + self.file_headers[i] 
			
			else:
				print("Table Column exactly matching with File Headers")
		
class __main__():
	cnfRead = configReader()
	cnfRead.readConfig()
	
	cmpHeader = compareHeaders()
	#cmpHeader.file_headers
	cmpHeader.compareHeaders()
#main()	