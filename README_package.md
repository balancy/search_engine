# Search

Script's main functionality is searching for a keyword or a phrase via bing.com or duckduckgo.com search engines.

It allows choosing search engine, number of results, saving format, possibility to search urls recursively.

### How to install locally

Python3 and Pip3 should be already installed. 

Installation is made by command:
```bash
pip install search
```

## How to use

The usual way to use search is follow:

```python
from search import search
search(keyword="python")
```

Complete list of script arguments :

`keyword` - is a word, or a phrase to search. Default value is 'python'.

`engine` is the search engine to use for search (bing, duckduckgo). Default value is 'bing'. 

`number` is the number of searched urls of 1st rang. Default value is 3.

`number2` is the number of recursively searched urls of 2nd rang. Default value is 2.

`format` is saving format (csv, json, console). Default value is 'json'.  

`recursively` if is True, then script will use recursive searching.  

Example of using `search` with arguments:
```python
search(engine="bing", number=2, number2=3, recursively=True, keyword="javascript", format="console")
```
In this case it will search for a phrase "javascript" via bing search engine and will print into console
8 found urls (2 urls of 1st rang and 2*3 urls of 2nd rang)