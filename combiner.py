import datetime
import os
import sys


def combine_files(root_dir, output_dir="combined"):
    # Create combined directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Prepare the output file name with the current datetime
    datetime_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"combined_{datetime_str}.py")

    with open(output_file, "w") as outfile:
        for subdir, dirs, files in os.walk(root_dir):
            for file in files:
                if file.endswith(".py") and not file.startswith("__init__"):
                    file_path = os.path.join(subdir, file)
                    # Write start tag
                    outfile.write(f"# STARTFILE {file_path}\n")
                    with open(file_path) as infile:
                        outfile.write(infile.read() + "\n")
                    # Write end tag
                    outfile.write(f"# ENDFILE\n\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python combiner.py <directory>")
        sys.exit(1)

    combine_files(sys.argv[1])
