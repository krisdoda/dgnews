from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def index():
    if os.path.exists('news_data.csv'):
        df = pd.read_csv('news_data.csv')
        return render_template('index.html', tables=[df.to_html(classes='data', header="true")], titles=df.columns.values)
    else:
        return "No data available. Please run the scraper."

if __name__ == '__main__':
    app.run(debug=True)
