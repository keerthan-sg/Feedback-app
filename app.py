from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method == "POST":
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form['rating']
        comments = request.form['comments']

        if customer == '' or dealer == '':
            return render_template('index.html',message='Please enter required fields..')

        #code


        return render_template('index.html',message='You have submitted the feedback form')
if __name__ == '__main__':
    app.run(debug=True)