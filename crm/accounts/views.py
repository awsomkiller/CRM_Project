from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == 'POST':
        fullName = request.POST["fullName"]
        contactNo = int(request.POST['contactNo']) 
        panNo = int(request.POST['panNo'])
        govIdtype = request.POST["govIdtype"]
        govId = request.POST["govId"]
        mentor = request.POST["mentor"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        serviceType = request.POST["serviceType"]
        readCheck = request.POST["readCheck"]
        modifyCheck = request.POST["modifyCheck"]
        deleteCheck = request.POST["deleteCheck"]


