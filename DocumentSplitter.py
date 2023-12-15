import os
import openai
import langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter, CharacterTextSplitter

text = """ Les Jeux Olympiques antiques, tels que nous en avons connaissance aujourd’hui, ont une longue histoire. Tout commence
en Grèce, dans le Péloponnèse, il y a 3000 ans environ. Selon les récits historiques existants, les premiers Jeux Olympiques
antiques furent célébrés en 776 av. J.-C. à Olympie. Ils étaient dédiés au dieu grec Zeus et avaient lieu au même endroit tous
les quatre ans. Cette période de quatre années a pris le nom d’« Olympiade ».
Le monde grec ancien était divisé en de nombreuses cités, toutes dirigées par leur propre gou-
vernement. A cette époque, il y avait souvent des conflits entre les cités. Pourtant, même pen-
dant les guerres les plus difficiles, la Trêve olympique venait mettre fin au combat et rassembler
les peuples, tous les quatre ans, à Olympie, patrie de Zeus. Il ne s’agissait pas d’un simple temps
de paix, il s’agissait aussi d’une période de compétitions intenses au cours desquelles les athlètes
s’affrontaient afin de remporter la couronne d’olivier.
Les Jeux olympiques anciens faisaient partie d’un festival religieux d'adoration de Zeus, le père
des dieux et des déesses grecs. Les Grecs arrivaient en masses à Olympie pour le festin, pour
célébrer et admirer les athlètes les plus forts s'affronter dans le but de faire honneur à leur cité
et à leur famille."""

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=10, 
    separators=["\n\n", "\n", "(?<=\. )", " ", ""]
)
split = r_splitter.split_text(text)
print(len(split))
print(split[0])
print('===========')
print(split[1])
print('===========')
print(split[2])
print('===========')
