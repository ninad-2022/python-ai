import logging

logging.basicConfig(
    level=logging.DEBUG,
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filename="logging.txt"
)

logging.warning("this is not allowed!")

logging.error("Something went wrong!")

logging.critical("Exiting the app")

logging.debug("Value is 123")

# this will give you a logging.txt file 