from django import forms
from .models import Department, Position, Employee

# -------- form example -------------
class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)
    phone_no = forms.IntegerField(label="Phone No.")


class EmployeeModelForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'

        widgets = {
            'department' : forms.Select(attrs={'class': 'form-select'}),
            'position' : forms.Select(attrs={'class': 'form-select'}),
            'full_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic' : forms.FileInput(attrs={'class': 'form-control'}),
            'email_id' : forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_no' : forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.Textarea(attrs={'class': 'form-control'}),
            'year_of_experience' : forms.TextInput(attrs={'class': 'form-control'}),
        }
