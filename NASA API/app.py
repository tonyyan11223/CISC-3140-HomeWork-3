from flask import Flask, render_template_string
import requests


app = Flask(__name__)


@app.route('/')
def HomeWork3():
    url = requests.get('https://api.nasa.gov/planetary/apod?api_key=LJboidkkTayViWW9uihvwKMASyg9bBQx0CAo0nvW')
    data = url.json()

    return render_template_string(
    '''
    <title>
        CISC3140 NASA API
    </title>

    <head>
    <style>
    body 
    {
         background-color:ccffff;
    }
    h1
    {
        color:#ff99ff;
    }
    h2
    {
        color:#6600ff;
    }
    h3
    {
        color:#cc3399;
    }
    p
    {
        color:#cc0066;
    }
    </style>
    </head>
    </body>
    
    <h1 style="text-align:center;">
      <br>  
            <u>
                <i>
                   {{ data.title }}
                </i>
            </u>  
        </br>
    </h1>

    <h2 style="text-align:center;">
        <br>
            <i>
                by {{ data.copyright }}
            <i>
        </br>
    </h2>

    <h3 style="text-align:center;">
        <br>
            <i>
                at {{ data.date }}
            <i>
        </br>
    </h3>

    <center>
        <img src="{{ data.url }}" width="900" height="500">
    </center>

    <p>
        <br>
            {{ data.explanation }}
        </br>
    </p>
    ''',data = data)

if __name__ == '__main__':
    app.run(debug=True)