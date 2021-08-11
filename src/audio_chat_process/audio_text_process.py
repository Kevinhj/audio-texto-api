import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from src.utilities.file_names import get_audio_file_names
from src.configs import directory_paths

# Procesa la llamada y le aplica analisis de sentimiento
def process_call_recording():
    audio_folder = ["informacion", "matricula", "cobro"]

    for folder in audio_folder:
        audios = get_audio_file_names(folder)
        print(audios)

        for audio in audios:
            call = sr.AudioFile(directory_paths.AUDIO + folder + '/' + audio)

            r = sr.Recognizer()
            with call as source:
                audio = r.record(source)

                try:
                    text = r.recognize_google(audio,
                                              language="es-CR")


                    # Analisis de Sentimiento
                    sentiment_analysis(text)


                except Exception as ex:
                    print(ex)


#def convert_call_to_text(call):


def sentiment_analysis(text):
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

process_call_recording()
