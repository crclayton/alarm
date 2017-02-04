import webbrowser

links = [ "https://www.reddit.com/",
	  "https://github.com/",
	  "http://stackoverflow.com/",
	  "https://webmail.alumni.ubc.ca/",
	  "https://www.youtube.com/dashboard?o=U" ]

def start():
	for link in links:
		webbrowser.open(link)

if __name__ == "__main__":
	start()


