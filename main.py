from interfaces.tkinter_app import UI 
from core.translator import load_model_tokenizer
from api.fastapi_app import app 
from api.flask_app import API
import uvicorn
if __name__=="__main__":
    api=API()
    api.relatives_routes()
    api.run_app()

