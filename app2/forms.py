from dataclasses import fields
from django import forms
from app2.models import Book, Employee

# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length = 200)
#     last_name = forms.CharField(max_length= 200)
#     roll_number = forms.IntegerField(help_text='Enter 6 digit roll number')
#     password = forms.CharField(widget = forms.PasswordInput())

# print(StudentForm())

class StudentForm(forms.ModelForm):
    # is_file = forms.FileField()
    class Meta:
        model = Book
        fields = "__all__"
        # fields = ('name', 'price') # case 1
        # fields = "__all__" # case 2
        # exclude = ("qty", )

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'