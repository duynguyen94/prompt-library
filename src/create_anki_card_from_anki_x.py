"""
This prompt help create a file to import into Anki
"""
PROMPT = """
flashcard for 
```
subject: {subject}
{content}

```
Flashcard should start with `[<subject>]`, 
card types support: cloze and basic, 
response in format to import into Anki
"""

if __name__ == '__main__':
    subject = "Use case diagram"
    content = """
A set of actions (called use cases) that a system should or can perform in collaboration with one or more 
external users of the system (called actors). use case should provide some observable and valuable result to the actors

Characteristics
- Use Case Diagrams describe the high-level functional behavior of the system.
- It answers what system does from the user point of view.
- Use case answers ‘What will the system do?’ and at the same time tells us 'What will the system NOT do?'.

Components
- System boundary - defines the scope and limits of the system, shown as a rectangle that 
spans all use cases of the system.
- Actors - an entity who performs specific actions, the actual business roles of the users in a given system.
An actor interacts with a use case of the system
- Use Case - business functionality, list the discrete business functionality specified in the problem statement.
- Include relationship - represents an invocation of one use case by another use case, like one function being 
called by another function.
- Extend relationship - signifies that the extended use case will work exactly like the base use case, except that some 
new steps will be inserted in the extended use case
"""
    print(PROMPT.format(content=content, subject=subject))

    with open("temp.txt", "w") as file_io:
        file_io.write(PROMPT.format(content=content, subject=subject))
