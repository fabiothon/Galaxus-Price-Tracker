# Galaxus Price Tracker

This Python script tracks prices of multiple specific products on www.galaxus.ch and alerts the user via email if the prices reaches a defined alert price. The script can be automatised with cronjob or windows task scheduler to run every 24h.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) and the provided requirements.txt file to install this script. This script is optimised for macOS and thus uses the keyring package to safely store and access necessary keys. Ignore if you use a different operating system.

```bash
pip install -r /path/to/requirements.txt
`````

## Google API
This script uses the Google API to send mail and thus credentials.json is needed to access the Google API. More information: https://developers.google.com/workspace/guides/create-credentials

### Notification E-Mails

<img width="1464" alt="Picture" src="https://github.com/fabiothon/Galaxus_Price_Tracker/blob/7e415fb3cad11c7d2c5c7b600e3d0563bf7111a7/picture_1.png">

## Usage

1. Download of all necessary files (main.py, requirements.txt, products.csv and credentials.json)
2. Install necessary libraries on your local environment or virtual environment via the requirement.txt
3. Get access to the Google API and fill in all necessary information into the products and credentials files
4. Run application
5. Use cronjob or other tools to automatise the process

## Contributing

Pull requests are welcome! For major changes, please open an issue first
to discuss what you would like to change.
Please make sure to update tests as appropriate.

## Licenses
This script uses the [MIT](https://choosealicense.com/licenses/mit/) License.