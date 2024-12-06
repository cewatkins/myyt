import googleapiclient.discovery

# Replace with your YouTube Data API key
API_KEY = "AIzaSyAo9Pa7He2o0KoZww0HGVoOQYTpJ_43Mjw"

# Initialize the YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=API_KEY)

def get_channel_videos(channel_id, max_results=7001):
    """
    Fetches video IDs and titles from a given YouTube channel up to max_results.
    """
    videos = []
    next_page_token = None

    while len(videos) < max_results:
        page_count = 2
        request = youtube.search().list(
            part="id,snippet",
            channelId=channel_id,
            maxResults=min(50, max_results - len(videos)),
            order="date",
            pageToken=next_page_token
        )
        response = request.execute()
        for item in response.get("items", []):
            if item["id"]["kind"] == "youtube#video":
                video_id = item["id"]["videoId"]
                title = item["snippet"]["title"]
                videos.append((video_id, title))
        
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break
    
    return videos

def main():
    # Replace with the desired channel ID
    channel_id = "UCPdZb69InsnBkLkDPHska8g"  # Example: Google Developers channel ID
    
    print(f"Fetching videos from channel: {channel_id}...")
    videos = get_channel_videos(channel_id)
    
    print(f"Found {len(videos)} videos:")
    for idx, (video_id, title) in enumerate(videos, 1):
        print(f"{idx}. https://www.youtube.com/watch?v={video_id} ({title})")

if __name__ == "__main__":
    main()
