import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from src.utilities.base_utility import get_audio_file_names
from src.utilities.base_utility import get_id_catalogo_interaccion
from src.utilities.base_utility import get_cliente_operador_dni
from src.configs import interactions
from src.configs import unprocessed_interactions
from datetime import date
from src.utilities.db_utility import insert_interacciones


# Process the calls to text and apply sentiment analysis
def process_call_recording():
    audio_folder = ["informacion", "matricula", "cobro"]

    # loop over the audio folders to get the file names
    for folder in audio_folder:
        audios = get_audio_file_names(folder)
        print("============================================")
        print(f"Procesando llamadas de la carpeta: {folder}")
        print(f"Lista de audios encontrados: {audios}")

        id_categoria_interaccion = get_id_catalogo_interaccion(folder) # [categoriainteraccion(FK)]
        id_medio_interaccion = interactions.LLAMADA # always call with id 1 [mediointeraccion(FK)]

        # loop over the audios under a given folder
        for audio in audios:
            text = convert_call_to_text(folder, audio) # [conversacion]
            print(text)
            call_date = date.today() # [fechainteraccion]

            dni = get_cliente_operador_dni(audio)
            dni_operador = dni[0] # dni del operador a utilizar para obtener el operador id en la bd
            dni_cliente = dni[1] # dni del cliente a utilizar para obtener el cliente id en la bd

            # call here the method to insert on tbInteracciones
            insert_interacciones(dni_cliente, dni_operador, id_categoria_interaccion, id_medio_interaccion, call_date, text)
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
        result = "Positiva"  # [resultado]
        print(result)

    elif sentiment_dict['compound'] <= - 0.05:
        result = "Negativa"
        print(result)

    else:
        result = "Neutral"
        print(result)

    print("")
    # call here the method to insert on tbSentimientoInteracciones


process_call_recording()
