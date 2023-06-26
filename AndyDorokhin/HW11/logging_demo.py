import logging

logging.basicConfig(filename='app.log',filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')

logger=logging.getLogger('Example_logger')
print(logger)
logger.warning('This is a warning')