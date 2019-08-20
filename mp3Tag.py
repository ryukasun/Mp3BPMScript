#Python project to iterate through a library of music and add them to a collection and checks if the song has something in the bpm slot
#Process flow would be
#Gets a list of MP3 Filenames from the given directory. otentially add a check that will have a regex command that only checks for files with mp3 filename
#Checks if there's anything in the BPM field of the code, if there is than 



import glob, os, pprint
from mutagen.easyid3 import EasyID3, ID3
from mutagen.mp3 import MP3


def main():
    directoryName = input("Please input the directory: ")
    #os.chdir(C:\Users\ryukasun\Music\Lindy Music\Brooks Prumo Orchestra)
    #for file in glob.glob("*.mp3"):
     #   print(file)
     
    musicNames = []
    print(EasyID3.valid_keys.keys())
    for root, dirs, files in os.walk(directoryName):
        for file in files:
            if file.endswith('.mp3'):
                fullpath = os.path.join(root, file) 
                
                audio = MP3(fullpath, ID3=EasyID3)
                #pprint.pprint(audio)
                #print(audio["title"])
                #pprint.pprint(audio)
                newbpm = ' '.join(audio["bpm"])
                if newbpm != "0":
                    newtitle =' '.join(audio["title"])
                    if "bpm:" in newtitle:
                        print("Already fixed title")
                    else:
                        audio["title"] = newtitle +" - bpm: " + newbpm
                    audio.save()                    
                    
                     
                    #print(newbpm)
                #else:
                    #print("There is no bpm for this song")
                
                #audio["title"] = "Bakers Bounce"
                #audio["bpm"] = "186"
                #newbpm = ' '.join(audio["bpm"])
                #newtitle =' '.join(audio["title"])
                #audio["title"] = newtitle +" - bpm: " + newbpm
                #audio.save()
               # musicNames.append(fullpath)
                
    # print(musicNames)
    
    #for name in musicNames:
    #    audio = ID3(name)
        
               
                

if __name__ == "__main__":
    main()