import json
from django.http import HttpResponse, JsonResponse
import requests
# Create your views here.




def get_price(request):
    if request.method == 'POST':
        
        try:
            managementUrl = 'https://appnursing.cannyva.com/assignments/front/fetch-price/'  
            body = json.loads(request.body)
            data = requests.get(managementUrl, data=json.dumps(body)).json()
          
            return JsonResponse(data)
         
        except:
            return ''
           
      