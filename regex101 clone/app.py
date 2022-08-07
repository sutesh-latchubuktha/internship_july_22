import re
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods = ['POST','GET'])
def regexEvaluate():
    if request.method == 'POST':
        reg_pattern = request.form['expression']
        sentence = request.form['string']
        pattern = re.compile(reg_pattern)
        result = pattern.findall(sentence)
        return render_template('index.html',reg_pattern = reg_pattern,sentence=sentence,values = result,count= len(result))
    return render_template('index.html')

    
if __name__ == "__main__":
    app.run()