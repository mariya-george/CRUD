
from django.shortcuts import redirect, render

from .models import Employee


from .forms import EmployeeForm

#Create your views here.
def Employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request,'Employee_list.html',context)

def Employee_form(request,id=0):
    if request.method=="GET":
        if id==0:
            form=EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance= employee)
        return render(request,"Employee_form.html", {'k':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid(): 
            form.save()
        return redirect('/list')  

def employee_delete(request,id):
    employee=Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/list')

