#coding=utf-8
import os
import time
import requests
import base64
from os import listdir
from os.path import isfile, isdir, join
r_path = './pdfs'
files = listdir(r_path)
filesList = []
for f in files:
	fullpath = join(r_path, f)
	if isfile(fullpath):
		filesList.append(fullpath)

def file2b64(filepath):
	# print(filepath.replace('./pdfs\\',''))
	file = open(filepath, 'rb')
	file_content = file.read()
	# print(file_content)
	b64 = base64.b64encode(file_content)
	return b64.decode()

if __name__ =='__main__':
	for i in filesList:
		# print(i)
		b64 = file2b64(i)
		queryjson = {
			'title': str(i).replace('./pdfs\\','').replace(',','|'),
			'content': b64
		}
		r = requests.post('http://192.168.57.20:58088', json=queryjson) #Server for BPSS-PVS
		paperStatus = r.content.decode()
		queryjson = {
		"fileHash":"fileHash",
		"hash":"hash",
		"authorList":"authorList",
		"status":paperStatus,
		"coAuthor":"coAuthor",
		"reqTime":"reqTime",
		"mail":"mail",
		"orcid":"orcid",
		"reqTimeForTest":time.time()*1000,
		}
		r = requests.post('http://192.168.57.30:8082/add', json=queryjson) #Server for BPSS-WebPage