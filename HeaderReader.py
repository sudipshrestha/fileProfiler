#!/bin/sh
# Script For.
# Developer - SUDIP SHRESTHA 

import csv
from ConfigReader import *
import MySQLdb


class HeaderReader():
	global rdcnfg 
	rdcnfg = ConfigReader()
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