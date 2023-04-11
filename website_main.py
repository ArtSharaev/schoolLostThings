import logging
from flask_app import application

logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s]'
                           u' %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG,
                    filename='logging_lib/website-logging.log',
                    filemode='w')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port="8080")
