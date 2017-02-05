import pygame, os, random, subprocess, mutagen.easyid3
from datetime import datetime, timedelta

music_directory = r"/home/crclayton/Music"
excluded_genres = ["Hardcore", "Punk", "Podcast", "Various", "Rap", "Hip-Hop"]
timeout         = 30 # minutes
fade_span       =  5 # minutes
max_volume      = 40 # %
current_volume  = 30 # %

pygame.init()
pygame.mixer.init()

def start():
    end = datetime.now() + timedelta(minutes = timeout)
    while datetime.now() < end:
        print("Timeout:", end - datetime.now())
        mp3 = get_song()
        print("Volume:", current_volume)
        play_song(mp3)
        fade_song()

def get_random_file(dir, type):
    files = [os.path.join(path, filename)
         for path, dirs, files in os.walk(dir)
         for filename in files
         if filename.endswith(type)]
    return random.choice(files)

def get_song():
    skip = True
    while skip:
        f = get_random_file(music_directory, "mp3")
        mp3 = mutagen.easyid3.EasyID3(f)
        genre = v(mp3, "genre")
        skip = any([g in genre for g in excluded_genres])
    print("Music:", v(mp3, "title"), v(mp3, "artist"), v(mp3, "album"), v(mp3,"genre"))
    return f 

def v(o, k):
    return o.get(k, [""])[0]

def set_volume_to(percent):
    subprocess.call(["amixer", "-D", "pulse", "sset", "Master", 
       str(percent) + "%", "stdout=devnull"])

def play_song(song_file):
    pygame.mixer.music.load(song_file)
    pygame.mixer.music.play()

def fade_song():
    global current_volume
    while pygame.mixer.music.get_busy():
        set_volume_to(min(current_volume, max_volume))
        current_volume += max_volume/(60.0*fade_span)
        pygame.time.Clock().tick(1)

if __name__ == "__main__":
    start()
