#program to take the database backups
import MySQLdb
#import sys
import os
import csv
import ConfigParser

#config = None

def readConfig():
	global config
	config = ConfigParser.RawConfigParser()
	config.read('config.ini')

# Learn the properties of csv so as to use it data = csv.reader(f)

def readHeaders():
	file = config.get('csv', 'csv.filename')
	
	headers = []
	with open(file,'r') as f:
		data = csv.reader(f)
		counter = 0
		for line in data:

			if counter == int(config.get('csv','csv.topBlankOffset')):
				print counter
				headers = line
				break
			counter += 1
	return headers

def readTableColumns():
	host = config.get('database', 'database.host')
	username = config.get('database', 'database.username')
	password = config.get('database', 'database.password')
	dbname = config.get('database', 'database.dbname')
	
	db = MySQLdb.connect(host, username, password, dbname)
	cursor = db.cursor()
	tablecolumncollection=[]
	query  = "select raw_column_field from data_validation where client_name='Teletech' and  raw_table_name='zzz_teletech_raw'" 
	print(query)
	cursor.execute(query)
	tablecolumnlist=[]
	tablecolumncollection  = cursor.fetchall()
	for column in tablecolumncollection:
		tablecolumnlist.append(column[0])
	db.close()
	
def main():
	readConfig()
	headers = readHeaders()
	print headers
	
main()	