import os
import hashlib
import csv
import sys

def file_hash_hex(file_path, hash_func):
    with open(file_path, 'rb') as f:
        return hash_func(f.read()).hexdigest()

def recursive_file_listing(base_dir):
    for directory, subdirs, files in os.walk(base_dir):
        for filename in files:
            yield directory, filename, os.path.join(directory, filename)

print("directory is " + (sys.argv[1]))
srcdir = sys.argv[1]


with open('checksums.tsv', 'w') as f:
    writer = csv.writer(f, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for directory, filename, path in recursive_file_listing(srcdir):
        try:
            writer.writerow((directory, filename, file_hash_hex(path, hashlib.md5), file_hash_hex(path, hashlib.sha1), file_hash_hex(path, hashlib.sha256), file_hash_hex(path, hashlib.sha512)))
        except Exception:
            print("error on " + directory + " " + filename)
            pass
