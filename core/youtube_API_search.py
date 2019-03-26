from apiclient.discovery import build

class Youtube:

	####### conexão com API #######
	def conexao(self, api_key):
		self.youtube = build('youtube', 'v3', developerKey=api_key) 


	####### Get videos por termo de busca #######
	def busca_video(self, busca):
		req = self.youtube.search().list(part='snippet', q=busca ,type='video',maxResults=50)
		res = req.execute()
		return (res['items'])


	####### Get Videos de um canal especifico #######
	def canal_video(self, canal_id):
      # get Uploads playlist id
	    res = self.youtube.channels().list(id=canal_id, part='contentDetails').execute()
	    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
	    
	    videos = []
	    next_page_token = None
	    
	    while 1:
	        res = self.youtube.playlistItems().list(playlistId=playlist_id, 
	                                           part='snippet', 
	                                           maxResults=50,
	                                           pageToken=next_page_token).execute()
	        videos += res['items']
	        next_page_token = res.get('nextPageToken')
	        
	        if next_page_token is None:
	            break
	    
	    return videos







