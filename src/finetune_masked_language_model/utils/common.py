
import os
from src.finetune_masked_language_model.logging import logger

from ensure import ensure_anotation
from box import ConfigBox
from pathlib import Path
import yaml
import json




@ensure_anotation
def read_yaml(path_to_yaml: Path, verbose=True) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error reading yaml file: {e}")