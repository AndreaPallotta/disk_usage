import os

# def calculate_size(path, size_dict, total_size):
#     file_size = os.path.getsize(path)

#     if os.path.isfile(path):
#         return total_size + file_size

#     if os.path.isdir(path):
#         for dirpath, dirname, filenames in os.walk(path):
            
#             return calculate_size(path, size_dict, total_size)
    
#     return total_size

def du(path="."):

    if not os.path.exists(path):
        raise Exception("File path does not exist")

    total_size = 0
    size_dict = {
        path: os.path.relpath(path, os.path.join(path, ".."))
    }

    print(f"Retrieving file size for {os.path.abspath(path)}\n\n")
    print(size_dict)
    print(f"Total size: {total_size}B")

if __name__ == "__main__":
    du()
    