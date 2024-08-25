import tkinter as tk
import psutil
import os
import subprocess
import stat
import argparse

# Define thresholds for warnings
CPU_THRESHOLD = 80  # example threshold in percentage
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
NETWORK_THRESHOLD = 100  # in MB

# Variables to store previous network counters
prev_net_sent = 0
prev_net_recv = 0


# Argument parsing for thresholds
def parse_arguments():
    parser = argparse.ArgumentParser(description="Health Indicator Warning System")
    parser.add_argument(
        "--cpu", type=int, default=CPU_THRESHOLD, help="CPU usage warning threshold"
    )
    parser.add_argument(
        "--memory",
        type=int,
        default=MEMORY_THRESHOLD,
        help="Memory usage warning threshold",
    )
    parser.add_argument(
        "--disk", type=int, default=DISK_THRESHOLD, help="Disk usage warning threshold"
    )
    parser.add_argument(
        "--network",
        type=int,
        default=NETWORK_THRESHOLD,
        help="Network usage warning threshold",
    )
    return parser.parse_args()


# Apply thresholds from arguments
args = parse_arguments()
CPU_THRESHOLD = args.cpu
MEMORY_THRESHOLD = args.memory
DISK_THRESHOLD = args.disk
NETWORK_THRESHOLD = args.network


# Function to get open SSH ports
def get_open_ports():
    try:
        result = subprocess.check_output(["ss", "-tuln"], text=True)
        return result.strip()
    except Exception as e:
        return f"Error retrieving open ports: {e}"


# Function to check for insecure file permissions
def check_insecure_files(path="/etc"):
    insecure_files = []
    for root, dirs, files in os.walk(path):
        for name in files:
            full_path = os.path.join(root, name)
            try:
                mode = os.stat(full_path).st_mode
                if mode & stat.S_IROTH:
                    insecure_files.append(full_path)
            except Exception as e:
                pass
    return insecure_files


# Function to update health indicators
def update_health_indicators():
    global prev_net_sent, prev_net_recv

    # CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        cpu_label.config(fg="red")
    else:
        cpu_label.config(fg="black")

    # Memory usage
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    memory_label.config(text=f"Memory Usage: {memory_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        memory_label.config(fg="red")
    else:
        memory_label.config(fg="black")

    # Disk usage
    disk_info = psutil.disk_usage("/")
    disk_usage = disk_info.percent
    disk_label.config(text=f"Disk Usage: {disk_usage}%")
    if disk_usage > DISK_THRESHOLD:
        disk_label.config(fg="red")
    else:
        disk_label.config(fg="black")

    # Network usage
    net_info = psutil.net_io_counters()
    net_sent = net_info.bytes_sent / (1024 * 1024)  # Convert to MB
    net_recv = net_info.bytes_recv / (1024 * 1024)  # Convert to MB

    # Calculate usage per second
    sent_per_sec = net_sent - prev_net_sent
    recv_per_sec = net_recv - prev_net_recv

    network_label.config(
        text=f"Network: Sent: {sent_per_sec:.2f} MB/s, Recv: {recv_per_sec:.2f} MB/s"
    )
    if sent_per_sec > NETWORK_THRESHOLD or recv_per_sec > NETWORK_THRESHOLD:
        network_label.config(fg="red")
    else:
        network_label.config(fg="black")

    # Update previous counters
    prev_net_sent = net_sent
    prev_net_recv = net_recv

    # SSH monitoring: open ports
    open_ports = get_open_ports()
    ssh_ports_label.config(text=f"Open SSH Ports:\n{open_ports}")

    # SSH monitoring: insecure files
    insecure_files = check_insecure_files()
    insecure_files_text = (
        "\n".join(insecure_files) if insecure_files else "No insecure files found"
    )
    insecure_files_label.config(text=f"Insecure Files:\n{insecure_files_text}")

    # Update again after 1000 ms (1 second)
    root.after(1000, update_health_indicators)


# Create the Tkinter window
root = tk.Tk()
root.title("Health Indicators")

# Create and place labels for each health indicator
cpu_label = tk.Label(root, text="CPU Usage: Calculating...", font=("Helvetica", 12))
cpu_label.pack(pady=10)

memory_label = tk.Label(
    root, text="Memory Usage: Calculating...", font=("Helvetica", 12)
)
memory_label.pack(pady=10)

disk_label = tk.Label(root, text="Disk Usage: Calculating...", font=("Helvetica", 12))
disk_label.pack(pady=10)

network_label = tk.Label(root, text="Network: Calculating...", font=("Helvetica", 12))
network_label.pack(pady=10)

# Create and place labels for SSH monitoring
ssh_ports_label = tk.Label(
    root, text="Open SSH Ports: Checking...", font=("Helvetica", 12)
)
ssh_ports_label.pack(pady=10)

insecure_files_label = tk.Label(
    root, text="Insecure Files: Checking...", font=("Helvetica", 12)
)
insecure_files_label.pack(pady=10)

# Start updating health indicators
update_health_indicators()

# Start the Tkinter main loop
root.mainloop()
