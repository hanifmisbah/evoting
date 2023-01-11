from django import forms

from .models import *

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ['owner']
        # widgets = {
        #     'agenda':forms.Select(attrs={'status':'readonly'})
        # }
        
    # def __init__(self, *args, **kwargs):
    #     super(PollForm, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['agenda'].widget.attrs['readonly'] = True
