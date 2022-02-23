from . import views
from django.urls import path

urlpatterns = [
    path('', views.Employee_form, name='employee_insert'),
    path('<int:id>/', views.Employee_form, name='employee_update'),
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
    path('list/',views.Employee_list,name='Employee_list'),
]

# urlpatterns = [
#      #get and post req for insert operations
#     #get and post req. for update operation
#     path('list/', views.employee_list, name ='employee_list'),#get req. to retrive and display all records
#     path('delete/<int:id>/',views.employee_delete,name='employee_delete'),


# ]