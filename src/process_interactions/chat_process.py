from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from src.utilities.base_utility import get_audio_chat_file_names
from src.utilities.base_utility import get_id_catalogo_interaccion
from src.utilities.base_utility import get_cliente_operador_dni
from src.configs import interactions
from src.configs import unprocessed_interactions
from src.utilities.db_utility import insert_interacciones
from src.utilities.db_utility import insert_sentimiento_interaccion


# Procesa los chats aplicando analisis de sentimiento
def process_chats():
    chat_folder = ["informacion", "matricula", "cobro"]  # subcarpeta list

    # loop en la carpeta de audios para obtener el nombre de los archivos
    for folder in chat_folder:
        chats = get_audio_chat_file_names(folder, 'chat')
        print("============================================")
        print(f"Procesando llamadas de la carpeta: {folder}")
        print(f"Lista de chats encontrados: {chats}")

        id_categoria_interaccion = get_id_catalogo_interaccion(folder)  # [categoriainteraccion(FK)]
        id_medio_interaccion = interactions.CHAT  # Chat siempre tienen el id 2 [mediointeraccion(FK)]

        for chat in chats:
            text = get_chat_conversation(folder, chat)  # [conversacion]
            print(text)

            dni_and_date = get_cliente_operador_dni(chat)
            dni_operador = dni_and_date[0]  # dni del operador a utilizar para obtener el operador id en la bd
            dni_cliente = dni_and_date[1]  # dni del cliente a utilizar para obtener el cliente id en la bd
            chat_date = dni_and_date[2]  # [fechainteraccion]

            # llama metodo para insert en tbInteracciones
            id_interaccion = insert_interacciones(dni_cliente, dni_operador,
                                                  id_categoria_interaccion, id_medio_interaccion,
                                                  chat_date, text)

            perform_sentiment_analysis(text, id_interaccion)


# convierte la llamada a texto , recibe el folder(informacion, matricula, etc) y el nombre de el archivo
def get_chat_conversation(folder, chat):
    with open(unprocessed_interactions.CHAT_PATH + folder + '/' + chat, 'r') as chat:
        try:
            text = chat.readlines()
            chat.close()
            return text[0]
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


process_chats()
