# File Handling Exercise that can take any .txt file or .log file
# and can output the number of WARNINGS and ERRORS, the first ERROR, and the last ERROR.
# 
# TODO: send the error_count, the warning_count, the first error (with the line number), and the last error (with the line number) 


try:
    file_name = input("Enter log file name: ")

    with open(f"{file_name}.log") as log_file:
        error_count: int = 0
        warning_count: int = 0
        first_error: str | None = None
        last_error: str | None = None
        line_number: int | None = None

        with open("errors.txt", "w") as error_file:
                for line in log_file:
                    clean_line = line.strip()

                    if "WARNING" in clean_line:
                        warning_count += 1
                    elif  "ERROR" in clean_line:
                        error_count += 1
                        error_file.write(line)
                        if first_error is None:
                             first_error = clean_line
                             line_number = enumerate(first_error)
                             

                        last_error = clean_line
                with open("report.txt", "w") as report_file:
                        report_file.writelines(f"Number of Errors: {error_count}\nNumber of Warnings: {warning_count}\nFirst Warning")
                             
    if error_count > 0:
         print(f"First Error Line: {first_error}")
         print(f"Last Error Line: {last_error}")
    else:
         print("No Errors Found")
    print(f"Total Errors: {error_count}\nTotal Warnings: {warning_count}")

except FileNotFoundError:
    print("Log file not found.")