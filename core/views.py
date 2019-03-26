from django.shortcuts import render
from django.views.generic import View, TemplateView, CreateView, UpdateView, FormView, ListView

from core.youtube_API_search import Youtube # <<<<<< caminho para a biblioteca
import json

class IndexView(TemplateView):
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		youtube = Youtube()
		
		youtube.conexao('AIzaSyCXzyKtit3GjGynx81PW9JdTqLhdmCKX2M') # chave api
		
		busca_videos = youtube.busca_video('noticias') # Termo de busca
		canal_videos = youtube.canal_video('UCkUq-s6z57uJFUFBvZIVTyg')# Id do canal


		context['busca_videos'] = busca_videos
		context['canal_videos'] = canal_videos
		return context





