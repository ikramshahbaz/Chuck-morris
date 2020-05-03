from flask import Flask
app = Flask(__name__)

@app.route("/")
def homepage():
    return """
    <p>Chuck Norris doesnt read books He stares them down until he gets the information he wants</p>
    <p>Time waits for no man Unless that man is Chuck Norris</p>
    <p>If you spell Chuck Norris in Scrabble you win Forever</p>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
