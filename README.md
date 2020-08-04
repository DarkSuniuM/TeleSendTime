# TeleSendTime
TeleSendTime is a Python module for Telegram message automation.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install TeleSendTime.

```bash
pip install git+https://gitlab.com/DarkSuniuM/TeleSendTime.git
```

## Usage

```
# template.txt
# "$" prefixed words are variables
BTC Rate (USD): $rate
```

```python3
# app.py

import requests

from tele_sendtime import Automation
from tele_sendtime import load_template


automation = Automation('MY_BOT_TOKEN')


# chat_id => Chat ID or Chat Username
# interval in seconds.
@automation.job(load_template('template.txt', chat_id='@my_username', interval=60)
def send_btc_rate_in_usd():
    # Sample API Call
    req = requests.get('https://api.coindesk.com/v1/bpi/currentprice/USD.json')
    rate = req.json()['bpi']['USD']['rate_float']

    # return type should be a list of strings or dictianories
    # Use dict when there is a template
    return [{'rate': rate}] 


@automation.job(chat_id='@my_username', interval=60)
def send_btc_rate_in_eur():
    # Sample API Call
    req = requests.get('https://api.coindesk.com/v1/bpi/currentprice/EUR.json')
    rate = req.json()['bpi']['EUR']['rate_float']

    # When using String, Template get's ignored!
    return [f'BTC Price (EURO): {rate}']


# Run the automation bot.
automation.run()
```

## To Do
* Add to Pypi
* Add Documentation
* Improve Concurrency


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU LGPLv3](https://choosealicense.com/licenses/lgpl-3.0/)