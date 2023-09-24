import os
import argparse


def du(path="."):

    if not os.path.exists(path):
        raise Exception("File path does not exist")

    total_size = 0
    start_path = os.path.join(path, "..")
    size_dict = {}

    for curr_dir, _, filenames in os.walk(path, topdown=True):
        for filename in filenames:
            file_path = os.path.join(curr_dir, filename)
            total_size += os.path.getsize(file_path)
            size_dict[os.path.relpath(file_path, start_path)] = to_dict_entry(
                file_path, start_path, False, os.path.getsize(file_path))

    print(f"\nRetrieving file size for {os.path.abspath(path)}\n\n")

    max_path_length = int(sum(len(s)
                          for s in size_dict.keys()) / len(size_dict.keys()))

    print(f"{'Path'.ljust(max_path_length)}  Size\n")
    for file_path, val in size_dict.items():
        displayed_path = truncate_middle(file_path, max_path_length)
        padded_path = displayed_path.ljust(max_path_length)
        print(f"{padded_path}  {val.get('size', 'N/A')}")

    print(f"\n\nTotal size: {format_size(total_size)}")


def truncate_middle(path, max_length):
    if len(path) <= max_length:
        return path

    mid = max_length // 2
    return f"{path[:mid - 2]}...{path[-(mid - 1):]}"


def to_dict_entry(path, start, is_dir, size=0.0):
    return {
        "relpath": os.path.relpath(path, start),
        "isdir": is_dir or os.path.isdir(path),
        "size": format_size(size)
    }


def format_size(size):
    for unit in ["B", "KB", "MB", "GB"]:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Disk utility")
    parser.add_argument("directory", metavar="directory", nargs="?",
                        default=".", type=str, help="Directory to inspect")
    args = parser.parse_args()

    root_dir = args.directory
    du(root_dir)
