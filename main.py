from summer1 import stream_n_download
from create_wav import create_wav
from summer2 import speech_to_text
from summer3 import summarize

result ='first run and no output'
def main(url):
    stream_n_download(url)
    create_wav()
    transcript = speech_to_text()
    result = summarize(transcript)
    return result

  
