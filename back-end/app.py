from flask import Flask,request,render_template,url_for,redirect

from functions.createList import create_list,get_items,api_add


def create_app():
        app = Flask(__name__)

        @app.route('/', methods=['POST','GET'])
        def index():
    
            return render_template('index.html', list=get_items())

        @app.route('/submit', methods=['POST','GET'])
        def submit():
            
            if request.method=='POST':
                details = request.form['details']
                create_list(details)
            return redirect(url_for('index') )        
        @app.route('/api/process', methods=['POST'])       
        def process():
            req =request.data
            decoded=req.decode()
            print(decoded)
            data=api_add(req)
            res={'data':data}
            return res

                
                       
                   
                


                
              


        return app

