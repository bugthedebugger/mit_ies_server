#! /usr/bin/python3
import os

def getFile():
	participants = """
	Aakriti Ghimire, 
	Aashish Bhandari,
	Aayush Gadal,
	Aditiya Mishra,
	Anmol Karna,
	Anubhav Sharma,
	Anusha Kiran Shukla,
	Ayush Jha,
	Ayush Kuman Chaudhary,
	Belina Sainju,
	Bibhuti Poudyal,
	Binaya Raj Paudyal,
	Jayshree Rathi,
	Nikesh Subedi,
	Nrepesh Joshi,
	Oskar Krishna Shrestha,
	Pratima Niroula,
	Preety Sitikhu,
	Rajan Bastakoti,
	Sagar Subedi,
	Shivam Chaudhary,
	Shria Rajbhandari,
	Shronim Tiwari,
	Sujan Shrestha,
	Vishad Pokharel,
	Yogesh Budhathoki"""

	raw_data = participants.split(',')
	temp = []

	for items in raw_data:
		temp.append(items.replace('\n', '').replace('\t', ''))
		#print(temp)

	participant_files = {}

	for items in temp:
		participant_files[items] = items.replace(' ','').lower()

	#for files in participant_files.values():
		#os.mkdir('/home/bprayush/Documents/IOT/webtest/uploads/'+files)

	#print(participant_files)
	return participant_files

#getFile()