from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, UpdateView, FormView, ListView
from core.youtube_API_search import Youtube
import json

class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		api_key = 'AIzaSyDkHQY3gk-rt614-tAm6_u1DMY_nk9nyg8'
		youtube = Youtube()
		busca = youtube.busca(api_key, 'linguagem python')
		context['buscas'] = busca
		return context





