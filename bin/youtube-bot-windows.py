import time,webbrowser,os

url = str(input("Enter your video url in ->\"url here \"<-  : "))
n = input("Enter refresh rate(seconds) : ")
brow = input("Enter your default browser in ->\"browser here \"<-  : ")
while (1):
    os.system("TASKKILL /F /IM " + brow + ".exe")
    time.sleep(int(n))
    webbrowser.open(url)
    print('Successfully Viewd')
