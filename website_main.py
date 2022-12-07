import logging
from flask_app import app


logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s]'
                           u' %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG,
                    filename='logging/website-logging.log',
                    filemode='w')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
