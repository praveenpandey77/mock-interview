from flask import Flask, render_template

app = Flask(__name__)

JOBS=[
  {
    'NAME': 'PRAVEEN',
    'ADDRESS': 'ASHOK NAGAR',
    'SALARY': '10,0000',
    'STREET SYMBOL': 'DELTA'
  },
  {
    'NAME': 'namrata',
    'ADDRESS': 'parpodi',
    'SALARY': '15,0000',
    'STREET SYMBOL' : 'sigma'
  }
]


@app.route("/")
def hello_world():
  return render_template('home.html', details=JOBS, character='life details in sanskrit')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
