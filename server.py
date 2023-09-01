from flask import Flask, render_template, request # This is different from requests
from MyTranslator import translate_text
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")

def index():
    return render_template("/index.html")

@app.route("/getData")
def get_data():
    source = request.args.get("source_text")
    tran_text = translate_text(source, "ur")
    return render_template("index.html",
                           translated_text = tran_text)


if __name__ == "__main__":

    app.run(host="0.0.0.0", port = 8000) # code for run on local machine
    # serve(app, host="0.0.0.0", port=8000) # code for run in production server