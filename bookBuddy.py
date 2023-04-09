# importing required modules
from sumy.summarizers.luhn import LuhnSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from PyPDF2 import PdfReader
from gtts import gTTS
from io import BytesIO
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from pydub import AudioSegment
from pydub.playback import play
from gptKaam import *




def playAudio(audioBytes):
    audioBytes.seek(0) # move the BytesIO object pointer to the start
    audio = AudioSegment.from_file(audioBytes, format='mp3')
    play(audio)


total_content = ""


def getText(file_path, total_content):
    reader = PdfReader(file_path)
    val = len(reader.pages)
    for i in range(val):
        page = reader._get_page(i)
        page_content = page.extract_text()
        total_content += page_content

    return val, total_content


val, text = getText("gptBook.pdf", "")
summary=" "
parser = PlaintextParser(text, Tokenizer('english'))
summarizer_1 = LuhnSummarizer()
summary_1 = summarizer_1(parser.document, 10)
for sentence in summary_1:
    print(sentence)
    summary += str(sentence)


print("printing summary")
print(summary)



def sumToAudio(summary):
    audio = gTTS(summary )
    af = BytesIO()
    audio.write_to_fp(af)
    return af

audio = sumToAudio(summary )

print(type(audio))

playAudio(audio)
