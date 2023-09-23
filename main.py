from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

wines = pd.read_csv('wines.csv')
wines = wines[['country','description','name','points','price']]

@app.route('/')

def home():
    return render_template('home.html', data = wines.to_html())

@app.route('/api/v1/best')

def bestPoint():
    result = wines[wines['points'] == 100 ].to_dict(orient='records')
    return result

@app.route('/api/v1/expensive')

def expensive():
    result = wines[wines['price'] == wines['price'].max()]['name'].squeeze()
    return result


@app.route('/api/v1/lowprice')

def lowPrice():
    result = wines[wines['price'] < 100].to_dict(orient='records')
    return result



    

if __name__ == '__main__':
    app.run(debug=True)