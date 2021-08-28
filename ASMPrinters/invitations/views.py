from django.shortcuts import redirect, render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from django.http.response import JsonResponse
import json
import requests


from invitations.models import customer
from invitations.serializer import cusSerializer
# Create your views here.
#User Interfaces
def home(request):
    return render (request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def orderbook(request):
    return render(request, 'orderbook.html')
     
  
def signup(request):
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

def userpage(request):
    return render(request, 'userpage.html')

def visit(request):
    return render(request, '1visiting.html')

def ordersts(request):
    return render(request, 'ordersts.html') 


    


#Backend
@csrf_exempt
def addC(request):
    if(request.method == 'POST'):
        # customer = JSONParser().parse(request)
        cus_serialize = cusSerializer(data = request.POST)
        if(cus_serialize.is_valid()):
            cus_serialize.save()
            #return JsonResponse(cus_serialize.data, status = status.HTTP_200_OK)
            return redirect(userpage)

        else:
            return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST )

    else:
        return HttpResponse("Signup Customer")

@csrf_exempt
def viewall(request):
    if(request.method == 'GET'):
        cus = customer.objects.all()
        cus_serializer = cusSerializer(cus, many=True)
        return JsonResponse(cus_serializer.data, safe=False)

    else:
        return JsonResponse("View customer details")

@csrf_exempt
def getSingle(request, fetchid):
    try:
        cus = customer.objects.get(phone = fetchid)
        if(request.method == 'GET'):
            cus_serialize = cusSerializer(cus)
            return JsonResponse(cus_serialize.data, safe = False, status = status.HTTP_200_OK)

        if(request.method == 'DELETE'):
            cus.delete()
            return HttpResponse("The customer details has been removed", status = status.HTTP_204_NO_CONTENT)

        if(request.method == 'PUT'):
            cusdata = JSONParser().parse(request)
            cus_serialize = cusSerializer(cus, data= cusdata)
            if(cus_serialize.is_valid()):
                cus_serialize.save()
                return JsonResponse(cus_serialize.data, status = status.HTTP_200_OK )

    except:
        return HttpResponse("Invalid data", status = status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def search(request):
    try:
        getemail = request.POST.get("email")
        getOrdersts= customer.objects.filter( email=getemail)
        email_serialize= cusSerializer(getOrdersts, many=True)
        #return JsonResponse(email_serialize.data, status = status.HTTP_200_OK )
        return render(request, 'ordersts.html', {"data":email_serialize.data})

    except:
        return HttpResponse("Invalid")
        

@csrf_exempt
def profile(request):
    try:
        getemail = request.POST.get("email")
        getprofile= customer.objects.filter( email=getemail)
        email_serialize= cusSerializer(getprofile, many=True)
        #return JsonResponse(email_serialize.data, status = status.HTTP_200_OK )
        return render(request, 'profile.html', {"data":email_serialize.data})

    except:
        return HttpResponse("Invalid")

@csrf_exempt
def updatepro(request):
    try:
        getphone= request.POST.get("phone")
        getupdate = customer.objects.filter(phone = getphone)
        phone_serialize = cusSerializer(getupdate, many=True)
        return render(request,"update.html",{"data":phone_serialize.data})
    except customer.DoesNotExist:
        return HttpResponse("Invalid Page", status= status.HTTP_404_NOT_FOUND)
    except:
         return HttpResponse("Something went wrong")

@csrf_exempt
def updateact(request):
    getnewName = request.POST.get("newName")
    getnewAdd = request.POST.get("newAdd")
    getnewemail= request.POST.get("newEmail")
    getnewPh = request.POST.get("newPhone")
    getnewPass = request.POST.get("newPass")
    getnewCPass = request.POST.get("newCpass")
    mydata = {"name":getnewName, "add":getnewAdd, "email":getnewemail, "phone":getnewPh,"password":getnewPass,"cnfrmpass":getnewCPass}
    jdata = json.dumps(mydata)

    apilink= "http://127.0.0.1:8000/asm/getone/"+getnewPh
    requests.put(apilink, data=jdata)
    return HttpResponse("Profile has been updated successfully")

@csrf_exempt
def  delete(request):
    try:
        getphone= request.POST.get("phone")
        getP = customer.objects.filter(phone = getphone)
        phone_serialize =cusSerializer(getP, many=True)
        #return JsonResponse(phone_serialize.data, safe=False, status=status.HTTP_200_OK)
        return render(request, "delpro.html", {"data":phone_serialize.data})
    except customer.DoesNotExist:
        return HttpResponse("Invalid content", status=status.HTTP_404_NOT_FOUND)

    except:
        return HttpResponse("Something went wrong")

@csrf_exempt
def delact(request):
    getnewPhone =request.POST.get("newPhone")
    APIlink ="http://127.0.0.1:8000/asm/getone/"+getnewPhone
    requests.delete(APIlink)
    return HttpResponse("The profile has been deleted successfully")





    
   
    



   






        
    

    