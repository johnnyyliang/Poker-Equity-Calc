# Poker Equity Calculator

A web-based poker equity calculator that simulates Texas Hold'em hands to determine winning probabilities. This application allows users to select two poker hands and calculates their respective chances of winning through Monte Carlo simulation.

## Features

- Interactive web interface with playing card emojis for card selection
- Visual poker table background
- Monte Carlo simulation with 10,000 iterations per calculation
- Supports full range of poker hand rankings:
  - Royal Flush
  - Straight Flush
  - Four of a Kind (Quads)
  - Full House
  - Flush
  - Straight
  - Three of a Kind (Trips)
  - Two Pair
  - One Pair
  - High Card

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/poker-equity-calculator.git
cd poker-equity-calculator
```

2. Install required dependencies:
```bash
pip install flask
```

## Project Structure

- `app.py` - Main Flask application file with routes and emoji-to-card mapping
- `cardclass.py` - Card class implementation
- `deckclass.py` - Deck class for managing the card deck
- `handclass.py` - Hand class with poker hand evaluation logic
- `simulation.py` - Monte Carlo simulation implementation
- `templates/index.html` - Main web interface template
- `static/styles.css` - CSS styling for the web interface
- `static/images/Table.jpg` - Poker table background image

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open a web browser and navigate to `http://127.0.0.1:5000`

3. Select cards for both hands using the dropdown menus

4. Click "Simulate" to calculate equity percentages
