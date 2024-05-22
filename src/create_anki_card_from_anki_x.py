"""
This prompt help create a file to import into Anki
"""
PROMPT = """
flashcard for 
```
subject: {subject}
{content}

```
Each card must have prefix `[<subject>]`, 
card types must include: cloze and basic, 
generate cloze import file and basic import file
"""

if __name__ == '__main__':
    subject = "DB - Control File"
    content = """## Control File in Oracle DB

- A control file is a small binary file that records the physical structure of the database
  - includes:
    - The database name
    - Names and locations of associated datafiles and online redo log files
    - The timestamp of the database creation
    - The current log sequence number
    - Checkpoint information

- When an instance of an ORACLE database is started, its control file is used to identify the database and redo log files that must be opened for database operation to proceed
  - Control file also used in database recovery
"""
    print(PROMPT.format(content=content, subject=subject))

    with open("temp.txt", "w") as file_io:
        file_io.write(PROMPT.format(content=content, subject=subject))
