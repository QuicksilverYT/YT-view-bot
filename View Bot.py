#Things you need
import webbrowser, time
import random
url = input("Enter the URL of the video you want to get views ")
#YT VIEW CODE
for i in range(int(input("How much views do you want to get ?"))):
    print("running video for {} times".format(i))  #This will show that how many times the video is running
    webbrowser.open_new(url)
    time.sleep(random.randint(3, 10))

#last print
print("  ")
print("  ")
time.sleep(2)
print("Hope you found it useful ")
print("  ")
time.sleep(0.5)
print("If you did not receive your views ,please wait for 10 to 20 minutes")
print("Made By QuicksilverYT")
