from flask import Flask, render_template
app = Flask(__name__)

#   Route for Hompage
@app.route('/', methods=['GET'])
def page_home():

    return render_template('index.html')

if __name__ == "__main__":
    app.run()