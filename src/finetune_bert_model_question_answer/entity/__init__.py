import os
from dataclasses import dataclass

from pathlib import Path



@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_file_dir: Path
    unzip_dir: Path

@dataclass(frozen = True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_FILES: list

@dataclass(frozen = True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: Path

@dataclass(frozen = True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path




