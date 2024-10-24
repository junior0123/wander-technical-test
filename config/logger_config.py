import logging
import os

def setup_logger():
    # Define the path to the 'logs' folder in the root of the project
    log_directory = os.path.join(os.getcwd(), 'logs')

    # Create the directory if it doesn't exist
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Define the path to the log file
    log_file_path = os.path.join(log_directory, 'test_log.log')

    # Create the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Set the level of the logger

    # Remove existing handlers to avoid duplicates
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create file handler which logs to the file
    file_handler = logging.FileHandler(log_file_path, mode='a')
    file_handler.setLevel(logging.INFO)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Define the format for the logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Make sure to close handlers at the end to avoid unclosed resource warnings
def close_logger(logger):
    handlers = logger.handlers[:]
    for handler in handlers:
        handler.close()
        logger.removeHandler(handler)
