from app import app

#import routes
from app.routes import *

# import Models
from app.models import register

if __name__ == '__main__':
    app.run(port=8080, debug=True)
