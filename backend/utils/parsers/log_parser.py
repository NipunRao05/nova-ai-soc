def read_log_file(filepath):

    with open(filepath, "r", errors="ignore") as f:
        content = f.read()

    return content