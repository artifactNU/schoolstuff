import os
import subprocess
import stat


# Additional function to monitor open ports
def get_open_ports():
    try:
        result = subprocess.check_output(["ss", "-tuln"], text=True)
        return result.strip()
    except Exception as e:
        return f"Error retrieving open ports: {e}"


# Additional function to check for insecure file permissions
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
