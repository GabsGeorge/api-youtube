from django.db import models

from apiclient.discovery import build

class Youtube:

	def busca(self, api_key, busca):

		youtube = build('youtube', 'v3', developerKey=api_key)

		req = youtube.search().list(part='snippet', q='racionais',type='video',maxResults=50)

		res = req.execute()

		return print(res['items'])
