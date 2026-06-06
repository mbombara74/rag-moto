from pypdf import PdfReader

pdf_path = "prova.pdf"

reader = PdfReader(pdf_path)

for i, page in enumerate(reader.pages, start=1):
    text = page.extract_text()
    print(f"\n--- PAGINA {i} ---\n")
    print(text)