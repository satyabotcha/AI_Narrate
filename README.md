# Narrate

A Python-based project for narrating videos using famous character voices. This package allows you to narrate either uploaded videos or live webcam footage using the voices of Homer Simpson, Morpheus (from The Matrix), or David Attenborough.

This package uses OpenAI for video analysis and script generation, and Eleven Labs for voice narration.

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



## Contributing

Contributions are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

Copyright (c) 2024 Satya Botcha

For more information, visit the [Narrate repository](https://github.com/satyabotcha/Narrate).