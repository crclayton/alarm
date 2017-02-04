import threading, music.py, internet.py

if __name__ == "__main__":
	threads = [threading.Thread(target=music.start),
		   threading.Thread(target=internet.start)]
	for thread in threads:
		thread.start()
		thread.join()
	
