from django import forms
from .models import employ


class empform(forms.ModelForm):
    name = forms.CharField(max_length=225, required=True)
    mobile_no = forms.CharField(max_length=225, required=True)
    email = forms.EmailField(max_length=225, required=True)
    course = forms.CharField(max_length=225, required=True)

    class Meta:
        model = employ
        fields = {'name','mobile_no','email','course'}
