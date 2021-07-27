import speech_recognition as sr

r = sr.Recognizer()

call = sr.AudioFile('unprocessed_audio/grabacion-27-07-2021.wav')
with call as source:
    audio = r.record(source)

    try:
        text = r.recognize_google(audio,
                                  language="es-CR")
        print(text)
    except Exception as ex:
        print(ex)

    f = open("processed_audio/call_test.txt", "w")
    f.write(text)
    f.close()
