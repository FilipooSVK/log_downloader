import os
import paramiko
import json
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from tkinter import ttk  # Import ttk for themed widgets
from tqdm import tqdm  # Import tqdm for the progress bar

# Global variables
local_dir = r'C:\RPI'  # Default local directory
log_data = {}  # Dictionary to store log data
hostname = ""  # Default hostname
source_folder = ""  # Default source folder

def save_json():
    global log_data, local_dir

    if 'log_data' in locals():
        # Specify the path to the JSON file you want to create
        json_file_path = os.path.join(local_dir, "log_data.json")

        # Create and write the JSON data to the file
        with open(json_file_path, "w") as json_file:
            json.dump(log_data, json_file, indent=4)

        status_label.config(text=f"Log download and removal completed. JSON data written to {json_file_path}")
    else:
        status_label.config(text="No log data to save.")

def download_and_remove_logs():
    global local_dir, log_data, hostname, source_folder

    # Prompt the user for SSH username and password
    username = simpledialog.askstring("Input", "Enter SSH Username:")
    password = simpledialog.askstring("Input", "Enter SSH Password:", show='*')

    if username is None or password is None:
        return

    # SSH Connection Details
    port = 22

    # Create a Paramiko SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Check if hostname and source_folder are empty
    if not hostname:
        hostname = simpledialog.askstring("Input", "Enter Hostname:")

        if hostname is None:
            return

    if not source_folder:
        source_folder = simpledialog.askstring("Input", "Enter Source Folder:")

        if source_folder is None:
            return

    # SSH Connection Details
    port = 22

    # Create a Paramiko SSH client
    ssh_client = paramiko.SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Create a list to store downloaded and removed files
    downloaded_and_removed_files = []

    try:
        # Connect to the remote server
        ssh_client.connect(hostname, port, username, password)

        # Determine the source folder dynamically based on user input
        source_dir = source_folder

        # List files in the remote directory
        remote_files = ssh_client.exec_command(f'ls {source_dir}')[1].read().decode().split()

        # Ensure the local directory exists
        os.makedirs(local_dir, exist_ok=True)

        # Create a progress bar
        progress = ttk.Progressbar(root, mode='determinate', length=300)
        progress.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        # Set the maximum value for the progress bar
        progress['maximum'] = len(remote_files)

        # Download each log file and delete it from the remote directory with tqdm progress bar
        for i, remote_file in enumerate(remote_files):
            remote_path = os.path.join(source_dir, remote_file)
            local_path = os.path.join(local_dir, remote_file)
            sftp = ssh_client.open_sftp()
            sftp.get(remote_path, local_path)
            sftp.remove(remote_path)  # Remove the file from the remote directory
            sftp.close()
            downloaded_and_removed_files.append(remote_file)
            # Update the progress bar
            progress['value'] = i + 1
            root.update_idletasks()

        print("Log download and removal completed.")

    except paramiko.AuthenticationException:
        messagebox.showerror("Authentication Error", "Authentication failed. Please check your credentials.")
    except paramiko.SSHException as e:
        messagebox.showerror("SSH Error", f"SSH error: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        # Close the SSH connection
        ssh_client.close()

        # Destroy the progress bar
        progress.destroy()

    # Update the log_data dictionary
    log_data = {
        "Hostname": hostname,
        "Username": username,
        "SourceFolder": source_folder,
        "DownloadedAndRemovedFiles": downloaded_and_removed_files
    }

    # Update the status label
    status_label.config(text="Log download and removal completed.")

def browse_local_dir():
    global local_dir, local_dir_entry
    local_dir = filedialog.askdirectory()
    local_dir_entry.delete(0, tk.END)
    local_dir_entry.insert(0, local_dir)

def exit_program():
    # This function is called when the exit button is clicked
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Log Downloader")

# Create and configure GUI elements
download_button = tk.Button(root, text="Download Logs", command=download_and_remove_logs)
save_button = tk.Button(root, text="Save JSON", command=save_json)
browse_button = tk.Button(root, text="Browse", command=browse_local_dir)
exit_button = tk.Button(root, text="Exit", command=exit_program)  # Added exit button

# Define the local_dir_label widget here
local_dir_label = tk.Label(root, text="Local Directory:")
hostname_label = tk.Label(root, text="Hostname:")  # Added hostname label
source_dir_label = tk.Label(root, text="Source Folder:")  # Added source folder label

local_dir_entry = tk.Entry(root)
hostname_entry = tk.Entry(root)  # Added hostname entry field
source_dir_entry = tk.Entry(root)  # Added source folder entry field
status_label = tk.Label(root, text="")

# Arrange GUI elements using grid layout
local_dir_label.grid(row=0, column=0, padx=5, pady=5)
local_dir_entry.grid(row=0, column=1, padx=5, pady=5)
browse_button.grid(row=0, column=2, padx=5, pady=5)
hostname_label.grid(row=1, column=0, padx=5, pady=5)  # Added hostname label
hostname_entry.grid(row=1, column=1, padx=5, pady=5)  # Added hostname entry field
source_dir_label.grid(row=2, column=0, padx=5, pady=5)  # Added source folder label
source_dir_entry.grid(row=2, column=1, padx=5, pady=5)  # Added source folder entry field
download_button.grid(row=3, column=0, padx=5, pady=5)
save_button.grid(row=3, column=1, padx=5, pady=5)
exit_button.grid(row=3, column=2, padx=5, pady=5)  # Added exit button
status_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Initialize the local directory to your default value
local_dir_entry.insert(0, local_dir)
hostname_entry.insert(0, hostname)  # Initialize hostname entry
source_dir_entry.insert(0, source_folder)  # Initialize source folder entry

# Start the GUI event loop
root.mainloop()
