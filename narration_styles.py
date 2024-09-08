import os
from dotenv import load_dotenv

load_dotenv('secrets.env')
NARRATION_STYLES = {
    "david_attenborough": {
        "prompt": """
These are frames from a video. 
Generate a David attenborough style documentary narration for this video. 
Make it funny, engaging and saracastic.
Only return the actual narration that will be read, no other text or comments.
""",
        "voice_id": os.environ["DAVID_ATTENBOROUGH_VOICE_ID"]
    },
    "morpheus": {
        "prompt": """
These are frames from a video. 
Generate a Morpheus style story narration from the Matrix for this video. 
Make the script engaging, inspirational and thought provoking. Just like Morpheus in the matrix.
Only return the actual narration that will be read, no other text or comments.
""",
        "voice_id": os.environ["MORPHEUS_VOICE_ID"]
    },
    "homer_simpson": {
        "prompt": """
These are frames from a video.
Generate a Homer Simpson style narration for this video.
Make it lazy, confused, and filled with references to donuts and beer.
Include his catchphrases and typical misunderstandings.
Only return the actual narration that will be read, no other text or comments.
""",
        "voice_id": os.environ["HOMER_SIMPSON_VOICE_ID"]
    }
}