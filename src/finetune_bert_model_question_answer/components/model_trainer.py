

from src.finetune_bert_model_question_answer.entity import ModelTrainerConfig
import os
import evaluate
from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from transformers import TrainingArguments
from transformers import Trainer
from datasets import load_dataset, load_from_disk

metric = evaluate.load("squad")

class ModelTrainer:

    def __init__(self, config:ModelTrainerConfig):
        self.config = config


    def train(self):
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForQuestionAnswering.from_pretrained(self.config.model_ckpt)
        
        datasets = load_from_disk(self.config.data_path)


        args = TrainingArguments(
            output_dir =self.config.root_dir,
            evaluation_strategy="no",
            save_strategy="epoch",
            learning_rate=2e-5,
            num_train_epochs=0.5,
            weight_decay=0.01,
            remove_unused_columns=False
        )

        trainer = Trainer(
            model=model,
            args=args,
            train_dataset=datasets['train'],
            eval_dataset=datasets['validation'],
            tokenizer=tokenizer,
        )
        trainer.train()

        # Save model
        model.save_pretrained(os.path.join(self.config.root_dir,"distilber-uncased"))
        
        # Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))