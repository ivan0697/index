from flask import Flask, render_template
app = Flask(__name__)
@app.route('/about')
def home():
    return('Aprendiendo flask')

@app.route('/')
def homee():
    return render_template ('home.html')

if __name__==('__main__'):
    app.run(debug=True)