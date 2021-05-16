from django.forms import ModelForm
from .models import meme

class MemeForm(ModelForm):
    class Meta:
        model = meme
        fields = ['name', 'caption', 'url']