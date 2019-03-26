from apiclient.discovery import build

class Youtube:

	def busca(self, api_key, busca):
		youtube = build('youtube', 'v3', developerKey=api_key)
		req = youtube.search().list(part='snippet', q='noticias',type='video',maxResults=50)
		res = req.execute()
		return (res['items'])




