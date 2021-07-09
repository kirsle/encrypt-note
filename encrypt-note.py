#!/usr/bin/env python3

import os
import getpass
import subprocess
import shutil

NOTES_DIR = "./notes"
OUTPUT_DIR = "./out"

def main():
    # Collect the input files.
    infiles = next(os.walk(NOTES_DIR), (None, None, []))[2]
    print("Going to encrypt the files in ./notes:")
    for filename in infiles:
        print(f"  - {filename}")
    print("")

    # Prepare the output directory.
    if not os.path.isdir(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)

    # Password to encrypt with.
    password = getpass.getpass(prompt='Password: ', stream=None)
    confirm = getpass.getpass(prompt='Confirm: ', stream=None)
    if not password:
        print("Password to encrypt is required.")
        os.exit(1)
    elif password != confirm:
        print("The passwords did not match.")
        os.exit(1)

    # Run the 7zip command on the whole folder.
    os.chdir(NOTES_DIR)
    print("* Create 7zip archive of entire folder")
    subprocess.run([
        "7z",
        "a", # add to archive
        f"../{OUTPUT_DIR}/notes.7z",
        "*",
        f"-p{password}",
    ])

    # GPG encrypt each file additionally.
    for filename in infiles:
        print(f"* GPG encrypt: {filename}")
        subprocess.run([
            "gpg",
            "--passphrase", password,
            "--pinentry-mode", "loopback",
            "--symmetric",
            filename,
        ])
        os.rename(f"{filename}.gpg", f"../{OUTPUT_DIR}/{filename}.gpg")
    
    # Copy the documentation file in.
    os.chdir("..")
    shutil.copy("./Decrypting.md", "./out/Decrypting.md")

if __name__ == "__main__":
    main()