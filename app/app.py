# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Linear Regression model
filename = 'random_forest.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index_5.html')


@app.route('/predict', methods=['POST'])
def predict():
    # with open('./random_forest.pkl', 'rb') as file:
    #     model = pickle.load(file)
    temp_array = list()

    if request.method == 'POST':

        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        overs = float(request.form['overs'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])

        temp_array = temp_array + [runs, wickets,overs,  runs_in_prev_5, wickets_in_prev_5]

        data = np.array([temp_array])
        my_prediction = int(model.predict(data)[0])
        print("Prediction:", my_prediction)
        return render_template('result.html', lower_limit=my_prediction - 4, upper_limit=my_prediction + 4)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4001,debug=True)