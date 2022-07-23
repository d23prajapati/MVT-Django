from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def employee(request):
    name=""
    email=""
    contact=""
    
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        print(name, email, contact)
        context = {
            'name':name,
            'email':email,
            'contact':contact,   
        }
        return render(request, 'details.html',context) 

    return render(request, 'employee.html')

def details(request):
    return render(request, 'details.html')