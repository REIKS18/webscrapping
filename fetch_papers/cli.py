import argparse
from fetch_papers.fetch import get_filtered_papers
import csv

def save_to_csv(data, filename):
    """Save fetched research papers to a CSV file."""
    if not data:
        print("No data to save.")
        return

    headers = ["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        
        for paper in data:
            writer.writerow({
                "PubmedID": paper.get("id", ""),
                "Title": paper.get("title", ""),
                "Publication Date": paper.get("date", ""),
                "Non-academic Author(s)": ", ".join([a["name"] for a in paper.get("non_academic_authors", [])]),
                "Company Affiliation(s)": ", ".join([a["affiliation"] for a in paper.get("non_academic_authors", [])]),
            })

    print(f"Results saved to {filename}")

def main():
    """Command-line interface for fetching papers."""
    parser = argparse.ArgumentParser(description="Fetch research papers with non-academic authors.")
    parser.add_argument("query", type=str, help="Search query for research papers.")
    parser.add_argument("-f", "--file", type=str, help="Output filename (CSV).")

    args = parser.parse_args()

    print(f"Fetching papers for query: {args.query}...")
    papers = get_filtered_papers(args.query)

    if args.file:
        save_to_csv(papers, args.file)
    else:
        print("Results:", papers)

if __name__ == "__main__":
    main()
