from django import forms
from matplotlib import widgets
from registrationApp.models import Person

class NewPersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('firstName', 'lastName', 'age', 'sex', 'profession', 'email', 'phone')

    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields['firstName'].widget.attrs.update({'class': 'form-control'})
       self.fields['lastName'].widget.attrs.update({'class':'form-control'})
       self.fields['age'].widget.attrs.update({'class':'form-control'})
       self.fields['sex'].widget.attrs.update({'class':'form-control'})
       self.fields['profession'].widget.attrs.update({'class':'form-control'})
       self.fields['email'].widget.attrs.update({'class':'form-control'})
       self.fields['phone'].widget.attrs.update({'class':'form-control'})