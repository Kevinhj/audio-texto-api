from os import walk
from src.configs import directory_paths


def get_audio_file_names(folder):
    filenames = \
        next(walk(directory_paths.AUDIO + folder),
             (None, None, []))[2]  # [] if no file

    return filenames
