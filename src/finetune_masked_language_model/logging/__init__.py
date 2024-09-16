

import os
import sys
import logging

log_dir = "logs"

log_filepath = os.join.path(log_dir, 'running_log')

os.makedir(log_dir, exist_ok = True)

logging.basicConfig(
    filename = log_filepath,
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getgetLogger('question-answer')
