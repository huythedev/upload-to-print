import os
import configparser
from concurrent.futures import ThreadPoolExecutor
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import win32print
import win32api

app = Flask(__name__)

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')

# Printer name
PRINTER_NAME = config.get('Printer', 'name')

#Port
PORT = config.getint('Server', 'port')

# Upload folder
UPLOAD_FOLDER = config.get('Upload', 'directory')
UPLOAD_FOLDER = os.path.join(os.getcwd(), UPLOAD_FOLDER)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Print job history
print_history = []

def allowed_file(filename):
    # Allow all file types for now
    return True

def print_to_printer(file_path, printer_name):
    try:
        printer_handle = win32print.OpenPrinter(printer_name)
        win32print.StartDocPrinter(printer_handle, 1, ("Test Print", None, "RAW"))
        win32print.StartPagePrinter(printer_handle)
        with open(file_path, 'rb') as f:
            data = f.read()
        win32api.ShellExecute(0, "print", file_path, None, ".", 0)
        win32print.EndPagePrinter(printer_handle)
        win32print.EndDocPrinter(printer_handle)
        win32print.ClosePrinter(printer_handle)
    except Exception as e:
        print(f"Error printing to printer: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_and_print():
    print("Received POST request to /upload")
    
    if 'files' not in request.files:
        print("No files uploaded")
        return "No files uploaded"

    files = request.files.getlist('files')
    print(f"Received {len(files)} file(s)")

    for file in files:
        if file.filename == '':
            print("No file selected")
            return "No file selected"
        print(f"Received file: {file.filename}")

        # Securely save file
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)

        # Print to printer in background
        with ThreadPoolExecutor() as executor:
            executor.submit(print_to_printer, file_path, PRINTER_NAME)

        # Add to print history
        print_history.append({'file': filename, 'printer': PRINTER_NAME})

    return "Files uploaded and printing..."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=PORT)
