
from gtts import gTTS

mytext = 'welcome to python.instruction'
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("welcome.mp3")
  
