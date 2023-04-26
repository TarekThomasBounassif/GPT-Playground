import sys

# Return size in KB to help estimate future db cost.
def get_size_kb(input_obj) -> float:
    size_in_bytes = sys.getsizeof(input_obj)
    return size_in_bytes / 1024
