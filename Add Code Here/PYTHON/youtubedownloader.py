from pytube import YouTube

def downloadd(link):
    videoYout = yt(link)
    videoYout = videoYout.streams.get_highest_resolution()
    try:
        videoYout.download()
    except:
        print("Your Link is Can't Download a Video")
    print("Download Complete")


link = input("Enter Youtube URL: ")
downloadd(link)
