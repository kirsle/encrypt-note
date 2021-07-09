# encrypt-note

A simple script to create encrypted notes using bog standard
encryption tools, with instructions how to decrypt them.

It takes your files from the `notes/` directory and encrypts
them into password-protected containers using commonly
available file formats.

## Usage

Write notes in the `notes/` folder, as standard Markdown .md files
or whatever you like really, plain text may be best.

And then just run the `encrypt-note.py` script. If you have GNU Make
available, the `make` command will run the script for shorthand.

It will prompt you for the symmetric encryption pass phrase and then
encrypt each of the files in the `notes/` folder into several files
in the `out/` folder.

## Output Formats

The `out/` folder will contain:

* `notes.7z`: A **7zip** password-protected archive of all of your
  notes together.
* `*.gpg` files: each of your notes individually encrypted using bog
  standard GPG/PGP symmetric keys, following the GNU Privacy Guard or
  Pretty Good Privacy standard.
* `README.txt` containing instructions how to open these files.

## Example



```bash
% make
# --OR--
% python3 encrypt-note.py
Going to encrypt the files in ./notes:
  - Hello-World.md

Password: 
Confirm: 
* Create 7zip archive of entire folder
* GPG encrypt: Hello-World.md

% ls out/
Hello-World.md.gpg  notes.7z

% gpg -d out/Hello-World.md.gpg 
gpg: AES.CFB encrypted data
gpg: encrypted with 1 passphrase
# Hello World

An example note to be encrypted.
```