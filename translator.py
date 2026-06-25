from transformers import AutoModelForSeq2SeqLM , AutoTokenizer
from transformers import GenerationConfig
from download_model import load_model_tokenizer
# load model translation persian to english 



#load model 
tokenizer,model=load_model_tokenizer("./models")

def detect_language(text):
    """This function automatically detects the language and makes our work easier for translation."""
    for char in text:
        if "\u0600"<=char<="\u06FF": # this range of chars for persian unicode chars
            return "fa"
    return "en"

def translate_auto(text:str):
    """Translation Persian text to English
    ARGS:
    text=get a text(str) and translate it.
    source_lang=get Origin language
    tatget_lang=get Destination  language
    """
    lang=detect_language(text)
    if lang=="en":
        source_lang="eng_Latn"
        target_lang="pes_Arab"

    elif lang=="fa":
        source_lang="pes_Arab"
        target_lang="eng_Latn"

    else:
        return "Language not supported"
    
    tokenizer.src_lang=source_lang



    inputs=tokenizer(text,return_tensors="pt")

    outputs=model.generate(**inputs,
                max_new_tokens=512,
                num_beams=4,
                forced_bos_token_id=tokenizer.convert_tokens_to_ids(target_lang)) # for translation num_beams its better
    
    translation=tokenizer.decode(outputs[0],skip_special_tokens=True)



    return translation

text="""به نام خدای مهربان که هر روز را با نور امید آغاز می‌کند.
زندگی همچون دفتری ست که ورق‌هایش را خودمان با قلم انتخاب می‌نویسیم.
گاه سطرهایش پر از لبخند و گاه آکنده از آموزه‌های تلخ است.
اما زیبایی در این جریان است که ما را به سوی فردایی روشن‌تر هدایت می‌کند.
پس بیایید قدر این لحظه‌های ناب را بدانیم و شکرگزار باشیم.
"""

print(len(tokenizer(text)["input_ids"]))