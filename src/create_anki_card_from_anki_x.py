"""
This prompt help create a file to import into Anki
"""
PROMPT = """
flashcard for 
```
subject: {subject}
{content}

```
Flashcard should start with `[NLP - <subject>]`, 
card types support: multiple choices and cloze, 
response in format to import into Anki
"""

if __name__ == '__main__':
    subject = "abc"
    content = "abc"
    print(PROMPT.format(content=content, subject=subject))
