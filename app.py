from flask import Flask, render_template, request
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""

    if request.method == 'POST':
        text = request.form['text']

        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()

        result = summarizer(parser.document, 3)

        summary = " ".join([str(sentence) for sentence in result])

    return render_template('index.html', summary=summary)

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)