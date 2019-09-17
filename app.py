from flask import Flask, render_template_string
import requests


app = Flask(__name__)


@app.route('/')
def home():
    url = requests.get('https://api.nasa.gov/planetary/apod?api_key=LJboidkkTayViWW9uihvwKMASyg9bBQx0CAo0nvW')
    data = url.json()

    return render_template_string('''<title>NASA API</title>
    <h1>{{ data.title }}</h1>
    <h2>by {{ data.copyright }}</h2>
    <h2>at {{ data.date }}</h2>
    <img src="{{ data.url }}">
    <p>{{ data.explanation }}</p>''', data = data)


if __name__ == '__main__':
    app.run(debug=True)
    





