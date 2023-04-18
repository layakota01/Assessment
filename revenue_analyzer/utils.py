import configparser
import os

def load_config(config_file):
    """
    Load the configuration from the given file.

    :param config_file: The path to the configuration file.
    :return: A ConfigParser object with the loaded configuration.
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return config

def create_output_directory(directory):
    """
    Create the output directory if it doesn't already exist.

    :param directory: The path to the output directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def format_output_filename(output_directory, prefix, extension):
    """
    Generate a formatted output filename.

    :param output_directory: The path to the output directory.
    :param prefix: A prefix to add to the output filename.
    :param extension: The file extension to use.
    :return: A string containing the formatted output filename.
    """
    return os.path.join(output_directory, f"{prefix}_SearchKeywordPerformance.{extension}")
