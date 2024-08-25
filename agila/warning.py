# Define thresholds for warnings
CPU_THRESHOLD = 80  # example threshold in percentage
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
NETWORK_THRESHOLD = 100  # in MB


def update_health_indicators():
    # Existing system resource updates...

    # Check CPU usage threshold
    if cpu_usage > CPU_THRESHOLD:
        cpu_label.config(fg="red")
    else:
        cpu_label.config(fg="black")

    # Check memory usage threshold
    if memory_usage > MEMORY_THRESHOLD:
        memory_label.config(fg="red")
    else:
        memory_label.config(fg="black")

    # Check disk usage threshold
    if disk_usage > DISK_THRESHOLD:
        disk_label.config(fg="red")
    else:
        disk_label.config(fg="black")

    # Check network usage threshold
    if sent_per_sec > NETWORK_THRESHOLD or recv_per_sec > NETWORK_THRESHOLD:
        network_label.config(fg="red")
    else:
        network_label.config(fg="black")

    # SSH monitoring and existing update logic...
