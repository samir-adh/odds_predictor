import sys
sys.path.append("../")
import matplotlib.pyplot as plt
import sqlite3

def plot_results(): # FIXME
    X = []
    Y = []
    connection = sqlite3.connect("./static/odds.db")
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT * FROM odds
        """
    )
    response = cursor.fetchall()
    n_games = len(response)
    for i in range(n_games):
        game = response[i]
        for j in range(2-1):
            x = game[j]
            X_i = [x_i[0] for x_i in X]
            if x in X_i:
                X[X_i.index(x)][1] += x*(j==game[3])
            else:
                X.append([x,x*(j==game[3])])
    connection.close()
    X.sort(key=lambda x:x[0])
    plt.plot(X)
    plt.show()
    
if __name__ == "__main__":
    plot_results()