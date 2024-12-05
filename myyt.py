from googleapiclient.discovery import build

# Replace with your YouTube Data API key
API_KEY = "AIzaSyAo9Pa7He2o0KoZww0HGVoOQYTpJ_43Mjw"

# Initialize the YouTube API client
youtube = build("youtube", "v3", developerKey=API_KEY)

def get_channel_videos(channel_id):
    """
    Fetches all video IDs and titles from a given YouTube channel.
    """
    videos = []
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50,
        order="date",
        type="video"
    )
    
    while request:
        response = request.execute()
        for item in response["items"]:
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            videos.append((video_id, title))
        
        # Check if there's a next page
        request = youtube.search().list_next(request, response)
    
    return videos

def main():
    # Replace with the desired channel ID
    channel_id = "UCPdZb69InsnBkLkDPHska8g"  # Example: Google Developers channel ID
    
    print(f"Fetching videos from channel: {channel_id}...")
    videos = get_channel_videos(channel_id)
    
    print(f"Found {len(videos)} videos:")
    for idx, (video_id, title) in enumerate(videos, 1):
        print(f"{idx}. {title} (https://www.youtube.com/watch?v={video_id})")

if __name__ == "__main__":
    main()
