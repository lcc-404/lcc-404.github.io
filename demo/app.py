from flask import Flask, request, render_template
import torch

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compose', methods=['POST'])
def compose():
    # 使用之前musegan.compose里的
    tempo=request.form['tempo']
    step=request.form['step']
    inst=request.form['inst']
    return render_template('compose.html', tempo=tempo,step=step,inst=inst)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
