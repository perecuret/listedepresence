from django import forms
from .models import Etudiant


class EtudiantForm(forms.ModelForm):

    class Meta:
        model = Etudiant
        fields = ('name','firstname','mobile','email','evenement')
        labels = {
            'name':'Nom',
            'firstname':'Prenom',
            'email':'Email',
            'mobile':'Numero de Telephone'
        }

    def __init__(self, *args, **kwargs):
        super(EtudiantForm,self).__init__(*args, **kwargs)
        self.fields['evenement'].empty_label = "Select"
    
