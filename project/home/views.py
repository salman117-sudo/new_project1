# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('password')
        print("Name is : ", name, "\nPassword is : ",password)
    return render(request, 'index1.html')
