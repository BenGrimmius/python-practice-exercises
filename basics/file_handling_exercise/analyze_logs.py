try:
    with open("server.log") as log_file:
        error_count: int = 0
        warning_count: int = 0

        with open("errors.txt", "w+") as error_file:

            for line in log_file:
                if "WARNING" in line:
                    warning_count += 1
                elif  "ERROR" in line:
                    error_count += 1
                    error_file.write(line)
            error_file.seek(0)
            first_line: str = error_file.readline()

            print(f"First error line: {first_line}\nLast error line: {error_file.readlines()[-1]}")

    print(f"Total Errors: {error_count}\nTotal Warnings: {warning_count}")
except FileNotFoundError:
    print("Log file not found.")