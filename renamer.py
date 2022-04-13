import io
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
import re
from os import listdir, rename
from os.path import isfile, join

def pdf_to_text(path):
    with open(path, 'rb') as fp:
        rsrcmgr = PDFResourceManager()
        outfp = io.StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, outfp, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
    text = outfp.getvalue()
    return text.replace('\t', ' ')


baseDir = '/Users/alessiopremoli/code/alessiopremoli/alessiopremoli/scripts/cms_scraper/pdf'

pdfs = [f for f in listdir(baseDir) if isfile(join(baseDir, f))]

for pdf in pdfs:
    txt = pdf_to_text(f'pdf/{pdf}')
    name: str = re.findall("Fattura N° \d* del \d{2}/\d{2}/\d{4}", txt)[0].replace("/", '')
    rename(join(baseDir, pdf), join(baseDir, f'{name}.pdf'))