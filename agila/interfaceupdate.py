"""

def update_health_indicators():
    # Existing system resource updates...

    # SSH monitoring: open ports
    open_ports = get_open_ports()
    ssh_ports_label.config(text=f"Open SSH Ports:\n{open_ports}")

    # SSH monitoring: insecure files
    insecure_files = check_insecure_files()
    insecure_files_text = (
        "\n".join(insecure_files) if insecure_files else "No insecure files found"
    )
    insecure_files_label.config(text=f"Insecure Files:\n{insecure_files_text}")

    # Continue with the update loop
    root.after(1000, update_health_indicators)

------------------------------------------------------------------------------------

# Skapa och placera etiketter för SSH-övervakning
ssh_ports_label = tk.Label(
    root, text="Open SSH Ports: Checking...", font=("Helvetica", 12)
)
ssh_ports_label.pack(pady=10)

insecure_files_label = tk.Label(
    root, text="Insecure Files: Checking...", font=("Helvetica", 12)
)
insecure_files_label.pack(pady=10)

"""
