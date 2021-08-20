import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from src.utilities.base_utility import get_audio_file_names
from src.utilities.base_utility import get_id_catalogo_interaccion
from src.utilities.base_utility import get_cliente_operador_dni
from src.configs import interactions
from src.configs import unprocessed_interactions
from datetime import date
from src.utilities.db_utility import insert_interacciones
from src.utilities.db_utility import insert_sentimiento_interaccion


# Procesa las llamadas a texto y aplica analisis de sentimiento
def process_call_recording():
    audio_folder = ["informacion", "matricula", "cobro"] #subcarpeta list

    # loop en la carpeta de audios para obtener el nombre de los archivos
    for folder in audio_folder:
        audios = get_audio_file_names(folder)
        print("============================================")
        print(f"Procesando llamadas de la carpeta: {folder}")
        print(f"Lista de audios encontrados: {audios}")

        id_categoria_interaccion = get_id_catalogo_interaccion(folder) # [categoriainteraccion(FK)]
        id_medio_interaccion = interactions.LLAMADA # llamadas siempre tienen el id 1 [mediointeraccion(FK)]

        # loop en los audios de un subfolder
        for audio in audios:
            text = convert_call_to_text(folder, audio) # [conversacion]
            print(text)
            call_date = date.today() # [fechainteraccion]

            dni = get_cliente_operador_dni(audio)
            dni_operador = dni[0] # dni del operador a utilizar para obtener el operador id en la bd
            dni_cliente = dni[1] # dni del cliente a utilizar para obtener el cliente id en la bd

            # llama metodo para insert en tbInteracciones
            id_interaccion = insert_interacciones(dni_cliente, dni_operador,
                                                  id_categoria_interaccion, id_medio_interaccion,
                                                  call_date, text)

            perform_sentiment_analysis(text, id_interaccion)


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


def perform_sentiment_analysis(text, id_interaccion):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(text)

    valor_negativo = sentiment_dict['neg']
    valor_neutral = sentiment_dict['neu']
    valor_positivo = sentiment_dict['pos']
    valor_compuesto = sentiment_dict['compound']

    print("Analisis de sentimiento general es de : ", sentiment_dict)
    print("La llamada fue calificada como ", valor_negativo * 100, "% Negativa")
    print("La llamada fue calificada como ", valor_neutral * 100, "% Neutral")
    print("La llamada fue calificada como ", valor_positivo * 100, "% Positiva")
    print("Llamada con calificacion general como ", end=" ")

    # decide sentiment as positive, negative and neutral
    if valor_compuesto >= 0.05:
        result = "Positiva"  # [resultado]
        print(result)

    elif valor_compuesto <= - 0.05:
        result = "Negativa"
        print(result)

    else:
        result = "Neutral"
        print(result)

    print("")
    # llama el metodo para insert en tbSentimientoInteracciones
    insert_sentimiento_interaccion(id_interaccion, valor_negativo, valor_neutral,
                                   valor_positivo, valor_compuesto, result)


process_call_recording()
