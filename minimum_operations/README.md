# Minimum Operations

## Description
This project solves the minimum operations problem where we need to calculate the fewest number of operations (Copy All and Paste) needed to result in exactly n H characters in a file, starting with a single H character.

## Requirements
- Allowed editors: vi, vim, emacs
- Files interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All files end with a new line
- First line of all files: `#!/usr/bin/python3`
- Code is documented
- Code follows PEP 8 style (version 1.7.x)
- All files are executable

## Algorithm
The solution uses prime factorization. The minimum number of operations to reach n characters is the sum of all prime factors of n (with repetition).

## Files
- `0-minoperations.py`: Contains the minOperations function
- `0-main.py`: Test file

## Author
Project by Carrie Ybay, Software Engineer at Holberton School
