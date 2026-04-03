with open("server.log") as log_file:
    errorCount: int = 0
    warningCount: int = 0

    with open("errors.txt", "w") as error_file:
        for line in log_file:
            if "WARNING" in line:
                warningCount += 1
            if "ERROR" in line:
                errorCount += 1
                error_file.write(line)
print(f"Total Errors: {errorCount}\nTotal Warnings: {warningCount}")