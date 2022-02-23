from .models import Employee
from django.forms import ModelForm

class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields='FullName','mobile','Emp_code','position'
        labels={'FullName':'Name','Emp_code':'Employee ID','mobile':'Phone Number'}
