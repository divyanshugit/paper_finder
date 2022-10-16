import re
import requests
from bs4 import BeautifulSoup as bs
import trafilatura as trf
import pandas as pd
from tqdm import tqdm

def extract_paper(key,link):
    download = trf.fetch_url(link)
    string = trf.extract(download, include_comments=False)
    data = string.split('\n')
    fed_paper = []
    for i in data:
        if 'Federated' in i:
            fed_paper.append(i)
    if "CVPR" in key:
        fed_paper = fed_paper[::2]

    return fed_paper

iclr2022 = "https://iclr.cc/Conferences/2022/Schedule"
iclr2021 = "https://iclr.cc/Conferences/2021/Schedule"
nips2022 = "https://nips.cc/Conferences/2022/Schedule"
nips2021 = "https://nips.cc/Conferences/2021/Schedule"
icml2022 = "https://icml.cc/Conferences/2022/Schedule"
icml2021 = "https://icml.cc/Conferences/2022/Schedule"
cvpr2022 = "https://openaccess.thecvf.com/CVPR2022?day=all"
cvpr2021 = "https://openaccess.thecvf.com/CVPR2021?day=all"

conferences = {"ICLR'21":iclr2021,"ICLR'22":iclr2022, "NIPS'21":nips2021, 
                "NIPS'22":nips2022, "CVPR'21":cvpr2021, "CVPR'22":cvpr2022}

papers = {}
conf = []
paper_name = []

for key in tqdm(conferences):
    ex_papers = extract_paper(key,conferences[key])
    paper_name.extend(ex_papers)
    conf.extend([key] * len(ex_papers))

print(len(paper_name))
print(len(conf))  
papers = {"Name of the Paper": paper_name, "Conference": conf}

papers_df = pd.DataFrame(papers)
filename = "Federated-Learning.csv"
papers_df.to_csv(filename,index=False)



    