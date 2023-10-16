from django.shortcuts import render,redirect
from .models import ContactManager
from .serializers import ContactSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import ContactManager

# Create your views here.
def home(request):
    return render(request,'home.html')

def create_contact(request):
    if request.method=="POST":
        id=request.POST["id"]
        first_name=request.POST["firstname"]
        last_name=request.POST["lastname"]
        email=request.POST["email"]
        phone_number=request.POST["phone_number"]
        notes=request.POST["notes"]
        contact=ContactManager(id=id,first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,
                               notes=notes)
        contact.save()
        return redirect('list_contact')
    return render(request,'create.html')

def list_contact(request):
    contacts=ContactManager.objects.all()
    context={
        "contacts":contacts
    }
    return render(request,'list_contact.html',context)

def update(request,id):
    if request.method=="POST":
        contact=ContactManager.objects.get(id=id)
        contact.id=request.POST["id"]
        contact.first_name=request.POST["firstname"]
        contact.last_name=request.POST["lastname"]
        contact.email=request.POST["email"]
        contact.phone_number=request.POST["phone_number"]
        contact.notes=request.POST["notes"]
        contact.save()
        return redirect('list_contact')
    else:
        contact=ContactManager.objects.get(id=id)
        context={
            "contact":contact
        }
        return render(request,'update.html',context)

def delete(request,id):
    contact=ContactManager.objects.get(id=id)
    contact.delete()
    return redirect("home")


@api_view(["GET","POST"])
def get_contact_list(request):
    if request.method=="GET":
        contact=ContactManager.objects.all()
        serializer=ContactSerializer(contact,many=True)
        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
def contact_details(request,id):
    try:
        contact=ContactManager.objects.get(id=id)
    except ContactManager.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer=ContactSerializer(contact)
        return Response(serializer.data)
    
    elif request.method=="PUT":
        serializer=ContactSerializer(contact,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    elif request.method=="DELETE":
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    









