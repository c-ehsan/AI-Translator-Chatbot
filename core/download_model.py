from transformers import AutoTokenizer ,AutoModelForSeq2SeqLM

def load_model_tokenizer(model_path):
    return(AutoTokenizer.from_pretrained(model_path),
    AutoModelForSeq2SeqLM.from_pretrained(model_path))



