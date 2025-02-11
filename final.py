import os
from transformers import pipeline
import time
import pyttsx3
from vosk import Model, KaldiRecognizer
import pyaudio
import json

model = Model(r"/media/suriya/Softwares/Udownloads/vosk-model-en-in-0.5")
recognizer = KaldiRecognizer(model, 16000)

# Initialize PyAudio once
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()


# Function to read text from a file
def read_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ""
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return ""

# Function to answer questions using a pre-trained model
def answer_question_from_text(question, context):
    qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
    result = qa_pipeline(question=question, context=context)
    return result['answer']

def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# Function to listen for a question
def listen():
    timeout_duration = 5
    last_active_time = time.time()
    
    while True:
        try:
            data = stream.read(4096, exception_on_overflow=False)
            print("Listening...")
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                result_dict = json.loads(result)
                MyText = result_dict.get("text", "")
                print("Recognized text:", MyText)
                if MyText == "exit" or MyText == "the exit":
                    return "exit"
                if MyText == "come again":
                    SpeakText(x)
                    return listen()
                return MyText  # Send the text to another function
                last_active_time = time.time()  # Reset the timer

        except OSError as e:
            print(f"Error reading audio data: {e}")
            SpeakText("There was an error processing the audio. Please try again.")
            continue  # Retry listening in case of an error
    
    restart_message = "Pardon..."
    print(restart_message)
    SpeakText(restart_message)

def is_out_of_context(question, context):
    # Simple check: if question contains any word from context, assume it's in context
    question_words = question.lower().split()
    context_words = context.lower().split()
    
    for word in question_words:
        if word in context_words:
            return False
    
    return True

# Main function to orchestrate the process
def main():
    while True:
        SpeakText("Select Chapter")
        qr = listen()
        if qr == "exit":
            break
        if "chapter one" == qr.lower():
            file_path = "/home/suriya/Downloads/perform.txt"
            context = read_text_from_file(file_path)
            SpeakText("chapter 1 selected..")
            break
        elif "chapter two" == qr.lower():
            file_path = "/home/suriya/Downloads/txt2.txt"
            context = read_text_from_file(file_path)
            SpeakText("chapter 2 selected..")
            break
        elif "chapter three" == qr.lower():
            file_path = "/home/suriya/Downloads/txt3.txt"
            context = read_text_from_file(file_path)
            SpeakText("chapter 3 selected..")
            break
        else:
            SpeakText("Select Chapter..")
    
    if context:
        while True:
            question = listen()
            if question == "exit":
                break
            if question:
                if not question.lower().startswith("beta"):
                    #SpeakText("I'm sorry, I don't have information on that.")
                    continue  # Skip answering if "beta" is not mentioned
                
                # Remove the "beta" prefix before answering
                command = question[5:].strip()
                
                if not command:
                    SpeakText("Hi, How can I help you?")
                    continue  # Prompt user for a question if "beta" is followed by nothing

                if command.lower() == "read the chapter":
                    SpeakText(context)
                    global x
                    x=context;
                    continue  # Read the entire chapter and wait for the next command

                if is_out_of_context(command, context):
                    SpeakText("I'm sorry, I don't have information on that.")
                    continue  # Skip answering if the question is out of context
                
                answer = answer_question_from_text(command, context)
                x = answer
                print(f"Answer: {answer}")
                SpeakText(x)

if __name__ == "__main__":
    main()

# Cleanup
stream.stop_stream()
stream.close()
mic.terminate()
