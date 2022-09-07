from django.forms import ChoiceField, ModelForm, RadioSelect
from matplotlib import style
from .models import Kandidat, Agenda

class KandidatForm(ModelForm):
    jenis_kelamin = [
        ('Laki-Laki', 'Laki-Laki'),
        ('Perempuan', 'Perempuan'),
    ]

    jk = ChoiceField(choices=jenis_kelamin, widget=RadioSelect())
    class Meta:
        model = Kandidat
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(KandidatForm, self).__init__(*args, **kwargs)
        # self.fields['nama'].widget.attrs['class'] = 'form-control'
        # self.fields['jk'].widget.attrs['class'] = 'form-control'
        self.fields['jurusan'].widget.attrs['class'] = 'form-control'
        # self.fields['nim'].widget.attrs['class'] = 'form-control'
        # self.fields['tgl_lahir'].widget.attrs['class'] = 'form-control'
        # self.fields['tpt_lahir'].widget.attrs['class'] = 'form-control'
        # self.fields['no_wa'].widget.attrs['class'] = 'form-control'
        # self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['agenda'].widget.attrs['class'] = 'form-control'
        # self.fields['visi'].widget.attrs['class'] = 'form-control'
        # self.fields['misi'].widget.attrs['class'] = 'form-control'
        
class PemilihanForm(ModelForm):
    status = [
        ('aktif', 'aktif'),
        ('tidak aktif', 'tidak aktif'),
    ]

    status = ChoiceField(choices=status, widget=RadioSelect())

    class Meta:
        model = Agenda
        fields = '__all__'
        # exclude = ['kandidat']

    # def __init__(self, *args, **kwargs):
        # super(PemilihanForm, self).__init__(*args, **kwargs)
        # self.fields['status'].widget.attrs.update({'class' : 'form-control'})
        # self.fields['waktu'].widget.attrs.update({'class' : 'form-control'})