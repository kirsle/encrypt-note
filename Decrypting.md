# About These Files

You have received an encrypted note! The message is encrypted in a
variety of standard and widely available formats with the hopes that
one of them can work.

You are expected to already know the passphrase that these files
were encrypted with. Hopefully, whoever pointed you to these files
has given you the encryption password.

The files here include:

| Filename      | Description                                         |
|---------------|-----------------------------------------------------|
| notes.7z      | 7-Zip archive containing all of the notes (easiest) |
| *.gpg         | Each note individually encrypted in GPG/PGP format  |
| Decrypting.md | This document!                                      |

The notes are encrypted redundantly in different formats. If you can
get the .7z file open, you have the full set of notes and you can
forget about the .gpg files. If you can't get at these files using
any of the methods written below, ask your closest computer geek friend
to help you out.

# Requirements

The following software will be helpful to open these files.

| Name     | Description                                   |
|----------|-----------------------------------------------|
| p7zip    | 7-Zip for opening the .7z file                |
| gnupg    | GNU Privacy Guard (GPG) to decrypt .gpg files |

7-Zip has a graphical program for Windows and Mac OS available
at https://www.7-zip.org/

These programs can all be installed trivially on Mac OS and
Linux computers using the names given in the table above.

On Windows 10 with the Windows Subsystem for Linux (WSL) you can
install a Linux command line environment and follow the Linux
directions within it.

## Mac OS: Homebrew

You are assumed to have [homebrew](https://brew.sh/) installed to get
the necessary tools. If you don't have it, see that link. It's easy
to install!

The `brew` command in your terminal can install the necessary programs:

    brew install p7zip gnupg

## Linux

The programs can be installed by your package manager, some examples:

Debian-likes (including Ubuntu, Mint, and Pop!_OS):

    sudo apt update
    sudo apt install p7zip gnupg

Fedora-likes (including Enterprise Linux, Oracle, RedHat):

    sudo dnf install p7zip gnupg
    # -or-
    sudo yum install p7zip gnupg

Arch Linux (including Manjaro):

    sudo pacman -Syu
    sudo pacman -S p7zip gnupg

# How to Open These Files

## 7Zip: for the .7z file

Linux or Mac OS terminal:

    7z x notes.7z

7z is the command, "x" to extract, notes.7z is the file name. All its
files will be extracted into your current folder. You'll notice all the
".gpg" files have non-".gpg" counterparts, as all of the notes were in
the 7z archive.

## GPG: for the .gpg files

Linux or Mac OS terminal:

    gpg -d <filename>.gpg

Example: `gpg -d Hello-World.md.gpg`

You'll be prompted for the password and the contents of the file will
printed to your terminal. To write the file elsewhere:

    gpg -d <filename.gpg> -o <outputfile>
    gpg -d Hello-World.md.gpg -o Hello-World.md
