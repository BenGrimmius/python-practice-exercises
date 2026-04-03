try:
    with open("server.log") as log_file:
        error_count: int = 0
        warning_Count: int = 0

        with open("errors.txt", "w+") as error_file:

            for line in log_file:
                if "WARNING" in line:
                    warning_Count += 1
                elif  "ERROR" in line:
                    error_count += 1
                    error_file.write(line)
            first_line: str = error_file.readline()
            print(first_line)

            print(f"First error line: {first_line}")

    print(f"Total Errors: {error_count}\nTotal Warnings: {warning_Count}")
except FileNotFoundError:
    print("Log file not found.")