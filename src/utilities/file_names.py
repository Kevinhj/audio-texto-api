from os import walk
from src.configs import unprocessed_interactions


# get and return the list of audios on a given folder
def get_audio_file_names(folder):
    filenames = \
        next(walk(unprocessed_interactions.AUDIO_PATH + folder),
             (None, None, []))[2]  # [] if no file

    return filenames
