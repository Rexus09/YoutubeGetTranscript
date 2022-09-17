from apiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi

#Para obtener tu API KEY sigue los primeros pasos de este tutorial 
# https://www.pragnakalp.com/automate-youtube-video-transcription-python/
try:
    api_key = "Pega aquí tu clave API" #Paste your API key in here
    youtube = build('youtube', 'v3', developerKey=api_key)
except:
    print("To obtain your API KEY follow this tutorial\nhttps://www.pragnakalp.com/automate-youtube-video-transcription-python/")
    exit()

url = input("Video URL:\t")
video_id = url.split("v=")[1]
file = open("transcript.docx","w")
try:
    #Try to get the Spanish transcript
    responses = YouTubeTranscriptApi.get_transcript(
        video_id, languages=['es'])
    #write the transcript to the file
    for response in responses:
        file.write(response['text'])
except:
    try:
        #Try to get English transcript
        responses = YouTubeTranscriptApi.get_transcript(
        video_id, languages=['en'])
        for response in responses:
            file.write(response['text'])
    except:
        print("Error :(\nCheck the URL and API key")
        file.close()
file.close()
