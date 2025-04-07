from flask import Flask, render_template

app = Flask(__name__, template_folder='mytemplates')

@app.route('/<name>')
def Home(name):
    return render_template('one.html', abc=name)

if __name__ == '__main__':
    app.run()
