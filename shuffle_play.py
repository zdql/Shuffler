import os
import random
import pygame
import sys
import time


def play_music(music_file):
    """
    Stream music with mixer.music module in a blocking manner.
    This will stream the sound from disk while playing.
    """
    # set up the mixer
    freq = 44100     # audio CD quality
    bitsize = -16    # unsigned 16 bit
    channels = 2     # 1 is mono, 2 is stereo
    buffer = 2048    # number of samples (experiment to get best sound)
    pygame.mixer.init(freq, bitsize, channels, buffer)

    # volume value 0.0 to 1.0
    pygame.mixer.music.set_volume(0.8)

    # Try to load the music, raise an exception if it fails
    try:
        pygame.mixer.music.load(music_file)
    except pygame.error:
        print(f"File {music_file} not found! ({pygame.get_error()})")
        return

    pygame.mixer.music.play()


def main(folder_path):
    """
    Entry point of the program
    """
    # check if the music directory exists
    if not os.path.isdir(folder_path):
        print(f"Directory '{folder_path}' not found!")
        return

    # get all mp3 files from the directory
    mp3_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]

    print("files: ", mp3_files)
    # shuffle the list of mp3 files
    random.shuffle(mp3_files)

    # play each song in the shuffled list
    for file in mp3_files:
        file_path = os.path.join(folder_path, file)
        print(f"Playing {file}...")
        play_music(file_path)

        # check if playback has finished
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python shuffle_play.py <path_to_music_folder>")
    else:
        main(sys.argv[1])
