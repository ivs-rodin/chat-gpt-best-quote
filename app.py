from flask import Flask, request, jsonify
from api.andruxnet_random_famous_quotes import get_quote
from api.motivational_text_generator import generate_quote_answer

app = Flask(__name__)

@app.route("/")
def generate_quote():

    quoteResp = get_quote('famous', 1).json()[0]
    if 'quote' not in quoteResp or not len(quoteResp['quote']):
        assert False, f"Bad quote response: {quoteResp}"
    quote = quoteResp['quote']

    motivationText = generate_quote_answer(quote)

    return jsonify({"motivationText": motivationText})

if __name__ == "__main__":
    app.run(debug=True)