from django.shortcuts import render
from .models import Details
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def reg_page(request):
     return render(request,'form.html')

#def login(request):
#      if request.method=='POST':
#            return HttpResponse('<h1> Welcome</h1>')

def render_login(request):
     return render(request,'login.html')

def submit(request):
    if request.method=='POST':
          emp_name=request.POST['emp_name']
          emp_reg_no=request.POST['emp_reg_no']
          shift_choice=request.POST['shift_choice']
          password=request.POST['password']
          instance=Details(emp_name=emp_name,emp_reg_no=emp_reg_no,shift_choice=shift_choice,password=password)
          instance.save()
    return render(request,'welcome.html')  
      
def success(request):
     if request.method=='POST':
          name=request.POST['emp_name']
          passw=request.POST['password']
          reg=request.POST['emp_reg_no']
          og=Details.objects.get(emp_reg_no=reg)
          if og.emp_name==name and og.password==passw:
             return render(request,'success.html')
          else:
             return render(request,'error.html')    

def det(request):
     if request.method=='POST':
          reg=request.POST['emp_reg_no']
          pass_one=request.POST['password_one']
          pass_two=request.POST['password_two']
          val=Details.objects.get(emp_reg_no=reg)
          if pass_one==pass_two:
               val.password=pass_one
               val.save()
               return render(request,'confirmation.html')
          else:
               return HttpResponse("<h1> Error ! </h1>")
  




def reg_prompt(request):
     return render(request,'prompt.html')



        

