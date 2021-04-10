import argparse
import csv
import json
import os

from bs4 import BeautifulSoup
import requests
from terminaltables import AsciiTable

FOLDER_TO_SAVE_RESULTS = "data/"


def parse_bing_one_page(keyword, page_number):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) "
                      "Gecko/20100101 Firefox/83.0"
    }
    params = {
        "q": keyword,
        "form": "QBLH",
        "first": page_number * 10,
    }
    url = "https://www.bing.com/search"

    response = requests.get(url, headers=headers, params=params, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "lxml")
    link_elements = soup.select("ol#b_results li.b_algo h2 a")
    return [
        (link_element.get("href"), link_element.text)
        for link_element in link_elements
    ]


def fetch_bing_search_results(keyword, results_number):
    if results_number < 1 or not keyword:
        return None

    search_results = list()

    page_number = 0
    while len(search_results) < results_number:
        search_results += parse_bing_one_page(keyword, page_number)
        page_number += 1

    return search_results[:results_number]


def parse_duckduckgo(keyword, results_number):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) "
                      "Gecko/20100101 Firefox/83.0"
    }
    params = {
        "q": keyword,
        "s": 0,
    }
    url = "https://duckduckgo.com/html/"

    response = requests.get(url, headers=headers, params=params, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "lxml")
    link_elements = soup.select("#links .links_main a")
    urls = [
        (href, link_element.text.strip())
        for link_element in link_elements
        if (href := link_element.get("href", ""))
    ]
    return urls[:results_number]


def fetch_urls_from_page(url):
    response = requests.get(url)
    response.raise_for_status()
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.content, "lxml")

    return [(url, a_elm.text.strip()) for a_elm in soup.select("a")
            if (url := a_elm.get("href", "")).startswith("https://")]


def fetch_urls_from_list_of_pages(urls, results_number):
    all_urls = []
    for url in urls:
        all_urls += fetch_urls_from_page(url[0])[:results_number]

    return all_urls


def save_urls_to_csv(urls, urls_second_rang=None):
    if urls_second_rang:
        urls += urls_second_rang

    with open(
            f"{FOLDER_TO_SAVE_RESULTS}urls.csv",
            mode="w",
            encoding="utf-8",
            newline="",
    ) as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["URL link", "URL title"])
        writer.writerows(urls)


def save_urls_to_json(urls, urls_second_rang=None):
    urls = {
        "urls_1st_rang": urls
    }
    if urls_second_rang:
        urls.update({
            "urls_2nd_rang": urls_second_rang,
        })

    with open(
            f"{FOLDER_TO_SAVE_RESULTS}urls.json",
            mode="w",
            encoding="utf-8"
    ) as file:
        json.dump(urls, file, ensure_ascii=False)


def print_to_console(urls, urls_second_rang=None):
    table_data = [["URL link", "URL title"]]

    if urls_second_rang:
        urls += urls_second_rang

    for url in urls:
        table_data.append((url[0][:100], url[1][:100]))

    table = AsciiTable(table_data)
    print(table.table)


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
        "-k", "--keyword", type=str, help="Keyword to search", default="python",
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
        help="Flag go search 2nd rang results",
    )
    args = parser.parse_args()

    if args.engine == "duckduckgo" or args.engine == "duck":
        urls = parse_duckduckgo(args.keyword, args.number)
    else:
        urls = fetch_bing_search_results(args.keyword, args.number)

    if args.recursively:
        urls_second_rang = fetch_urls_from_list_of_pages(urls, args.number2)
    else:
        urls_second_rang = None

    os.makedirs(FOLDER_TO_SAVE_RESULTS, exist_ok=True)

    if args.format == "console":
        print_to_console(urls, urls_second_rang=urls_second_rang)
    elif args.format == "csv":
        save_urls_to_csv(urls, urls_second_rang=urls_second_rang)
    else:
        save_urls_to_json(urls, urls_second_rang)
