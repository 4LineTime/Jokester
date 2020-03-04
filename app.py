from flask import Flask,request, render_template
from api import jokes



app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html',img='../img/JESTER.jpeg')

@app.route('/get_my_joke')
def get_my_joke():
    category = request.args.get('category')
    resp=jokes.get_joke(category)

    if get_my_joke:
        return render_template('joke.html', category=category,
                               my_joke=resp)

    else:
        return render_template('error.html')




if __name__ == '__main__':
    app.run()
