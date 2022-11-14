from pytube import YouTube
from moviepy.editor import *
# made by stallion
def linkgir():
    global link
    link = str(input("Link'i Girin : "))

linkgir();
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()

print("Video'nun başlığı bu mu :", yt.title)
yn = str(input("y/n : "))

if(yn == "y"):
    name = str(input("Dosya adı (özel karakter yasak) : "))
    print("İndirme başlatıldı") 
    ys.download(r'C:\Users\yiit2\Documents\Editing', filename=f'{name}.mp4')
    print("İndirildi")
elif(yn == "n"):
    print("İndirme iptal edidi başa dönülüyor")
    linkgir()
else:
    print("Ne dediğinizi anlayamadım başa dönülüyor")
    linkgir()

# made by stallion
# made by stallion# made by stallion
# made by stallion
mp3 = str(input("Mp3'e dönüşsünmü (y/n) : "))

if(mp3 == "y"):
    print("Dönüştürülüyor")
    mp4_file = r'mp4ün ineceği klasör'+"\\"+name+".mp4"
    mp3_file = r'mp3ün olduğu klasör'+"\\"+name+".mp3"
    videoclip = VideoFileClip(mp4_file)
 
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
 
    audioclip.close()
    videoclip.close()
    print("Dönüştürüldü")
elif(mp3 == "n"):
    print("İşlem iptal edildi")
else:
    print("Komut anlaşılamadı lütfen tekrar deneyin!")

