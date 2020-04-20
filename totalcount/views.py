from django.shortcuts import render
import requests
import json
from django.http import HttpResponse
# Create your views here.
def index(request):
    response = requests.get('https://api.covid19india.org/state_district_wise.json')
    item = json.loads(response.content.decode('utf-8'))
    # return HttpResponse(item['Tamil Nadu']['districtData'])

    return render(request,'index.html',{'data':item.items()})