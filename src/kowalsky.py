import sys
sys.path.append("../")
import matplotlib.pyplot as plt
import numpy as np
import sqlite3

def plot_results(): # FIXME
    connection = sqlite3.connect("./static/odds.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM odds
        """
    )
    response = cursor.fetchall()
    n_games = len(response)
    n = 64
    Y = [0.]*n
    X = [0]*n
    for game in response:
        for i in range(0,3):
            index = int(game[i])
            X[index] +=1
            if i==game[3]:
                Y[index] +=1
    for i in range(len(X)):
        if X[i] > 0:
            Y[i] = Y[i]/X[i]
    plt.bar(np.arange(32),Y[:32])
    X = np.arange(1,33)
    Y = 1/X
    plt.plot(np.arange(32),Y,color='r')
    plt.show()
            
    

    
if __name__ == "__main__":
    plot_results()