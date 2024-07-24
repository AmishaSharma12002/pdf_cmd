# PDF Commander

**PDF Commander** is a Python script designed to divide PDF files into smaller sections based on user-defined chapter ranges. It automates the process of splitting a PDF into multiple files, each corresponding to a chapter or section.

## Features

- **Automatic Processing**: Handles all PDF files in the current directory.
- **User-Defined Chapter Ranges**: Allows specifying start and end pages for each chapter.
- **Cross-Platform Compatibility**: Works on both Windows and Linux.

## Installation

To run the PDF Commander, you need Python and the PyPDF2 library.

### Prerequisites

- Python 3.x
- PyPDF2 library

### Installing PyPDF2

Install the required library using pip:

```sh
pip install PyPDF2
```
## Usage

1.  **Save the Script**: Save the provided `main.py` script to your project directory.
    
2.  **Prepare Your PDFs**: Ensure that the PDF files you want to split are located in the same directory as the script.
    
3.  **Run the Script**: Execute the script using Python. Open your terminal or command prompt and run:
```sh
python main.py
```
4. **Follow Prompts**:
    
    -   The script will automatically detect all PDF files in the current directory.
    -   For each PDF file, you will be prompted to enter the number of chapters.
    -   Specify the starting and ending pages for each chapter.
 5. **Check Output**: The split PDFs will be saved in a directory named `Split_Chapters`, with subfolders named after the original PDF files. Each chapter will be saved as a separate PDF file.
 
 ## Contributing

Contributions are welcome! If you have suggestions or improvements, please:

1.  Fork the repository.
2.  Create a new branch for your changes.
3.  Make your changes and test them.
4.  Submit a pull request with a clear description of your modifications.
## Contact

For any questions or feedback, please contact [Ammy](https://github.com/AmishaSharma12002).
"# pdf_cmd" 
