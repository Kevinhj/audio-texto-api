import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

r = sr.Recognizer()

call = sr.AudioFile('unprocessed_interactions/audio/informacion/grabacion-06-08-2021-pos.wav')
#llamada = sr.AudioFile('')
with call as source:
    audio = r.record(source)

    try:
        text = r.recognize_google(audio,
                                  language="es-CR")
        print(text)

        # write the text on a file
        #f = open("processed_audio/call_test.txt", "w")
        #f.write(text)
        #f.close()

        # Analysis de Sentimiento
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

    except Exception as ex:
        print(ex)


