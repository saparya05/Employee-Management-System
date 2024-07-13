from django.shortcuts import render,HttpResponse, get_object_or_404, redirect
from .forms import NameForm, EmployeeModelForm
from django.contrib import messages
from .models import Employee


# Create your views here.
def index(request):

    return render(request, 'index.html')

# ------ example of from api ----------
# def add_employee(request):

#     if request.method == "POST":
        
#         formobj = NameForm(request.POST)
        
#         if formobj.is_valid():
#             # write logic here to save data in model
#             return HttpResponse('Your form submited !')

#     else:
#         formobj = NameForm()
#     # context = {'formobj':formobj, }
#     return render(request, 'add_emp.html', {'formobj':formobj})


# ------ example of modelfrom api ----------
def add_employee(request):

    if request.method == "POST":
        
        formobj = EmployeeModelForm(request.POST, request.FILES)
        
        if formobj.is_valid():
            formobj.save()
            
            messages.success(request, "Employee Added successfully.")

    else:
        formobj = EmployeeModelForm()
   
    return render(request, 'add_emp.html', {'formobj':formobj})

def view_employee(request):

    all_emp = Employee.objects.all()

    return render(request, 'view_emp.html', {'all_emps':all_emp})


def update_employee(request, pk): #pk = primary key

    emp_to_update = get_object_or_404(Employee, pk=pk)

    if request.method == "POST":
        
        formobj = EmployeeModelForm(request.POST, request.FILES, instance = emp_to_update)
        
        if formobj.is_valid():
            formobj.save()
            
            messages.success(request, "Employee updated successfully.")

    else:
        formobj = EmployeeModelForm(instance = emp_to_update)
   
    return render(request, 'update_emp.html', {'formobj':formobj})

def delete_employee(request, pk): #pk = primary key
    emp_to_delete = get_object_or_404(Employee, pk=pk)
    emp_to_delete.delete()
    messages.success(request, "Employee deleted successfully.")
    return redirect('/view-employee/')

    