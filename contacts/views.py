from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

from contacts.models import Contact

# Create your views here.


class ContactListView(generic.ListView):
    model=Contact
    paginate_by=5
    
    def  get_queryset(self) -> QuerySet[Any]:
        q=self.request.GET.get('q')
        if q:
            return Contact.objects.filter(name__icontains=q)
        return super().get_queryset()
    
    
class ContactCreateView(generic.CreateView):
    model=Contact
    fields=['avatar','name','email','birth','phone']
    success_url='/'
    
    
class ContactUpdateView(generic.UpdateView):
    model=Contact
    fields=['avatar','name','email','birth','phone']
    success_url='/'
    
class ContactDeleteView(generic.DeleteView):
    model=Contact
    success_url='/'
    