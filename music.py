import pygame, os, random, subprocess
from datetime import datetime, timedelta

music_directory = r"/home/crclayton/Music"
timeout         = 30 # minutes
max_volume      = 40 # %
current_volume  = 0  # %

pygame.init()
pygame.mixer.init()

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
        current_volume += 0.5
        pygame.time.Clock().tick(1)
    
def start():
    end = datetime.now() + timedelta(minutes = timeout)
    while datetime.now() < end:
	try:
            print("Timeout in: " + str(end - datetime.now()))
            mp3 = get_random_file(music_directory, "mp3")

            print("Song starting: " + mp3)        
            play_song(mp3)
	    fade_song()
        except KeyboardInterrupt:
            pass # skip to the next song


if __name__ == "__main__":
    start()

