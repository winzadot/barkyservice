# the simplest flask application can fit in a single source file
from enum import unique
from datetime import datetime

from flask import Flask

app = Flask(__name__)

def homepageModel():
    from models import User
    output = User.query.all()
    app.logger.debug(output)
    return output.to_json()
 

##### ROUTES #####
@app.route("/")
def homepage():
    
   ''' from models import homepageModel'''
   return homepageModel()


if __name__ == '__main__':
    app.run(debug=True)