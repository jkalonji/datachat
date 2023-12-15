import os
import openai
import langchain

openai.api_key='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'

from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("Texte_de_loi.pdf")

pages = loader.load()