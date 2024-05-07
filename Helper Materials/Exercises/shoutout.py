import win32com.client as wincom

voice = wincom.Dispatch("SAPI.SpVoice")
l = ['Pulkit' , 'Jagrit' , 'Rajat' , 'CPU']
for i in l:
    voice.Speak(f'Hi, how are you {i}?')

