from pytube import YouTube
from moviepy.editor import *
# Made by Stallion
# Made by Stallion
# Made by Stallion
# Made by Stallion
def linkgir():
    global link
    link = str(input("Link'i Girin : "))
# Made by Stallion
linkgir();
#link'i al
yt = YouTube(link)
#Çözünürlük seç / Video Seç
ys = yt.streams.get_highest_resolution()
# Made by Stallion
print("Video'nun başlığı bu mu : ", yt.title)
yn = str(input("y/n : "))
# Made by Stallion
if(yn == "y"):
    name = str(input("Dosya adı (özel karakter yasak) : "))
    print("İndirme başlatıldı")
    ys.download(filename=f'{name}.mp4')
    print("İndirildi")
elif(yn == "n"):
    print("İndirme iptal edidi başa dönülüyor")
    linkgir()
else:
    print("Ne dediğinizi anlayamadım başa dönülüyor")
    linkgir()
# Made by Stallion
# Made by Stallion
# Made by Stallion
# Made by Stallion
mp3 = str(input("Mp3'e dönüşsünmü (y/n) : "))
# Made by Stallion
if(mp3 == "y"):
    print("Dönüştürülüyor")
    mp4_file = name+".mp4"
    mp3_file = name+".mp3"
    videoclip = VideoFileClip(mp4_file)
 # Made by Stallion
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
 # Made by Stallion
    audioclip.close()
    videoclip.close()
    print("Dönüştürüldü")
elif(mp3 == "n"):
    print("İşlem iptal edildi")
else:
    print("Komut anlaşılamadı lütfen tekrar deneyin!")
# Made by Stallion
# Made by Stallion
