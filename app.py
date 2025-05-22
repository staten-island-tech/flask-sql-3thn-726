from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ideas.db'
db = SQLAlchemy(app)

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)

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
        return redirect(url_for('index'))
    return render_template('submit.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        idea_id = request.form.get('id')
        idea = Idea.query.get(idea_id)
        if idea:
            db.session.delete(idea)
            db.session.commit()
        return redirect(url_for('delete'))
    ideas = Idea.query.all()
    return render_template('delete.html', ideas=ideas)


if __name__ == '__main__':
    app.run(debug=True)