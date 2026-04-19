from googleapiclient.discovery import build

API_KEY = "AIzaSyDPOdjvvj4Ksis5lEWoYUoIB2qWBoBEeko"

youtube = build('youtube', 'v3', developerKey=API_KEY)


def extract_video_id(url):
    return url.split("v=")[-1]


def get_comments(video_id):
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )

    response = request.execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments
