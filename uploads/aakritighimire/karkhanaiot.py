#! /usr/bin/python3
import sys

#IGNORE THESE LINE, LEAVE AS IT IS
#FOR SERVER PARSING PROCESS
def getrequest(parms=len(sys.argv)):
	if parms < 3:
		print("No data recieved")

	else:
		raw_data = sys.argv[1]
		data = raw_data.replace('{', '')
		data = data.replace('}', '')
		data = data.replace(' ', '')
		data = data.replace("'", "")
		data = data.split(',')
		newdata = []
		for i in data:
			temp = i.split(':')
			newdata.append(temp)
		request = {}
		for items in newdata:
			request[items[0]] = items[1]

	return request