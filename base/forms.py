from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):  # creating a form but as a class
    class Meta:  # modelform is a ready made class with meta as a subclass
        model = Room  # what model we are making the form for
        fields = '__all__'  # fields from the model we want the user to fill in
