from youtube_transcript_api import YouTubeTranscriptApi


def get_transcript(video_id):
    try:
        ytt = YouTubeTranscriptApi()

        # Priority order: English → Hindi → Bangla
        transcript_list = ytt.fetch(
            video_id,
            languages=["en", "hi", "bn"]
        )

        transcript = " ".join(chunk.text for chunk in transcript_list)

        return transcript

    except Exception as e:
        print(f"Transcript Error: {e}")
        return None