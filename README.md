# Coin Toss Simulator

A Python project that simulates coin toss experiments and analyzes their results using basic probability concepts and Monte Carlo simulation.

## Project Goal

The main goal of this project is to reinforce Python fundamentals while practicing concepts such as:

- Functions
- Loops
- Conditionals
- Lists
- Dictionaries
- Randomness
- Percentages and averages
- Streak detection
- Basic probability
- Monte Carlo simulation

## How It Works

The program simulates a configurable number of coin tosses.

Each toss can result in:

- `H` → Heads
- `T` → Tails

The user defines:

- The value earned when Heads occurs
- The value lost when Tails occurs
- The number of tosses per experiment
- The number of experiments

Each experiment calculates information such as:

- Total Heads
- Total Tails
- Percentage of Heads
- Percentage of Tails
- Longest Heads streak
- Longest Tails streak
- Money earned
- Money lost
- Final balance

After running multiple experiments, the program performs a Monte Carlo analysis.

## Monte Carlo Results

The final simulation reports:

- Average balance
- Average Heads percentage
- Average Tails percentage
- Number of profitable experiments
- Number of losing experiments
- Number of break-even experiments
- Probability of profit
- Probability of loss
- Probability of break-even
- Best balance
- Worst balance
- Longest Heads streak observed
- Longest Tails streak observed

## Project Structure

```text
3_coin_toss_simulator/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── coin.py
│   └── simulator.py
│
├── .gitignore
├── README.md
└── requirements.txt