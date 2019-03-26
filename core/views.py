from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, UpdateView, FormView, ListView

from core.youtube_API_search import Youtube # <<<<<< caminho para a biblioteca
import json

class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		youtube = Youtube()
		
		youtube.conexao('AIzaSyDkHQY3gk-rt614-tAm6_u1DMY_nk9nyg8') # chave api
		busca_video = youtube.busca('linguagem python') # termo de busca

		context['buscas'] = busca_video
		return context





