# python-logging-handler-twilio
Python logging handler wrapper for twilio module

## prerequisites
- twilio (pip install twilio)
- an active twilio.com account with SID and TOKEN

## installation
This is just a simple handler wrapped around the twilio module, so I'm not going to submit it to PyPi.

### the usual
```bash
$ pip install twilio
$ python ./setup.py install
```
### virtualenv
```bash
project$ source venv/bin/activate
(venv)project$ pip install twilio 
(venv)project$ pip install pip install -e /path/to/python-logging-handler-twilio
```

### config object
- **sid**	sid supplied to you by twilio
- **token**	token supplied to you by twilio
- **recipients**	a list of one or more phone numbers in E.164 format
- **From**	a single phone number in E.164 format

```python
{
	"recipients": ["+18125551212", "+15135551212"],
	"From": "+12195551212",
	"sid": "ALongStringFromTwilio",
	"token": "AnotherLongStringFromTwilio",
}

```

## usage
An example named "test.py"

```python
import logging
from TwilioHandler.TWHandler import TWHandler

twconfig = {
	"recipients": [ "+18125551212", ], 
        "From": "+15135551212",
        "sid": "thesid",
        "token": "thetoken",
}

logger = logging.getLogger("twilio")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")

stream = logging.StreamHandler()
stream.setLevel(logging.INFO)
stream.setFormatter(formatter)
logger.addHandler(stream)

twh = TWHandler(twconfig) 
twh.setLevel(logging.WARNING)
twh.setFormatter(formatter)
logger.addHandler(twh)

logger.info("test")
logger.warning("sms test")
```
The StreamHandler will give you a nice heads up.
```bash
python ./test.py
2015-08-11 12:18:33,836 INFO test
2015-08-11 12:18:33,836 WARNING sms test
```

Your sms will arrive as a formatted json object as the body of the text.
```json
{
 "function": "<module>", 
 "host": "kreplach", 
 "file": "./test.py", 
 "logger name": "twilio", 
 "time": "2015-08-11 12:18:33,836", 
 "message": "sms test", 
 "error level": "WARNING", 
 "module": "test"
}
```

