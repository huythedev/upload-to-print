## Installation
 * Install [**python**](https://www.python.org/downloads/) if you doesn't have it on your machine
 * Open cmd in the source code directory
 * Run `pip install -r requirements.txt` or `pip3 install -r requirements.txt`

## Configuration

 * In _**config.ini**_ , change _**name**_ to your printer name (you can type `Control Panel\Hardware and Sound\Devices and Printers` as a directory in _**Explorer**_, right click at the printer you want to be used and choose _**Printer properties**_ then replace the name in config file with your printer name)
 * You can also change the port for the application in **config.ini**

## Usage

 * If you want it to run in background, just double click the file **wsgi.pyw**. Else run `python wsgi.py` or `python3 wsgi.py`
 * Go to `localhost:5000` if you don't change the port in _**config.ini**_ or `localhost:[the port you set in config.ini]` and done :)
 * To stop the program, open task manager and **end task** all python processes(if you run in background) or **Ctrl + C** in cmd
