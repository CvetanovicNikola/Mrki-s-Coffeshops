from django import forms
from .models import Coffeeshop



class CoffeeshopForm(forms.ModelForm):
    class Meta:
        model = Coffeeshop
        fields = ["name", "address", "smoking", "description",
                  "image1", "image2", "image3", "votes"]
