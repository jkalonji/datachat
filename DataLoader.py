import os
import openai

openai.api_key='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'

from langchain.document_loaders import PyPDFLoader
loader = PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf")
pages = loader.load()