"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
      <html>
        <head>
          <title>Home</title>
        </head>
        <body>
          <a href="/hello">Take me to the next page</a>
        </body>
      </html>
      """

@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <div>
          Please select a compliment 
            <select name="compliment">
              <option value="awesome">Awesome</valiue>
              <option value="terrific">Terrific</value>
              <option value="fantastic">Fantastic</value>
              <option value="neato">Neato</value>
              <option value="fantabulous">Fantabulous</value>
              <option value="wowza">Wowza</value>
              <option value="oh-so-not-meh">Oh-so-not-meh</value>
              <option value="brilliant">Brilliant</value>
              <option value="ducky">Ducky</value>
              <option value="coolio">Coolio</value>
              <option value="incredible">Incredible</value>
              <option value="wonderful">Wonderful</value>
              <option value="smashing">Smashing</value>
              <option value="lovely">Lovely</value>
            </select>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""
    
    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
