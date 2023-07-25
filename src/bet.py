import sys

sys.path.append("../")
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

W_count = 0

def kelly_criterion(odd: float):
    p = 1 / odd
    q = 1 - p
    b = odd - 1
    x = (q / b)
    res = p - (q / b)  # 1/odd - (1- (1/odd)/(odd-1) = p - (1-p)/(1/p - 1)
    return 0.05


def gamble(wealth: float, odd: float, outcome: bool):
    bet = kelly_criterion(odd)*wealth
    if outcome:
        new_wealth = wealth + bet * (odd - 1)
    else:
        new_wealth = wealth - bet
    return new_wealth

def place_bet(wealth: float):
    connection = sqlite3.connect("./static/odds.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM odds
    """
    )
    response = cursor.fetchall()
    connection.close()
    game = response[np.random.randint(len(response))]
    odd_placed = min(game[:3])
    outcome = odd_placed == game[game[3]]
    if outcome:
        global W_count
        W_count +=1
    return gamble(wealth=wealth, odd=odd_placed, outcome=outcome)


def bet_simulator(starting_wealth: float, n_bets: int):
    wealth = starting_wealth
    wealth_evolution = [starting_wealth]
    for i in range(n_bets):
        wealth = place_bet(wealth)
        wealth_evolution.append(wealth)
    return wealth_evolution


def plot_wealth_evolution(starting_wealth: float, n_bets: int):
    wealth_evolution = bet_simulator(starting_wealth, n_bets)
    plt.plot(np.arange(n_bets + 1), wealth_evolution)
    plt.xlabel("Temps")
    plt.ylabel("€€€")
    plt.show()


if __name__ == "__main__":
    starting_wealth = 1e5
    n_bets = 250
    plot_wealth_evolution(starting_wealth, n_bets)
    print(W_count)
