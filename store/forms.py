'''from django import forms
from .models import *

class Computer(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ('book',)

class Electronics(forms.ModelForm):
    class Meta:
        model = Electronics
        fields = ('book',)
    
class Electrical(forms.ModelForm):
    class Meta:
        model = Electrical
        fields = ('book',)

class  Mechanical (forms.ModelForm):
    class Meta:
        model = Mechanical
        fields = ('book',)
'''