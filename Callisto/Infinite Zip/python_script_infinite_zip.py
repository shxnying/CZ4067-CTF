import os
import patoolib
import tempfile

def find_first_archive(directory):
    archive_exts = ['.zip', '.rar', '.tar', '.gz', '.bz2', '.xz', '.7z']
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if any(file_path.lower().endswith(ext) for ext in archive_exts):
            return file_path
    return None

def extract_nested_archive(file_path, output_dir=None):
    current_file = file_path
    while True:
        print(f"Extracting '{current_file}'...")  # Print current archive being extracted

        temp_outdir = tempfile.mkdtemp()
        try:
            patoolib.extract_archive(current_file, outdir=temp_outdir)
        except patoolib.util.PatoolError:
            print(f"Error: Unable to extract '{current_file}'.")
            break

        nested_archive = find_first_archive(temp_outdir)
        if nested_archive:
            current_file = nested_archive
        else:
            # Move extracted files to the output directory
            for root, dirs, files in os.walk(temp_outdir):
                for file in files:
                    src = os.path.join(root, file)
                    dst = os.path.join(output_dir, file)
                    os.rename(src, dst)
            # Clean up temporary directory
            os.rmdir(temp_outdir)
            break

initial_archive = "/home/kali/Desktop/test/infinite_zip.zip"  # Replace with the path to your initial archive
output_directory = "/home/kali/Desktop/open"  # Replace with the desired output directory (optional)

extract_nested_archive(initial_archive, output_dir=output_directory)
