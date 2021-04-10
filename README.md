# Search

Script's main functionality is searching for a keyword or a phrase via bing.com or duckduckgo.com search engines.

It allows choosing search engine, number of results, saving format, possibility to search urls recursively.

It also contains setup file to have a possibility to build a package.

### How to install locally

Python3 and Git should be already installed. 

1. Clone the repository by command:
```console
git clone https://github.com/balancy/search_for
```

2. Go inside cloned repository and create virtual environment by command:
```console
python -m venv env
```

3. Activate virtual environment. For linux-based OS:
```console
source env/bin/activate
```
&nbsp;&nbsp;&nbsp;
For Windows:
```console
env\scripts\activate
```

4. Install dependencies:
```
pip install -r requirements.txt
```

## How to use

The usual way to use it is via command:

```console
python main.py -k keyword
```

Complete list of script arguments :

```console
-k keyword
``` 
&nbsp;&nbsp;&nbsp;
where `keyword` is a word, or a phrase to search. Default value is 'python'.

```console
-e engine
``` 
&nbsp;&nbsp;&nbsp;
where `engine` is the search engine to use for search (bing, duckduckgo). Default value is 'bing'. 

```console
-n number
``` 
&nbsp;&nbsp;&nbsp;
where `number` is the number of searched urls of 1st rang. Default value is 3.

```console
-n2 number2
``` 
&nbsp;&nbsp;&nbsp;
where `number2` is the number of recursively searched urls of 2nd rang. Default value is 2.

```console
-f format
``` 
&nbsp;&nbsp;&nbsp;
where `format` is saving format (csv, json, console). Default value is 'json'.  

```console
-r
``` 
&nbsp;&nbsp;&nbsp;
If this argument given (flag enabled), then script will use recursive searching.  

You can always see the help how to use script by command:
```console
python main.py -h
```

Example of script use with arguments:
```console
python main.py -k "python abuser" -r -n 4 -n2 4 -e "bing" -f "console"
```
In this case it will search for a phrase "python abuser" via bing search engine and will print into console
20 found urls (4 urls of 1st rang and 4*4 urls of 2nd rang)