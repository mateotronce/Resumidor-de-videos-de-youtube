from youtube_transcript_api import YouTubeTranscriptApi 

def transcript_url(url):
    url = url.split(sep = "=")
    url = url[1]
    # assigning srt variable with the list 
    # of dictionaries obtained by the get_transcript() function
    srt = YouTubeTranscriptApi.get_transcript(url,languages=['es', 'en'])

    texto  = ""
    for text in srt:
        texto = texto + " " + text["text"]


    return texto

