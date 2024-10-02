

from src.finetune_bert_model_question_answer.config.configuration import ConfigManager

from transformers import AutoTokenizer
from transformers import pipeline



class PredictionPipeline:

    def __init__(self):
        self.config = ConfigManager().get_model_prediction_config()


    def predict(self, question):

        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        question_answerer = pipeline("question-answering", model=self.config.model_path, tokenizer = tokenizer)
        
        context = """
        🤗 Transformers is backed by the three most popular deep learning libraries — Jax, PyTorch and TensorFlow — with a seamless integration
        between them. It's straightforward to train your models with one before loading them for inference with the other.
        """
        output = question_answerer(question=question, context=context)
        print(output)
        print(output['answer'])

        return output


