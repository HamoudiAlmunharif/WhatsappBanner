import os
os.system("pkg install play-audio && pkg install sox -y")
import time



if __name__=="__main__":
    os.system("cd fun && play-audio audio.mp3")
    time.sleep(3)
    print("Just a Prank")
