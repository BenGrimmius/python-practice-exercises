with open("server.log", "r") as file:
    errorLineCount: int = 0
    for line in file:
        if "ERROR" in line:
            errorLineCount += 1
            with open("errors.txt", "w")
    print(f"There are {errorLineCount} errors")

