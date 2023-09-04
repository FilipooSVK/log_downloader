# **Log Downloader**

## Overview

The Log Downloader is a Python script with a graphical user interface (GUI) built using the Tkinter library. It allows users to download log files from a remote server via SSH, remove them from the remote server, and save information about the downloaded logs in a JSON file.

## **Features**

**SSH Connectivity**: Users are prompted to enter their SSH username and password to connect to a remote server.

**Download Logs**: The script lists log files in a specified source folder on the remote server, allowing users to download them to a local directory.

**Progress Bar**: A progress bar using the tqdm library displays the download progress.

**Removal from Remote**: After successful download, the script removes the downloaded log files from the remote server to save space.

**Save to JSON**: The script allows users to save information about the downloaded logs, including the server hostname, username, source folder, and a list of downloaded log files, to a JSON file.

**Browse for Local Directory**: Users can choose the local directory where log files will be downloaded.

**Exit Button**: An exit button allows users to close the application.

## **Instructions**

Run the script, and the GUI window will appear.

Enter your SSH username and password when prompted.

Enter the hostname of the remote server and the source folder where the log files are located.

Click the "Download Logs" button to initiate the download process.

A progress bar will display the download progress for each log file.

Once the download is complete, the script will remove the downloaded log files from the remote server.

You can click the "Save JSON" button to save information about the downloaded logs in a JSON file.

You can also click the "Browse" button to choose a different local directory for log file downloads.

To exit the application, click the "Exit" button.

## Getting Started

Requirements: Ensure you have Python 3.x installed along with the required libraries: Paramiko for SSH connectivity, Tkinter for GUI, and tqdm for the progress bar.

Clone the Repository: Clone this repository to your local machine using the following command:

bash
Copy code

`git clone https://github.com/your-username/log-downloader.git`

Run the Script: Navigate to the project directory and run the script:

bash

Copy code
cd log-downloader
python main.py
Use the GUI: The graphical user interface will appear. Follow the on-screen instructions to connect to a remote server, download logs, and manage them.

## Compatibility
This script has been tested on Windows but is designed to be cross-platform. It should work on other operating systems with minimal adjustments.

## Contribution
Contributions are welcome! If you'd like to enhance or customize this script, please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License, which means you're free to use and modify it for personal or commercial purposes.
