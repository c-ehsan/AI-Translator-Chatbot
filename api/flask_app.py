from flask import Flask  ,render_template
class API:
    def __init__(self) -> None:
        self.app=Flask(__name__)

    def relatives_routes(self):
        @self.app.route("/")
        def start():
            
            return render_template("index.html")
        

    def run_app(self):
        self.app.run(host="127.0.0.1",port=5000)
        
        
