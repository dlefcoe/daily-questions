'''

module to perform a backup of files and folders.

the user can specify: 
 - source folder
 - destination folder
 - cut off date

All files that are `newer` than the cutoff date are copied
from the `source folder` to the `destination folder` maintaining the
original tree structure of the `source folder`.

'''

# %%

import shutil
import os
import time
from datetime import datetime
import json

import PySimpleGUI as sg


def main():
    ''' the main module '''

    # inputs file is in the same directory as the program
    path = os.path.abspath(__file__)
    path = os.path.dirname(path)
    input_file_path = os.path.join(path, 'inputs.json')
    
    # read the data 
    initial_params = read_data(input_file_path)
    print('the inputs are:')
    print(json.dumps(initial_params, indent=4))


    # Set the source and destination paths (suggestions)
    source = initial_params['source folder'] 
    destination = initial_params['destination folder']

    # Set the cutoff date for new files (in seconds since the epoch)
    cutoff_date_string = initial_params['cut off date']
    cutoff_date = time.mktime(time.strptime(cutoff_date_string, "%Y-%m-%d"))

    try:
        source, destination, cutoff_date = gui(
            source, 
            destination, 
            cutoff_date_string)
        if cutoff_date == None:
            return
    except Exception as e:
        print('close button probably pressed')
        print(e)
        return

    result = {}
    result['current time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    result['source folder'] = source
    result['destination folder'] = destination
    dt = datetime.fromtimestamp(cutoff_date)
    result['cut off date'] = dt.strftime("%Y-%m-%d")

    n = how_many_files(source, cutoff_date)
    # print(f"Backing up {n} new files.")
    result['files to backup'] = n
    n = perform_backup(source, destination, cutoff_date)
    # print(f"Backup complete! {n} files copied.")
    result['backed up files'] = n
    print('the data is backed up:')
    print(json.dumps(result, indent=4))
    # write result to a json file
    with open('results.json', 'w') as f:
        json.dump(result, f, indent=4)

# %%

def read_data(input_file:str)->dict:
    ''' file to read the basic data inputs 
    
    args:
        input_file (str): path to input file that contains the data

    return:
        a python dict with the data
    '''

    # Open the JSON file
    with open(input_file, "r") as f:
        # Load the JSON data from the file
        data = json.load(f)

    return data


# %%
def gui(source, destination, cutoff_date):
    # Define the layout of the app
    layout = [[sg.Text("Enter the source file path:")],
            [sg.InputText(source)],
            [sg.Text("Enter the destination file path:")],
            [sg.InputText(destination)],
            [sg.Text("Enter the cutoff date (YYYY-MM-DD):")],
            [sg.InputText(cutoff_date)],
            [sg.Button("OK"), sg.Button("Close"), sg.Button("Date")]
            ]

    # Create the window
    window = sg.Window("File Path Input", layout)

    # Run the event loop to capture user input
    while True:
        event, values = window.read()
        if event == "OK":
            # Get the inputted file paths and cutoff date
            source_path = values[0]
            dest_path = values[1]
            cutoff_date = values[2]
            try:
                cutoff_date = time.mktime(time.strptime(cutoff_date, "%Y-%m-%d"))
            except Exception as e:
                cutoff_date = None
            # Close the window
            window.close()
            break
        elif event == "Close":
            # Close the window
            window.close()
            break
        elif event == "Date":
            # Set the inputted date to the current date
            now = datetime.now()
            window["Date"].update(now.strftime("%Y-%m-%d"))

    # Return the inputted file paths and cutoff date
    return source_path, dest_path, cutoff_date


def how_many_files(source:str, cutoff_date:str):
    '''
    function to determine how many files need to be updated.

    args:
        source (str): path of the source folder
        cutoff_date (str): string of a date in this format "2022-01-01"

    return:
        number of files that will be backed up
    '''
    # Initialize a counter for the number of files to be backed up
    num_files_to_backup = 0

    # Use the os.walk() function to iterate over all files and directories in the source drive
    for root, dirs, files in os.walk(source):
        for file in files:
            # Get the full path of the file
            src_path = os.path.join(root, file)
            # Get the modification time of the file
            mtime = os.stat(src_path).st_mtime
            # Check if the file was modified after the cutoff date
            if mtime > cutoff_date:
                # Increment the counter
                num_files_to_backup += 1

    # return the number of files to be backed up
    return num_files_to_backup


def perform_backup(source:str, destination:str, cutoff_date:str):
    '''
    function to perform the backup

    args:
        source (str): path of the source folder
        destination (str): path of the destination folder
        cutoff_date (str): string of a date in this format "2022-01-01"

    return:
        number of files that will have backed up

    
    '''
    # Initialize a counter for the number of files copied
    num_files_copied = 0

    # Use the shutil.copytree() function to copy the entire source 
    # drive to the destination
    for root, dirs, files in os.walk(source):
        for file in files:
            # Get the full path of the file
            src_path = os.path.join(root, file)
            # Get the modification time of the file
            mtime = os.stat(src_path).st_mtime
            # Check if the file was modified after the cutoff date
            if mtime > cutoff_date:
                # Calculate the relative path of the file
                rel_path = os.path.relpath(src_path, source)
                # Calculate the destination path of the file
                dest_path = os.path.join(destination, rel_path)
                # Create any necessary parent directories
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                # Copy the file to the destination
                shutil.copy2(src_path, dest_path)
                # Increment the counter
                num_files_copied += 1

    # return a success message with the number of files copied
    return num_files_copied
