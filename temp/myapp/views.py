from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
def contactus(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        msg=request.POST.get('message')
        
        data={
            'name':name,
            'email':email,
            'phone':phone,                                                                                                                   
            'message':msg
        }
        print(data)
        message='''
        name={}
        email={}
        phone={}
        message={}
        ''' .format(data['name'],data['email'],data['phone'],data['message'])
        send_mail('ENQUIRY',message,'',
                  ['envvumarketing2@gmail.com'])
        html="<html><body><hr><hr>THANKYOU</body></html>"
        return HttpResponse('html')
    return render(request,'base.html')
        