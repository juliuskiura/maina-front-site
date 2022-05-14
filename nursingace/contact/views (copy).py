import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponseRedirect
from requests import JSONDecodeError
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AssignmentMessageSerializer
from products.serializers import OrderFileSerializer
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

@api_view(['GET'])
def message_list(request, slug):
    order_assignment = get_object_or_404(OrderItem, slug=slug)
    instances = order_assignment.assign_messages.all().order_by('-date_sent')    
    serializer = AssignmentMessageSerializer(instances, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_message(request):  
    file_resp =[]
    usr = User.objects.get(id=request.user.id)  
    assignment = get_object_or_404(OrderItem, slug=request.data['assigmentId'])  
    if request.data.get('file'):
        file = request.data.pop('file')        
        for file_obj in request.FILES.getlist('file'):
            data ={
                'order': assignment,
                'file': file_obj,
            }
            
            file_serializer = OrderFileSerializer(data=data)
            if file_serializer.is_valid(raise_exception=True):
                file_serializer.save()
            file_resp.append(file_serializer.data)
            
    
    
    request_data = request.data.copy() 
    request_data['assignment'] = assignment

    serializer = AssignmentMessageSerializer(data=request_data)    
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=usr, assignment=assignment)

    data_resp = serializer.data.copy()

    data_resp['file_data'] = file_resp

        
   
    return Response(data_resp)

@api_view(['POST'])
def update_message(request, id):
    instance = AssignmentMessage.objects.get(id=id)
    usr = User.objects.get(id=1)
    serializer = AssignmentMessageSerializer(instance=instance, data=request.data)      
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=usr)
    
    

    return Response(serializer.data)

@api_view(['POST'])
def delete_message(request, id):
    instance = AssignmentMessage.objects.get(id=id)
    instance.delete()

    return Response('Item successfully deleted')


@api_view(['POST'])
def mark_ms_read(request): 
    data=request.data
    slug = data['messageID']
    instance = get_object_or_404(AssignmentMessage, slug=slug)
    instance.read_status=True
    instance.save()
    unread_messages = AssignmentMessage.objects.filter(read_status=False).exclude(user=request.user)
 

    return Response({'unread':AssignmentMessageSerializer(unread_messages, many=True).data,'marked':True, 'total': unread_messages.count()})