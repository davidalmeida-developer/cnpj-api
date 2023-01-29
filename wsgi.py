from settings import app, FLASK_HOST, FLASK_PORT

import controller.cnpj_controller




if __name__ == '__main__':
    app.run(host=FLASK_HOST,port=FLASK_PORT)