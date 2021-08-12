import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from src.utilities.base_utility import get_audio_file_names
from src.utilities.base_utility import get_id_catalogo_interaccion
from src.configs import interactions
from src.configs import unprocessed_interactions


# Process the calls to text and apply sentiment analysis
def process_call_recording():
    audio_folder = ["informacion", "matricula", "cobro"]

    # loop over the audio folders to get the file names
    for folder in audio_folder:
        audios = get_audio_file_names(folder)
        print("============================================")
        print(f"Procesando llamadas de la carpeta: {folder}")
        print(f"Lista de audios encontrados: {audios}")

        id_catalogo_interaccion = get_id_catalogo_interaccion(folder)
        id_medio_interaccion = interactions.LLAMADA # always call with id 1

        # loop over the audios under a given folder
        for audio in audios:
            text = convert_call_to_text(folder, audio)

            # Analisis de Sentimiento (antes de aplicar analisis de sentimiento insert ontbInteracciones y retornar
            # el id)
            perform_sentiment_analysis(text)


# convert call to text, it receives the folder(informacion, matricula, etc) and the audio name
def convert_call_to_text(folder, audio):
    call = sr.AudioFile(unprocessed_interactions.AUDIO_PATH + folder + '/' + audio)
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
