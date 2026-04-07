try:
    with open("server.log") as log_file:
        error_count: int = 0
        warning_count: int = 0
        first_error: str | None = None
        last_error: str | None = None

        with open("errors.txt", "w") as error_file:
                for line in log_file:
                    clean_line = line.strip()

                    if "WARNING" in clean_line:
                        warning_count += 1
                    elif  "ERROR" in clean_line:
                        error_count += 1
                        error_file.write(line)
                        if first_error == None:
                             first_error = clean_line

                        last_error = clean_line
                             
    if error_count > 0:
         print(f"First Error Line: {first_error}")
         print(f"Last Error Line: {last_error}")
    else:
         print("No Errors Found")
    print(f"Total Errors: {error_count}\nTotal Warnings: {warning_count}")

except FileNotFoundError:
    print("Log file not found.")