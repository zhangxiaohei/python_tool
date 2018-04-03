import logging

# https://docs.python.org/3/library/logging.html
logging.basicConfig(level = logging.INFO,format = '%(asctime)s %(name)s %(levelname)s %(filename)s:%(lineno)d   %(message)s')
logger = logging.getLogger(__name__)

logger.info("Start print log")
logger.debug("Do something")
logger.warning("Something maybe fail.")
logger.info("Finish")
