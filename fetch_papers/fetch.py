import requests
import xml.etree.ElementTree as ET
import re
from typing import List, Dict, Optional

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_paper_ids(query: str) -> List[str]:
    """Fetch PubMed IDs based on a query."""
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": 10}
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])

def fetch_paper_details(paper_id: str) -> Optional[Dict]:
    """Fetch details of a paper given its PubMed ID."""
    params = {"db": "pubmed", "id": paper_id, "retmode": "xml"}
    response = requests.get(DETAILS_URL, params=params)
    response.raise_for_status()
    return parse_paper_details(response.text)

def parse_paper_details(xml_data: str) -> Optional[Dict]:
    """Parse XML data to extract paper details."""
    root = ET.fromstring(xml_data)
    title = root.find(".//ArticleTitle")
    date = root.find(".//PubDate")
    authors = []
    for author in root.findall(".//Author"):
        name = " ".join([
            author.find("ForeName").text if author.find("ForeName") is not None else "",
            author.find("LastName").text if author.find("LastName") is not None else ""
        ]).strip()
        affiliation = author.find(".//Affiliation")
        authors.append({"name": name, "affiliation": affiliation.text if affiliation is not None else ""})
    return {
        "title": title.text if title is not None else "Unknown",
        "date": date.text if date is not None else "Unknown",
        "authors": authors
    }

def filter_non_academic(authors: List[Dict]) -> List[Dict]:
    """Filter authors who are affiliated with non-academic institutions."""
    pharma_keywords = ["pharma", "biotech", "laboratories", "inc", "corp", "ltd"]
    return [author for author in authors if any(keyword in author["affiliation"].lower() for keyword in pharma_keywords)]

def get_filtered_papers(query: str) -> List[Dict]:
    """Fetch and filter papers based on query."""
    paper_ids = fetch_paper_ids(query)
    results = []
    for paper_id in paper_ids:
        paper_info = fetch_paper_details(paper_id)
        if paper_info:
            non_academic_authors = filter_non_academic(paper_info.get("authors", []))
            if non_academic_authors:
                paper_info["non_academic_authors"] = non_academic_authors
                results.append(paper_info)
    return results
