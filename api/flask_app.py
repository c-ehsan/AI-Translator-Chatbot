from flask import Flask  ,render_template,jsonify,request
from core.translator import translate_auto
class API:
    def __init__(self) -> None:
        self.app=Flask(__name__)

    def relatives_routes(self):

        @self.app.route("/")
        def home():
            return render_template("index.html")
        @self.app.route("/translate",methods=["POST"])
        def translate():
            data=request.get_json()

            text=data["text"]

            result=translate_auto(text)

            return jsonify({
                "translation":result
            })


    def run_app(self):
        self.app.run(host="127.0.0.1",port=5000)
        
        
