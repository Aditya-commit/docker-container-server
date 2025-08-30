from django.http import HttpResponse
import httpx

def greet(request):
	return HttpResponse('Hello from Server 👋')

def internal_api(request):
	# response = httpx.get('http://172.17.0.3:5000') # HERE THIS IP IS THE IP ALLOTED TO THE CONTAINER RUNNING THIS FLASK SERVER PRESENT IN THE DEFAULT BRIDGE NETWORK
	response = httpx.get('http://flask-container:5000') # THIS WILL AUTOMATICALLY RESOLVE TO THE IP OF THE FLASK-CONTAINER THAT IS ALLOCATED BY OUT CUSTOM CREATED NETWORK INSIDE OF WHICH BOTH THE DJANGO , FLASK CONTAINERS ARE RUNNING
	print(response.status_code)
	return HttpResponse(response.text)