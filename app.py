
from flask import Flask,jsonify,request
from main import*
app = Flask(__name__)
#@app.route('/summarize', methods=['GET','POST'])
#def sample():
#   if request.method == 'POST':
#      return jsonify({ "message": "true"})  
@app.route('/api/endpoint', methods=['GET', 'POST']) 
def api_endpoint(): 
    url = request.json['url'] 
    res = main(url) 
    return {'text': res} 

if __name__ == '__main__':  
    app.run(debug = True)

 

