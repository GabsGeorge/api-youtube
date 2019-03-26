from apiclient.discovery import build

class Youtube:

	def conexao(self, api_key):
		self.youtube = build('youtube', 'v3', developerKey=api_key)
	
	def busca(self, busca):
		req = self.youtube.search().list(part='snippet', q='noticias',type='video',maxResults=50)
		res = req.execute()
		return (res['items'])






