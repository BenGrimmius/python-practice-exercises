# File Handling Exercise that can take any .txt file or .log file
# and can output the number of WARNINGS and ERRORS, the first ERROR, and the last ERROR.
# 
# TODO: replace input() with file_name = sys.argv[1]. (Need to import sys)
# TODO: Process multiple files in a folder need to import os and use logs/

import sys
from pathlib import Path
from datetime import datetime


def analyze_file(file_path, error_file):
    error_count = 0
    warning_count = 0

    first_error = None
    first_error_line = None

    last_error = None
    last_error_line = None

    try:
        with open(file_path) as log_file:

            for line_number, line in enumerate(log_file, start=1):
                clean_line = line.strip()

                if "WARNING" in clean_line.upper():
                    warning_count += 1

                elif "ERROR" in clean_line.upper():
                    error_count += 1
                    error_file.write(
                        f"{file_path.name} (line {line_number}): {line}"
                    )

                    if first_error is None:
                        first_error = clean_line
                        first_error_line = line_number

                    last_error = clean_line
                    last_error_line = line_number

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    return (
        error_count,
        warning_count,
        first_error,
        first_error_line,
        last_error,
        last_error_line,
    )


def main():

    if len(sys.argv) < 2:
        print("Usage: python analyze_folder.py <folder>")
        sys.exit()

    folder_path = Path(sys.argv[1])

    if not folder_path.exists():
        print("Folder not found.")
        sys.exit()

    if not folder_path.is_dir():
        print("Provided path is not a directory.")
        sys.exit()

    time_stamp = datetime.now().strftime("%H-%M-%S_%m-%d-%Y")

    error_output = Path(
        f"txt_files/errors/error_{time_stamp}.txt"
    )

    report_output = Path(
        f"txt_files/reports/report_{time_stamp}.txt"
    )

    total_errors = 0
    total_warnings = 0

    first_error = None
    first_error_line = None

    last_error = None
    last_error_line = None

    try:
        with open(error_output, "w") as error_file:

            for file_path in folder_path.glob("*"):

                if file_path.suffix.lower() not in [".log", ".txt"]:
                    continue

                print(f"Processing: {file_path.name}")

                (
                    error_count,
                    warning_count,
                    f_error,
                    f_line,
                    l_error,
                    l_line,
                ) = analyze_file(file_path, error_file)

                total_errors += error_count
                total_warnings += warning_count

                if first_error is None and f_error:
                    first_error = f_error
                    first_error_line = f_line

                if l_error:
                    last_error = l_error
                    last_error_line = l_line

    except PermissionError:
        print("Permission denied while writing output files.")
        sys.exit()

    try:
        with open(report_output, "w") as report_file:

            report_file.write(
                f"Total Errors: {total_errors}\n"
                f"Total Warnings: {total_warnings}\n"
                f"First Error (Line {first_error_line}): {first_error}\n"
                f"Last Error (Line {last_error_line}): {last_error}\n"
            )

    except PermissionError:
        print("Permission denied while writing report.")
        sys.exit()

    print("\nProcessing complete.")
    print("Total Errors:", total_errors)
    print("Total Warnings:", total_warnings)
    print("Report created:", report_output)


if __name__ == "__main__":
    main()