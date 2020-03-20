from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView

class IngredientsCreateFormView(CreateView):
	model = None
	template_name = 'ingredients_create_form.html'
	
class IngredientsDetailView(DetailView):
	model = None
	
class IngredientsListView(ListView):
	model = None

class IngredientsUpdateFormView(UpdateView):
	model = None
	template_name = 'ingredients_update_form.html'

