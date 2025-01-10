from flask import Flask, render_template, request
from cardclass import Card
from handclass import Hand
from deckclass import Deck
from simulation import Simulator

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods = ["POST"])
def simulate():
    emoji_to_card = {
    "🃑": Card('A', 'S'),
    "🃁": Card('A', 'C'),
    "🂱": Card('A', 'H'),
    "🂡": Card('A', 'D'),
    "🃞": Card('K', 'S'),
    "🃎": Card('K', 'C'),
    "🂾": Card('K', 'H'),
    "🂮": Card('K', 'D'),
    "🃝": Card('Q', 'S'),
    "🃍": Card('Q', 'C'),
    "🂽": Card('Q', 'H'),
    "🂭": Card('Q', 'D'),
    "🃛": Card('J', 'S'),
    "🃋": Card('J', 'C'),
    "🂻": Card('J', 'H'),
    "🂫": Card('J', 'D'),
    "🃚": Card('10', 'S'),
    "🃊": Card('10', 'C'),
    "🂺": Card('10', 'H'),
    "🂪": Card('10', 'D'),
    "🃙": Card('9', 'S'),
    "🃉": Card('9', 'C'),
    "🂹": Card('9', 'H'),
    "🂩": Card('9', 'D'),
    "🃘": Card('8', 'S'),
    "🃈": Card('8', 'C'),
    "🂸": Card('8', 'H'),
    "🂨": Card('8', 'D'),
    "🃗": Card('7', 'S'),
    "🃇": Card('7', 'C'),
    "🂷": Card('7', 'H'),
    "🂧": Card('7', 'D'),
    "🃖": Card('6', 'S'),
    "🃆": Card('6', 'C'),
    "🂶": Card('6', 'H'),
    "🂦": Card('6', 'D'),
    "🃕": Card('5', 'S'),
    "🃅": Card('5', 'C'),
    "🂵": Card('5', 'H'),
    "🂥": Card('5', 'D'),
    "🃔": Card('4', 'S'),
    "🃄": Card('4', 'C'),
    "🂴": Card('4', 'H'),
    "🂤": Card('4', 'D'),
    "🃓": Card('3', 'S'),
    "🃃": Card('3', 'C'),
    "🂳": Card('3', 'H'),
    "🂣": Card('3', 'D'),
    "🃒": Card('2', 'S'),
    "🃂": Card('2', 'C'),
    "🂲": Card('2', 'H'),
    "🂢": Card('2', 'D'),
}
    self1 = emoji_to_card[request.form.get("self1")]
    self2 = emoji_to_card[request.form.get("self2")]
    other1 = emoji_to_card[request.form.get("other1")]
    other2 = emoji_to_card[request.form.get("other2")]
    handself = Hand([self1, self2])
    handother = Hand([other1, other2])
    simulation = Simulator()
    result = simulation.run_sim(handself, handother)
    return render_template("index.html", result = result)



if __name__ == "__main__":
    app.run(debug = True)