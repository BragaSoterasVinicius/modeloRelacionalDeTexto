import pypdf as p
import os.path

def readBook(bookName, primeiraPagina, ultimaPagina):

    bookPath = os.path.join(os.path.dirname(__file__), bookName)

    book = open(bookPath, "rb")
    pdf_reader = p.PdfReader(book)
    bookSize = pdf_reader.get_num_pages()

    for paginaNumero in range(primeiraPagina, ultimaPagina):
        page = pdf_reader.get_page(paginaNumero)
    output = page.extract_text()

    return output