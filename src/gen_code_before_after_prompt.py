PROMPT = """
as a senior engineer, do step-by-step
1. extract data from {url}
2. generate an example of before and after using this design pattern.

response "no access" if you cannot read the data, do not attempt to generate anything
"""

if __name__ == '__main__':
    url = "https://refactoring.guru/design-patterns/prototype/python/example#example-0"
    with open("temp.txt", "w") as file_io:
        file_io.write(PROMPT.format(url=url))
