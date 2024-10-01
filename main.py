from app import application
from app.api import *



if __name__=="__main__":

    application.run(host='0.0.0.0',debug=True)