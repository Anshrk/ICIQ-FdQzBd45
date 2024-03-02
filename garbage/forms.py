from django.forms import ModelForm
from .models import Garbage

class GarbageForm(ModelForm):
    class Meta:
        model = Garbage
        exclude = ["cleaned", "cleaned_by"]