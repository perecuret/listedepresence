from django.shortcuts import render, redirect
from .forms import EtudiantForm
from .models import Etudiant

# Create your views here.


def etudiant_list(request):
    context = {'etudiant_list': Etudiant.objects.all()}
    return render(request, "etudiant_register/etudiant_list.html", context)


def etudiant_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EtudiantForm()
        else:
            etudiant = Etudiant.objects.get(pk=id)
            form = EtudiantForm(instance=etudiant)
        return render(request, "etudiant_register/etudiant_form.html", {'form': form})
    else:
        if id == 0:
            form = EtudiantForm(request.POST)
        else:
            etudiant = Etudiant.objects.get(pk=id)
            form = EtudiantForm(request.POST,instance= etudiant)
        if form.is_valid():
            form.save()
        return redirect('/list')


def etudiant_delete(request,id):
    etudiant = Etudiant.objects.get(pk=id)
    etudiant.delete()
    return redirect('/list')

