# Image Filter Program

## Overview
This is a C program that applies various filters to 24-bit uncompressed BMP 4.0 image files. The program reads an input BMP file, applies a specified filter, and writes the result to an output BMP file.

## Features
The program supports four image filters:
- `-b`: Blur filter
- `-g`: Grayscale filter
- `-r`: Reflection filter (horizontal reflection)
- `-s`: Sepia filter

## Prerequisites
- C compiler (e.g., gcc)
- Standard C libraries
- The `helpers.h` header file containing filter function declarations

## Compilation
To compile the program:

gcc -o filter filter.c helpers.c -std=c11

## Usage
./filter [flag] infile outfile

- `[flag]`: One of `-b`, `-g`, `-r`, or `-s`
- `infile`: Input BMP filename
- `outfile`: Output BMP filename

Examples:

./filter -g input.bmp output.bmp    # Convert to grayscale
./filter -b input.bmp output.bmp    # Apply blur effect


## Requirements
- Input must be a 24-bit uncompressed BMP 4.0 file
- Only one filter can be applied at a time
- Exact command-line arguments must be provided (flag, input file, output file)

## Error Codes
The program returns different exit codes for various errors:
- 1: Invalid filter flag
- 2: More than one filter specified
- 3: Incorrect number of arguments
- 4: Could not open input file
- 5: Could not create output file
- 6: Unsupported file format
- 7: Memory allocation failure

## Implementation Details
1. Uses `getopt` for command-line argument parsing
2. Validates BMP file headers
3. Processes image data as `RGBTRIPLE` pixels
4. Handles BMP padding requirements
5. Dynamically allocates memory for image processing
6. Depends on filter functions defined in `helpers.h`

## File Structure
- `filter.c`: Main program
- `helpers.h`: Header file with filter function declarations
- (Presumed) `helpers.c`: Filter function implementations

## Limitations
- Only supports 24-bit BMP 4.0 files
- No support for chaining multiple filters
- Requires exact command-line format

## Dependencies
- Standard C libraries: `<getopt.h>`, `<stdio.h>`, `<stdlib.h>`
- Custom `helpers.h` header file