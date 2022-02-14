import youtube_dl

def extract():
    video_link=input("Enter youtube video link: ")

    info = youtube_dl.YoutubeDL().extract_info(

        url = video_link, download = False

    )
    file = f"{info['title']}.mp3"
    options={

        'format':"bestaudio/best",
        "keepvideo":False,
        "outtmpl":file,

    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete.")

if __name__=='__main__':
    extract()
