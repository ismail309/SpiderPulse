def log(message):
    with open("logs.txt", "a") as log_file:
        log_file.write(f"{message}\n")
    print(message)