from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def quiz():
    return render_template('HappyMagic.html')

if __name__ == '__main__':##Comment this and the line next to this to deploy on heroku
    app.debug = True
    app.run(host='0.0.0.0', port = 8000)
