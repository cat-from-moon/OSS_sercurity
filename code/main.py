import argparse
from urllib.parse import quote

import requests


def main():
    parser = argparse.ArgumentParser(description="Show GitHub repository information.")
    parser.add_argument("owner", nargs="?", default="Crabbercat", help="GitHub repository owner")
    parser.add_argument(
        "repository", nargs="?", default="OSS_sercurity", help="GitHub repository name"
    )
    args = parser.parse_args()

    owner = quote(args.owner, safe="")
    repository = quote(args.repository, safe="")
    response = requests.get(
        f"https://api.github.com/repos/{owner}/{repository}", timeout=10
    )
    response.raise_for_status()
    details = response.json()

    print(f"Name: {details['full_name']}")
    print(f"Description: {details.get('description') or 'No description'}")
    print(f"Stars: {details['stargazers_count']}")


if __name__ == "__main__":
    main()