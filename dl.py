#Created by KasRoudra
#Github . : https://github.com/KasRoudra2
#Facebook : https://facebook.com/KasRoudra
#Messenger: https://m.me/KasRoudra
import os, sys
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
purple="\033[0;35m"
cyan="\033[0;36m"
blue="\033[1;34m"
input_url=""
primary_url=""
mid_url=""
final_url=""
os.system("clear")
print(blue)
os.system("figlet KasDrive")
print(yellow+"Disclaimer:"+green+"You can generate direct download link for audio, video, ebooks and files except executable files such as exe, apk and large files more than 100MB. And you also need access to the file of link!\n")
def output(url):
     print(purple+"\nThe desired link is:\n"+blue+url)
     print(green+"\nOpening link in browser...")
     os.system('''xdg-open --view "'''+url+'''"''')
     mainfunc(input_url)
def vieditdelete(primary_url):
    if (primary_url.find("/view") != -1 ):
        mid_url=primary_url.replace("/view", "")
        uspdelete(mid_url)
    if (primary_url.find("/edit") != -1 ):
        mid_url=primary_url.replace("/edit", "")
        uspdelete(mid_url)
    output(primary_url)
def uspdelete(mid_url):
    if (mid_url.find('?usp=sharing') != -1):
        final_url=mid_url.replace("?usp=sharing", "")
        output(final_url)
    if (mid_url.find('?usp=drivesdk') != -1):
        final_url=mid_url.replace("?usp=drivesdk", "")
        output(final_url)
    output(mid_url)
def default_delete(input_url):
    if (input_url.find("/file/d") != -1):
        primary_url=input_url.replace("file/d/", "uc?export=download&id=")
        vieditdelete(primary_url)
def userdelete(input_url,n):
    user={"0","1","2","3","4","5","6","7","8","9"}
    for n in user:
        if (input_url.find(('/u/')+n) != -1):
            primary_url=input_url.replace("file/u/"+n+"/d/", "uc?export=download&id=")
            vieditdelete(primary_url)
def mainfunc(input_url):
    print(yellow+"Enter the google drive link:")
    input_url=input(">>>"+green)
    if (input_url.find('drive.google.com/file') != -1):
        loop= False
        default_delete(input_url)
        n=0
        while(n<10):
            userdelete(input_url,n)
            n+=1
    if (input_url==""):
            exit()
    else:
        print(red+"Sorry! This is not a google drive file url!\nPress enter to exit!\n")
        mainfunc(input_url)
mainfunc(input_url)