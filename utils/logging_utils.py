import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S",
    level=logging.DEBUG,
    handlers=[logging.StreamHandler(), logging.FileHandler("logs/test.log")],
)

logger = logging.getLogger()
