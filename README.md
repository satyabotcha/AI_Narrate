# From Homer to Morpheus: The Ultimate AI Voice Overkill

A Python-based project for narrating videos using famous character voices. This package allows you to narrate either uploaded videos or live webcam footage using the voices of Homer Simpson, Morpheus (from The Matrix), or David Attenborough.

This package uses OpenAI for video analysis and script generation, and Eleven Labs for voice narration.


## Demo

https://github.com/user-attachments/assets/887f3f7f-16c0-4365-a7dc-e455eb2ffc1f




**Disclaimer:** The creator of this software does not take any responsibility for any copyright infringement that may occur through its use. Users are responsible for ensuring they have the necessary rights and permissions for any content they use or create with this tool.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/satyabotcha/Narrate.git
   cd Narrate
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install required packages:
   ```
   pip install -r requirements.txt
   ```

5. Create a `secrets.env` file in the root directory with the following API keys:
   ```
   OPEN_AI_API_KEY=your_openai_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   DAVID_ATTENBOROUGH_VOICE_ID=your_david_attenborough_voice_id_here
   MORPHEUS_VOICE_ID=your_morpheus_voice_id_here
   HOMER_SIMPSON_VOICE_ID=your_homer_simpson_voice_id_here
   ```
   Replace the placeholder values with your actual API keys and voice IDs from OpenAI and Eleven Labs.

## Usage

The project consists of three main Python files:

- `main.py`: The entry point of the application
- `narration.py`: Handles narration functionality
- `webcam.py`: Manages webcam operations

To run the project, execute: 

python main.py

## How to add new narration character

To add a new narration character:

1. Obtain a new voice ID from Eleven Labs:
   - Go to [Eleven Labs](https://elevenlabs.io/) and navigate to "Voices"
   - Select "Add voice" and choose "Instant voice cloning"
   - Upload a 1-minute voice recording and name it
   - Click "Add voice"
   - Visit the [Eleven Labs API documentation](https://elevenlabs.io/docs/api-reference/get-voices)
   - In the "Get voices" function, add your API key to the header and send the request
   - Find your new voice recording in the returned list of voices and note its `voice_id`

2. Add the new voice ID to your `secrets.env` file:
   ```
   NEW_CHARACTER_VOICE_ID=your_new_character_voice_id_here
   ```

3. Update the `narration_styles.py` file to include the new character:
   - Add a new entry to the `NARRATION_STYLES` dictionary:
     ```python
     NARRATION_STYLES = {
         # ... existing entries ...
         "new_character": {
             "prompt": """
     These are frames from a video.
     Generate a [New Character] style narration for this video.
     [Add specific instructions for the character's style]
     Only return the actual narration that will be read, no other text or comments.
     """,
             "voice_id": os.environ["NEW_CHARACTER_VOICE_ID"]
         }
     }
     ```
   - Replace `"new_character"` with the actual name of your character
   - Customize the prompt to match the character's style

4. Test the new character by running `python main.py` and selecting the new character from the available options.

## Contributing

Contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Copyright (c) 2024 Satya Botcha

For more information, visit the [Narrate repository](https://github.com/satyabotcha/Narrate).
