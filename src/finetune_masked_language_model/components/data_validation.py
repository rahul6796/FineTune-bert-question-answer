

import os 

from src.finetune_masked_language_model.entity import DataValidationConfig
from src.finetune_masked_language_model.logging import logger


class DataValidation:


    def __init__(self, config: DataValidationConfig):
        self.config = config


    def validate_all_files(self) -> bool:

        validation_status = None 
        
        all_files = os.listdir(os.path.join('artifacts', 'data_ingestion', 'squad'))

        for files in all_files:

            if files not in self.config.ALL_FILES:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f'STATUS : {validation_status}')
            else:
                validation_status = True
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f'STATUS : {validation_status}')

            
        return validation_status
            

        