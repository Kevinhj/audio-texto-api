import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from src.utilities.file_names import get_audio_file_names
from src.configs import directory_paths


# Process the calls to text and apply sentiment analysis
def process_call_recording():
    audio_folder = ["informacion", "matricula", "cobro"]

    # loop over the audio folders to get the file names
    for folder in audio_folder:
        audios = get_audio_file_names(folder)
        print("============================================")
        print(f"Procesando llamadas de la carpeta: {folder}")
        print(f"Lista de audios encontrados: {audios}")

        # loop over the audios under a given folder
        for audio in audios:
            text = convert_call_to_text(folder, audio)
            # Analisis de Sentimiento
            perform_sentiment_analysis(text)


# convert call to text, it receives the folder(informacion, matricula, etc) and the audio name
def convert_call_to_text(folder, audio):
    call = sr.AudioFile(directory_paths.AUDIO + folder + '/' + audio)
    r = sr.Recognizer()

    with call as source:
        audio = r.record(source)

        try:
            text = r.recognize_google(audio,
                                      language="es-CR")
            return text

        except Exception as ex:
            print(ex)


def perform_sentiment_analysis(text):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(text)

    print("Analisis de sentimiento general es de : ", sentiment_dict)
    print("La llamada fue calificada como ", sentiment_dict['neg'] * 100, "% Negativa")
    print("La llamada fue calificada como ", sentiment_dict['neu'] * 100, "% Neutral")
    print("La llamada fue calificada como ", sentiment_dict['pos'] * 100, "% Positiva")
    print("Llamada con calificacion general como ", end=" ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positiva")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negativa")

    else:
        print("Neutral")

    print("")


process_call_recording()
