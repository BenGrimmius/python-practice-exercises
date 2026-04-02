with open("server.log") as logFile:
    errorLineCount: int = 0
    for line in logFile:
        if "ERROR" in line:
            errorLineCount += 1
            with open("errors.txt", "w") as file:
                file.write(line)
    print(f"There are {errorLineCount} errors")

