
import os
from src.finetune_bert_model_question_answer.logging import logger

from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import yaml
import json




@ensure_annotations
def read_yaml(path_to_yaml: Path, verbose=True) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error reading yaml file: {e}")

@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):

    try:
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f'Directory {path} successfully created !')
    except Exception as e:
        logger.error(f"Error creating directories: {e}")
        


@ensure_annotations
def get_size(path: Path) -> int:
    """
    this method return the size of file.

    Args:
        path: input like path.
    Returns:
        size: size of file.
    """
    try:
        size_in_kb = os.path.getsize(path/1024)
        return f"~ size in{size_in_kb} kb"
    except Exception as e:
        logger.error(f'error is raised from get size function :; {e}')
