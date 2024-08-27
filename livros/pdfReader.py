import pypdf as p
import os.path

def readBook(bookName, primeiraPagina, ultimaPagina):

    bookPath = os.path.join(os.path.dirname(__file__), bookName)

    book = open(bookPath, "rb")
    pdf_reader = p.PdfReader(book)
    bookSection = []
    
    for paginaNumero in range(primeiraPagina, ultimaPagina):
        page = pdf_reader.get_page(paginaNumero)
        output = page.extract_text()
        groups = output.split('\n')
        print(groups)
        bookSection = bookSection + groups
    return bookSection