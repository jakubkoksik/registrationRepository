from re import template
from django.shortcuts import redirect, render, reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from registrationApp.forms import NewPersonForm
from registrationApp.models import Person
from django.shortcuts import get_object_or_404

# Create your views here.
class HomeView(TemplateView):
    template_name = 'registrationApp/home.html'

class NewPewsonView(CreateView):
    model = Person
    template_name = 'registrationApp/newPerson.html'
    redirect_field_name = 'registrationApp/home.html'
    form_class = NewPersonForm

class DoneView(TemplateView):
    template_name = 'registrationApp/done.html'

class PersonListView(ListView):
    template_name = 'registrationApp/personList.html'
    model = Person
    context_object_name = 'people'

    def get_queryset(self):
        return super().get_queryset()

class PersonDetailView(DetailView):
    model = Person
    template_name = 'registrationApp/personDetail.html'
    context_object_name = 'person'

class DeletePersonView(DeleteView):
    model = Person
    template_name = 'registrationApp/personDeleteConfirm.html'
    success_url = reverse_lazy('personList')

def changeWorkStatus(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.changeWorkStatus()
    return redirect('personDetail', pk = pk)


# def personDetail(request, pk):
#     people = get_object_or_404(Person, pk = pk)
#     return render(request, 'registrationApp/postDetail.html', {'people': people})