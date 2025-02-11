# Voice Assistant with Text Reading and Question Answering

## Overview

This project implements a voice assistant capable of reading text from files and answering questions based on the content of those files using Natural Language Processing (NLP) techniques. The program listens for voice commands, processes them, and then responds either by reading text from a file or by providing answers to questions related to the content.

The voice assistant uses Vosk for speech recognition, Hugging Face's transformers library for question answering, and pyttsx3 for text-to-speech functionality.

## Features

- **Speech Recognition**: The assistant listens to voice commands using Vosk and processes audio input in real-time.
- **Text-to-Speech**: The assistant responds with spoken text using pyttsx3.
- **Question Answering**: The assistant can answer questions based on the content of a selected chapter, using a pre-trained transformer model (`bert-large-uncased-whole-word-masking-finetuned-squad`).
- **Chapter Selection**: The user can select one of three available chapters, after which the assistant will read the content and answer questions.
- **Customizable Text Files**: The content can be customized by changing the text files used for the chapters.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Required Libraries

1. `transformers`: To load and use the pre-trained question-answering model.
2. `pyttsx3`: For text-to-speech functionality.
3. `vosk`: For speech recognition.
4. `pyaudio`: To interface with the microphone for real-time speech capture.

You can install the necessary libraries with the following command:

```bash
pip install transformers pyttsx3 vosk pyaudio
```

Additionally, make sure you have the correct Vosk model downloaded (for example, `vosk-model-en-in-0.5`) and provide the correct path in the program.

## Usage

### 1. Setting up the Vosk Model

Download the appropriate Vosk model from the [Vosk Models](https://alphacephei.com/vosk/models) page. In this example, the model path is set as `"dir"/vosk-model-en-in-0.5`. Update this path in the script to match where you've downloaded your model.

### 2. Running the Program

To start the program, run the Python script:

```bash
python assistant.py
```

Once the program is running:

1. The assistant will prompt you to **Select Chapter**. You can choose from "Chapter One", "Chapter Two", or "Chapter Three".
2. After selecting a chapter, the assistant will read the content from the corresponding text file.
3. You can then ask questions about the chapter. The assistant will use the question-answering model to answer your queries based on the content.
4. To exit the program, simply say "exit".

### Commands

- **Select a Chapter**: Say one of the following to choose a chapter:
  - "Chapter One"
  - "Chapter Two"
  - "Chapter Three"
  
- **Ask a Question**: Once a chapter is selected, you can ask questions related to the chapter, such as:
  - "Beta, what is the main theme of the chapter?"
  - "Beta, who are the main characters in the chapter?"

  The assistant will then provide an answer based on the selected chapter's content.

- **Exit the Program**: Say "exit" to stop the assistant.

### Example Interaction

```
Assistant: Select Chapter
User: Chapter One
Assistant: Chapter 1 selected..
User: Beta, what is the main idea of the chapter?
Assistant: The main idea of Chapter One is...
User: exit
```

### Note:
- The assistant is designed to respond only to questions that include the prefix **"Beta,"** to trigger the question-answering functionality.
- If the assistant doesn’t have enough information, it will respond with "I’m sorry, I don't have information on that."

## Files

- `assistant.py`: The main Python script for the assistant.
- `vosk-model-en-in-0.5`: The Vosk model for speech recognition (you must download this separately).
- `"dir"/perform.txt`, `"dir"/txt2.txt`, `"dir"/txt3.txt`: Sample text files containing chapter contents (you can replace these with your own files).

## Cleanup

The program automatically cleans up and closes the microphone stream after exiting.

## Troubleshooting

- **Microphone not working**: Make sure your microphone is properly connected and configured.
- **Model errors**: Ensure the Vosk model is correctly installed and the path is set in the code.
- **Missing libraries**: Double-check that you have installed all required libraries.

---
