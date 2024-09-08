import cv2 as cv
import base64
from openai import OpenAI
from dotenv import load_dotenv
import os
from elevenlabs import VoiceSettings, save
from elevenlabs.client import ElevenLabs



load_dotenv('secrets.env')



def process_video(video_path):
    # Open the video file
    video = cv.VideoCapture(video_path)

    # Get the frames per second (fps) and total frame count
    fps = video.get(cv.CAP_PROP_FPS)
    total_frames = int(video.get(cv.CAP_PROP_FRAME_COUNT))

    # Calculate duration in seconds
    video_duration = total_frames / fps

    print(f"Video duration: {video_duration:.2f} seconds")

    # Estimate tokens needed based on video duration
    # This estimation helps in setting an appropriate max_tokens parameter for the AI model
    words_per_second = 150 / 60
    estimated_words = int(video_duration * words_per_second)
    estimated_tokens = int(estimated_words * 1.5)

    # List to store base64 encoded frames
    base64Frames = []

    # Read the video file frame by frame
    while video.isOpened():
        success, frame = video.read()
        if not success:
            break
        # Encode each frame as a JPEG image
        _, buffer = cv.imencode(".jpg", frame)
        # Convert the image to base64 and add to the list
        base64Frames.append(base64.b64encode(buffer).decode("utf-8"))

    # Release the video capture object
    video.release()
    print(len(base64Frames), "frames read.")
    
    return base64Frames, estimated_tokens



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

def generate_narration(base64Frames, estimated_tokens, chosen_style):
    # Define the prompt structure for the AI
    PROMPT_MESSAGES = [
        {
            "role": "user",
            "content": [
                NARRATION_STYLES[chosen_style]["prompt"],
            ],
        },
    ]

    # Add every 50th frame to the prompt
    # This reduces the number of frames sent to the AI model while still representing the video content
    for frame in base64Frames[0::50]:
        PROMPT_MESSAGES[0]["content"].append({"image": frame, "resize": 768})

    # Set parameters for the API call
    params = {
        "model": "gpt-4o",  # Specify the AI model to use
        "messages": PROMPT_MESSAGES,
        "max_tokens": estimated_tokens,  # Limit the response length to match the video duration
    }

    # Load the OpenAI API key from the environment file
    OPEN_AI_KEY = os.environ['OPEN_AI_API_KEY']

    # Initialize the OpenAI client with the API key
    client = OpenAI(api_key=OPEN_AI_KEY)

    # Make the API call to generate the narration
    result = client.chat.completions.create(**params)

    script = result.choices[0].message.content
    print(script)
    return script




def text_to_speech(text, chosen_style):
    ELEVENLABS_API_KEY = os.environ["ELEVENLABS_API_KEY"]
    client = ElevenLabs(
        api_key=ELEVENLABS_API_KEY,
    )

    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id=NARRATION_STYLES[chosen_style]["voice_id"],
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2_5",
        voice_settings=VoiceSettings(
            stability=0.7,
            similarity_boost=0.5,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Save the audio to a file
    save(response, "output.mp3")

    print("Audio file saved as output.mp3")


def video_to_narrate(video_path, chosen_style):
    base64Frames, estimated_tokens = process_video(video_path)
    script = generate_narration(base64Frames, estimated_tokens, chosen_style)
    text_to_speech(script, chosen_style)

