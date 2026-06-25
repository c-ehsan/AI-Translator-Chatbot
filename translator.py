from transformers import AutoModelForSeq2SeqLM , AutoTokenizer
from transformers import GenerationConfig
from download_model import load_model_tokenizer
# load model translation persian to english 



#load model 
tokenizer,model=load_model_tokenizer("./models")




def translate_fa_to_en(text,source_lang,target_lang):
    """Translation Persian text to English
    ARGS:
    text=get a text(str) and translate it.
    source_lang=get Origin language
    tatget_lang=get Destination  language
    """

    source_lang=source_lang
    target_lang=target_lang

    inputs=tokenizer(text,return_tensors="pt")

    outputs=model.generate(**inputs,
                max_new_tokens=100,
                num_beams=4,
                forced_bos_token_id=tokenizer.convert_tokens_to_ids(target_lang)) # for translation num_beams its better
    
    translation=tokenizer.decode(outputs[0],skip_special_tokens=True)



    return translation



res=translate_fa_to_en("hello my freind","eng_Latn","pes_Arab")
print(f"translate_result is :{res}")
