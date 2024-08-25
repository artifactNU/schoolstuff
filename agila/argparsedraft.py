import argparse


# Define argparse for thresholds
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
