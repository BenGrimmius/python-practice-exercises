# File Handling Exercise that can take any .txt file or .log file
# and can output the number of WARNINGS and ERRORS, the first ERROR, and the last ERROR.
# 
# TODO: replace input() with file_name = sys.argv[1]. (Need to import sys)
# TODO: Process multiple files in a folder need to import os and use logs/

import os
import sys
from pathlib import Path
from datetime import datetime


try:

    if len(sys.argv) < 2:
        pass

    file_name = sys.argv[1]

    file_extension_path: str = ""
    time_stamp: str = datetime.now().strftime("%H:%M:%S %m-%d-%Y")

    if file_name[-3:] == "txt":
        file_extension_path = "txt_files/"
    elif file_name[-3:] == "log":
        file_extension_path = "logs/"
    else:
        print("Cannot find file.")

    with open(f"{file_extension_path}{file_name}") as log_file:
        error_count: int = 0
        warning_count: int = 0
        first_error: str | None = None
        first_error_line: int | None = None
        last_error: str | None = None
        last_error_line: int | None = None
        line_number = None

        with open(f"txt_files/errors/error_{time_stamp}.txt", "w") as error_file:
            for line_number, line in enumerate(log_file, start=1):
                clean_line = line.strip()

                if "WARNING" in clean_line.upper():
                    warning_count += 1
                elif "ERROR" in clean_line.upper():
                    error_count += 1
                    error_file.write(line)

                    if first_error is None:
                        first_error = clean_line
                        first_error_line = line_number

                    last_error = clean_line
                    last_error_line = line_number

            with open(f"txt_files/reports/report_{time_stamp}.txt", "w") as report_file:
                report_file.writelines(
                    f"Number of Errors: {error_count}\n"
                    f"Number of Warnings: {warning_count}\n"
                    f"First Error on line {first_error_line}: {first_error}\n"
                    f"Last Error on line {last_error_line}: {last_error}\n"
                )
                             
    if error_count > 0:
         print(f"\nFirst Error on line {first_error_line}: {first_error}")
         print(f"Last Error on line {last_error_line}: {last_error}")
    else:
         print("No Errors Found")
    print(f"Total Errors: {error_count}\nTotal Warnings: {warning_count}\n")

except FileNotFoundError:
    print("Log file not found.")