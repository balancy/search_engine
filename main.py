import argparse

from search import search

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Makes search for specified phrase via search engines. "
                    "Allows to choose search engine, saving format."
    )
    parser.add_argument(
        "-e", "--engine", type=str, default="bing",
        help="Which search engine to use (bing, duckduckgo)",
    )
    parser.add_argument(
        "-f", "--format", type=str, default="json",
        help="Format to save results in (csv, json, console)",
    )
    parser.add_argument(
        "-k", "--keyword", type=str, help="Keyword to search",
        default="python",
    )
    parser.add_argument(
        "-n", "--number", type=int, help="Number of 1st rang URLs in result",
        default="3",
    )
    parser.add_argument(
        "-n2", "--number2", type=int, help="Number of 2st rang URLs in result",
        default="3",
    )
    parser.add_argument(
        "-r", "--recursively", action="store_true",
        help="Flag designating need go search 2nd rang results",
    )
    args = parser.parse_args()

    search(
        args.engine, args.format, args.keyword,
        args.number, args.number2, args.recursively,
    )
