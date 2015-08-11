import logging
import time
import json 
import platform
from twilio.rest import TwilioRestClient

class TWHandler(logging.Handler):
    """
    logging handler uses postmarkapp to send email at a given log level.
    """

    def __init__(self, config):
        """
        accepts {config}
        inititializes Handler
        """
        self.config = config
        logging.Handler.__init__(self)

    def emit(self, record):
        """
        accepts record logging message object
        """
        for number in self.config["recipients"]:
            try:
                self.send(number, record)
            except(KeyboardInterrupt, SystemExit):
                raise
            except:
                self.handleError(record)

    def send(self, number, record):
        """
        accepts
            number string  E.164 formated phone number (+19995551212)
            record logging message object 

        uses twilio module to send
        """

        body = json.dumps({
            "host": platform.node(),
            "time": record.asctime,
            "logger name": record.name,
            "error level": record.levelname,
            "file": record.pathname,
            "module": record.module,
            "function": record.funcName,
            "message": record.message,
                },
            indent=True
            )

        client = TwilioRestClient(
                self.config["sid"],
                self.config["token"],
                )

        message = client.messages.create(
                body = body,
                to = number,
                from_= self.config["From"],
                )
        # we'll just reeeealy respect that rate limit. 
        time.sleep(5)
