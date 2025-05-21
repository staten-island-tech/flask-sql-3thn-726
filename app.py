from flask import Flask, render_template, request, redirect
from models import db, Idea

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideas.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    ideas = Idea.query.all()
    return render_template('index.html', ideas=ideas)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        text = request.form['idea']
        new_idea = Idea(text=text)
        db.session.add(new_idea)
        db.session.commit()
        return redirect('/')
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)
