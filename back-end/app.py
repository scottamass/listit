from flask import Flask,request,render_template,url_for,redirect

from functions.createList import create_list,get_items


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


        return app

