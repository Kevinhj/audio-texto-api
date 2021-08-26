from os import walk
from src.configs import unprocessed_interactions
from src.configs import interactions


# get and return the list of audios on a given folder
def get_audio_chat_file_names(folder, tipo_interaccion='audio'):
    if tipo_interaccion == 'audio':
        filenames = \
            next(walk(unprocessed_interactions.AUDIO_PATH + folder),
                 (None, None, []))[2]  # [] if no file
    else:
        filenames = \
            next(walk(unprocessed_interactions.CHAT_PATH + folder),
                 (None, None, []))[2]  # [] if no file

    return filenames


def get_id_catalogo_interaccion(subfolder):
    if subfolder == 'informacion':
        return interactions.INFORMACION
    elif subfolder == 'matricula':
        return interactions.MATRICULA
    else:
        return interactions.COBRO


def get_cliente_operador_dni(file_name):
    dni = file_name.split("_")
    return dni
