#importing module
import logging
  
#Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
#Creating an object
logger=logging.getLogger()
  
#Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)
  
#Test messages
logger.debug("debug Message")
logger.info("information message")
logger.warning("Warning message")
logger.error("Error message")
logger.critical("Critical message")