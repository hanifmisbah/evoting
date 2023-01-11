from django import forms

from .models import *

class KandidatForm(forms.ModelForm):
    class Meta:
        model = Kandidat
        exclude = ['owner']
        widgets = {
            'nama': forms.TextInput(attrs={'style': 'border-color:#1AB394; border-radius:10px;'}),
            'jk': forms.Select(attrs={'style': 'width:220px; height:30px; border-color:#1AB394; border-radius:10px;'}),
            'domisili': forms.TextInput(attrs={'style': 'border-color:#1AB394; border-radius:10px;'}),
            'nim': forms.NumberInput(attrs={'style': 'border-color:#1AB394; border-radius:10px;'}),
            'jurusan': forms.TextInput(attrs={'style': 'width:220px; border-color:#1AB394; border-radius:10px;'}),
            'tgl_lahir': forms.DateInput(format='%Y-%m-%d', attrs={'type':'date','style': 'width:220px; border-color:#1AB394; border-radius:10px;'}),
            'tpt_lahir': forms.TextInput(attrs={'style': 'width:220px; border-color:#1AB394; border-radius:10px;'}),
            'no_wa': forms.NumberInput(attrs={'style': 'border-color:#1AB394; border-radius:10px;'}),
            'email': forms.EmailInput(attrs={'style': 'border-color:#1AB394; border-radius:10px;'}),
            'agenda': forms.Select(attrs={'style': 'border-color:#1AB394; border-radius:10px;'}),
            'visi': forms.Textarea(attrs={'style': 'height:150px; border-color:#1AB394; border-radius:10px;'}),
            'misi': forms.Textarea(attrs={'style': 'height:150px; border-color:#1AB394; border-radius:10px;'}),
            # 'vote': forms.NumberInput(attrs={'style': 'border-color:#1AB394; border-radius:10px;'}),
        }
        
    def __init__(self, *args, **kwargs):
        super(KandidatForm, self).__init__(*args, **kwargs)
        self.fields['nama'].widget.attrs['class'] = 'form-control'
        self.fields['domisili'].widget.attrs['class'] = 'form-control'
        self.fields['nim'].widget.attrs['class'] = 'form-control'
        self.fields['jurusan'].widget.attrs['class'] = 'form-control'
        self.fields['tgl_lahir'].widget.attrs['class'] = 'form-control'
        self.fields['tpt_lahir'].widget.attrs['class'] = 'form-control'
        self.fields['no_wa'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['agenda'].widget.attrs['class'] = 'form-control'
        self.fields['visi'].widget.attrs['class'] = 'form-control'
        self.fields['misi'].widget.attrs['class'] = 'form-control'
            
        
class PemilihanForm(forms.ModelForm):
    class Meta:
        model = Agenda
        exclude = ['owner']
        widgets = {
            'judul': forms.TextInput(attrs={'style': 'height:100px; border-color:#1AB394; border-radius:10px;'}),
            'waktu_awal': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type':'datetime-local','style': 'width:220px; border-color:#1AB394; border-radius:10px;'}),
            'waktu_akhir': forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type':'datetime-local','style': 'width:220px; border-color:#1AB394; border-radius:10px;'}),
            'status': forms.Select(attrs={'style': 'width:220px; border-color:#1AB394; border-radius:10px;'})
        }

    def __init__(self, *args, **kwargs):
        super(PemilihanForm, self).__init__(*args, **kwargs)
        self.fields['status'].widget.attrs.update({'class' : 'form-control'})
        self.fields['waktu_awal'].widget.attrs.update({'class' : 'form-control'})
        self.fields['waktu_akhir'].widget.attrs.update({'class' : 'form-control'})
        self.fields['judul'].widget.attrs.update({'class' : 'form-control'})