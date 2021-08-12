from os import walk
from src.configs import unprocessed_interactions
from src.configs import interactions


# get and return the list of audios on a given folder
def get_audio_file_names(folder):
    filenames = \
        next(walk(unprocessed_interactions.AUDIO_PATH + folder),
             (None, None, []))[2]  # [] if no file

    return filenames


def get_id_catalogo_interaccion(subfolder):
    if subfolder == 'informacion':
        return interactions.INFORMACION
    elif subfolder == 'matricula':
        return interactions.MATRICULA
    else:
        return interactions.COBRO
