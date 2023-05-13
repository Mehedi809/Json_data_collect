from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def home(request):
    form = requests.get('https://jsonplaceholder.typicode.com/users')
    json_forms = form.json()
    return render(request, 'index.html', {'form_json':json_forms})

def clean(request):
    return HttpResponse('Alhamdulillah')