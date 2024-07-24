import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, chapters):
    # Create a folder to save the split files
    base_folder = "Split_Chapters"
    file_name = os.path.splitext(os.path.basename(input_pdf_path))[0]
    output_folder = os.path.join(base_folder, file_name)
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the input PDF file
    pdf_reader = PdfReader(input_pdf_path)
    
    for i, (start_page, end_page) in enumerate(chapters):
        pdf_writer = PdfWriter()
        
        # Copy the pages from the input PDF to the new file
        for page_num in range(start_page-1, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        
        # Save the new file with the pages copied
        output_pdf_path = os.path.join(output_folder, f"Chapter_{i+1}.pdf")
        with open(output_pdf_path, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        
        print(f"Chapter {i+1} saved to {output_pdf_path}")

def main():
    # Get a list of all PDF files in the current folder
    pdf_files = [f for f in os.listdir(os.getcwd()) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print("No PDF files found in the current directory.")
        return
    
    # Process each PDF file one by one
    for input_pdf_name in pdf_files:
        input_pdf_path = os.path.join(os.getcwd(), input_pdf_name)
        print(f"Processing {input_pdf_name}...")
        
        # Ask how many chapters there are
        num_chapters = int(input("Enter the number of chapters: "))
        chapters = []
        
        # Get the starting page for each chapter
        for i in range(num_chapters):
            start_page = int(input(f"Enter the starting page number for Chapter {i+1}: "))
            if i > 0:
                chapters[-1] = (chapters[-1][0], start_page - 1)
            chapters.append((start_page, None))
        
        # Get the ending page for the last chapter
        end_page = int(input(f"Enter the ending page number for the last chapter: "))
        chapters[-1] = (chapters[-1][0], end_page)
        
        # Split the PDF based on the chapter information
        split_pdf(input_pdf_path, chapters)

if __name__ == "__main__":
    main()
