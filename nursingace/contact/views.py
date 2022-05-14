from email import message
from django.shortcuts import redirect, render
import json
from. forms import ModelContactForm
from .serializers import SubscriberSerializer
from .models import Subscriber
from django.contrib import messages
from sitemanager.models import SiteManagerSetting
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def contact_form_view(request):
    sitesetting_complete = False
    try:  
        site_manager =SiteManagerSetting.objects.all()[0]
        address = site_manager.address
        location = site_manager.location
        phone = site_manager.phone
        email = site_manager.email   
        contact_response = site_manager.email_thank_you_text
        if address and location and phone and email and contact_response:
            sitesetting_complete = True
    except:
        pass
   
       
    form = ModelContactForm() 

    if request.method == 'POST':
        form = ModelContactForm(request.POST)
        if form.is_valid():
            instance = form.save()
            visitor = instance.full_name
            messages.success(request, f'Hi, {visitor}. {contact_response}')
            
            return redirect('contactform')
    context = {
        'site_manager':site_manager,
        'form': form,
    }
    if sitesetting_complete:   
        return render(request, 'home/contact-us.html', context)


@api_view(['GET'])
def subs(request):
    serializer = SubscriberSerializer(data=request.data)
    instances = Subscriber.objects.all()
    serializer = SubscriberSerializer(instances, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def subscribe(request): 
    print('SOmething==', request)
    serializer = SubscriberSerializer(data=request.data)    
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        data_resp = {'data':'Thank you for your subscription'}
    return Response(data_resp)

def csrf_failure(request, reason=""):
    # Do stuff here.
    messages.error(request, 'Abnormal traffic coming from your browser prevented the form from saving. Reload the form and try again')
    return redirect(request.path_info)  