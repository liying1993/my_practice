from flask import Flask, render_template
from flask_script import Manager, Server

app = Flask(__name__)
manager = Manager(app)

@app.route("/")
def index():
    return render_template("temp1.html", title="hello world")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/index')
def index2():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/service')
def service():
    return render_template('service.html')

manager.add_command('runserver',
                    Server(
                        host='127.0.0.1',
                        port="5000",
                        use_debugger=True,
                        use_reloader=True
                    )

                    )
if __name__ == "__main__":
    app.run(debug=True)
