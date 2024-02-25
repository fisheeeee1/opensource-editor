from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # you cant really change this

if __name__ == '__main__':
    app.run(debug=True)

# this runs the app in debug mode (i recommend doing this in cmd.exe if you want to update without rerunning it every time)
