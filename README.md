#Log Downloader
#Overview
#The Log Downloader is a Python script with a graphical user interface (GUI) built using the Tkinter library. It allows users to download log files from a remote server via SSH, remove them from the remote server, and save information about the downloaded logs in a JSON file.

#Features
#SSH Connectivity: Users are prompted to enter their SSH username and password to connect to a remote server.

#Download Logs: The script lists log files in a specified source folder on the remote server, allowing users to download them to a local directory.

#Progress Bar: A progress bar using the tqdm library displays the download progress.

#Removal from Remote: After successful download, the script removes the downloaded log files from the remote server to save space.

#Save to JSON: The script allows users to save information about the downloaded logs, including the server hostname, username, source folder, and a list of downloaded log files, to a JSON file.

#Browse for Local Directory: Users can choose the local directory where log files will be downloaded.

#Exit Button: An exit button allows users to close the application.

#Instructions
#Run the script, and the GUI window will appear.

Enter your SSH username and password when prompted.

Enter the hostname of the remote server and the source folder where the log files are located.

Click the "Download Logs" button to initiate the download process.

A progress bar will display the download progress for each log file.

Once the download is complete, the script will remove the downloaded log files from the remote server.

You can click the "Save JSON" button to save information about the downloaded logs in a JSON file.

You can also click the "Browse" button to choose a different local directory for log file downloads.

To exit the application, click the "Exit" button.

Requirements
Python 3.x
Paramiko library (for SSH connectivity)
Tkinter library (for GUI)
tqdm library (for the progress bar)
Compatibility
This script has been tested on Windows, but it should also work on other platforms with minor adjustments.
