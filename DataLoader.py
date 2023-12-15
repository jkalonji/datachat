import os
import openai
import langchain
from langchain.document_loaders import PyPDFLoader

with open("C:\\Users\\jerem\\Documents\\openai_secret_key.txt", "r") as f:
    secret_key = f.read()

openai.api_key=secret_key

loader = PyPDFLoader("Texte_de_loi.pdf")

pages = loader.load()
page = pages[1]
print(page.page_content)
print(page.metadata)
