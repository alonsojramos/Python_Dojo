from flask_app import app 
from flask_app.controllers import users 
    # #replace rename_controller 
    # with your controller file name. 
    # Do not include .py
    # controllers are where routes live !!!!!

if __name__=='__main__':
    app.run(debug=True, port=5001)