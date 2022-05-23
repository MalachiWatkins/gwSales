# Goodwill Sales Dashboard
This app is a Dashboard for seeing listers sales for a specific month
it uses the Uprightlabs API to search for all sold items with a specific created at date.

## Prerequisites
You will need an API token for your store, provided by uprightlabs (Contact them about setting one up)
This script requires Python and the requests package to be installed for it to run, I highly recommend Installing the Microsoft store version
of python 3.9.

![alt text](https://phoenixnap.com/kb/wp-content/uploads/2021/08/starting-python-3-9-installation-in-microsoft-store.png)

Once Python is installed open Windows command prompt by pressing the Windows key and R
a window will pop up type cmd to open a command prompt. and enter the command below.
```
pip install requests
```
When the installation is finished you can close command prompt.
## Usage
This does use an API with a lot of data parsing.
It will take a while depending on the lister and
how many items they have sold.

Do not panic if it seems like it is not working, some listers have thousands of items
to parse through.

Clone this repository and unzip into a folder.
Then create a desktop shortcut to Dashboard.pyw

## Configuration
The api token is in Dashboard.pyw line 13 .
```
API_TOKEN = 'YOU KEY GOES IN HERE'

```
As far as Listers and the Listers id, there is no reliable way to get the lister IDS.
If your store wants to use this app feel free to Contact me and I can work with you on setup.
## Contribute
If you would like to Contribute feel free to submit a pull request.
