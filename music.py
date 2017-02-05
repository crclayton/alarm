import pygame, os, random, subprocess
from datetime import datetime, timedelta

music_directory = r"/home/crclayton/Music"
timeout         = 30 # minutes
fade_span       =  5 # minutes
max_volume      = 40 # %
current_volume  =  0 # %

pygame.init()
pygame.mixer.init()

def start():
    end = datetime.now() + timedelta(minutes = timeout)
    while datetime.now() < end:
        print("Timeout in: " + str(end - datetime.now()))
        mp3 = get_random_file(music_directory, "mp3")
        print("Volume: " + str(current_volume) + ", starting: " + mp3)
        play_song(mp3)
        fade_song()

def get_random_file(dir, type):
    files = [os.path.join(path, filename)
         for path, dirs, files in os.walk(dir)
         for filename in files
         if filename.endswith(type)]
    return random.choice(files)

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
