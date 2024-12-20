# Nova: AI-Powered Personal Assistant

Nova is an intelligent voice assistant powered by Google Generative AI (Gemini 1.5) and other powerful Python libraries. Nova can recognize speech, respond with natural language, interact with web browsers, open local applications, and provide contextual assistance.

## Features
- **Voice Commands: Interact with Nova using voice inputs.**
- **Google Generative AI Integration: Engage in intelligent, context-aware conversations.**
- **Open Websites and Applications: Quickly access frequently used websites and desktop applications.**
- **Real-Time Clock: Ask Nova for the current time.**
- **Custom AI Prompts: Generate text responses using AI and save them locally.**
- **Streamlined Chat History: Reset or continue chat seamlessly.**

## Prerequisites
1. Python 3.9 or higher
2. Virtual Environment (.venv) activated
3. API key for Google Generative AI (Gemini)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Sahil9822/Nova-AI-Powered-Personal-Assistant.git
   cd Nova-AI-Powered-Personal-Assistant
   ```
2. Create and activate the virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your Google Generative AI API key:
   - Open config.py.
   - Replace "" with your API key from Google Generative AI.

## Usage
1. Run the main program:
   ```bash
   python main.py
   ```
2. Speak commands like:
   - "Open YouTube"
   - "What is the time?"
   - "Nova quit" to exit the program.
3. For testing AI interactions, run aitest.py:
   ```bash
   python aitest.py
   ```

## Folder Structure
```bash
nova/
├── main.py            # Main script to run Nova
├── aitest.py          # Script to test AI functionalities
├── config.py          # Configuration file for API keys
├── Genai/             # Folder where AI responses are saved
├── requirements.txt   # List of required Python libraries
├── .venv/             # Virtual environment
└── README.md          # Project documentation
```

## Requirements
Here’s a list of libraries used:
- speech_recognition: For speech-to-text functionality.
- pyttsx3: For text-to-speech synthesis.
- google-generativeai: To interact with Google Generative AI (Gemini).
- webbrowser: To open URLs.
- os: To interact with the operating system.
- datetime: To fetch the current time.

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Future Enhancements
- Add More Commands: Expand Nova's functionality.
- Integrate Other APIs: Enable interaction with APIs like OpenWeather or Google Maps.
- Improve Error Handling: Refine command recognition and error responses.
