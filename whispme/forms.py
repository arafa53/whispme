from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    content = forms.CharField(label='content', max_length=100, required=False, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))



    class Meta:
        model = Image
        fields = ('caption','image','content')
        






        