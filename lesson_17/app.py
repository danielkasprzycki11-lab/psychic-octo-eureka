from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    users = ['Adam', 'Ewa', 'Karol']
    return render_template('index.html', title='Strona Główna', users=users)

@app.route('/about')
def about():
    return 'To jest strona o nas.'

@app.route('/contact')
def contact():
    return 'Tutaj znajdziesz nasz kontakt.'

if __name__ == '__main__':
    app.run(debug=True)
