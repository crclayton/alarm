import webbrowser, subprocess

links = [ 
    "https://www.reddit.com/",
    "https://github.com/",
    "http://stackoverflow.com/",
    "https://webmail.alumni.ubc.ca/",
    "https://www.youtube.com/dashboard?o=U",
    "https://play.google.com/music/listen?authuser#/now",
    #"http://www.cbc.ca/listen/live/radio1/vancouver" 
]

def start():
    # turn the monitor on
    subprocess.call(["xset", "dpms", "force", "on"])

    # open links
    for link in links: 
        webbrowser.open(link)

if __name__ == "__main__":
    start()


