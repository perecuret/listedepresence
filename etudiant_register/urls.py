from django.urls import path
from . import views

urlpatterns = [
    path('', views.etudiant_form,name='etudiant_insert'), # get and post req. for insert operation
    path('<int:id>/', views.etudiant_form,name='etudiant_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.etudiant_delete,name='etudiant_delete'),
    path('list/',views.etudiant_list,name='etudiant_list') # get req. to retrieve and display all records
]