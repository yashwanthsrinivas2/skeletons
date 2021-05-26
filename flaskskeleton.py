from flask import Flask
from flask_restful import Api,request
from flask import Response
from PIL import Image
import json



def similar(image):
	return "hello world"




@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        image = request.files['img']
        result = find_similar(image)
        res1 = Response(result)
        res1.headers["Content-Type"]="application/json"
        res1.headers["Access-Control-Allow-Origin"]="*"
        return(res1)
        
port =os.getenv('PORT',5000)
if __name__ == '__main__':
    app.run(host ="0.0.0.0",port=port)
        