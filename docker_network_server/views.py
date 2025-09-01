from django.http import HttpResponse
from time import time
import httpx

def greet(request):
	return HttpResponse('Hello from Server 👋')

def internal_api(request):
	# response = httpx.get('http://172.17.0.3:5000') # HERE THIS IP IS THE IP ALLOTED TO THE CONTAINER RUNNING THIS FLASK SERVER PRESENT IN THE DEFAULT BRIDGE NETWORK
	response = httpx.get('http://flask-container:5000') # THIS WILL AUTOMATICALLY RESOLVE TO THE IP OF THE FLASK-CONTAINER THAT IS ALLOCATED BY OUT CUSTOM CREATED NETWORK INSIDE OF WHICH BOTH THE DJANGO , FLASK CONTAINERS ARE RUNNING
	print(response.status_code)
	return HttpResponse(response.text)

def read_file(requset):
	try:
		file_to_check = open('/app/data/data.txt' , 'rt')
	except Exception as e:
		print(e)
		return HttpResponse('Cannot open the specified file' , 500)
	else:
		return HttpResponse(file_to_check.read())

def edit_file(request):
	try:
		file_to_write = open('/app/data/data.txt' , 'a')
	except Exception as e:
		print(e)
		return HttpResponse('Something went wrong while opening the file' , 500)
	else:
		file_to_write.write(str(time()))
		return HttpResponse('Edited the file successfully' , 200)