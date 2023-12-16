import numpy as np
import openai

from langchain.embeddings.openai import OpenAIEmbeddings

with open("C:\\Users\\jerem\\Documents\\openai_secret_key.txt", "r") as f:
    secret_key = f.read()
openai.api_key=secret_key

embedding = OpenAIEmbeddings(api_key=openai.api_key)

sentence1 = "i like dogs"
sentence2 = "i like canines"
sentence3 = "the weather is ugly outside"

embedding1 = embedding.embed_query(sentence1)
embedding2 = embedding.embed_query(sentence2)
embedding3 = embedding.embed_query(sentence3)

print(np.dot(embedding1, embedding2))
np.dot(embedding1, embedding3)
np.dot(embedding2, embedding3) 

