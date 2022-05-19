import requests
import csv
domains=list()
fp=open("domains.csv")
urls= csv.reader(fp)
for i in urls:
	domains.append(i[0])
workingdomains=list()
for i in domains:
	try:
		resp=requests.get(i)
	except:
		continue
	else:
		workingdomains.append(i)
print workingdomains