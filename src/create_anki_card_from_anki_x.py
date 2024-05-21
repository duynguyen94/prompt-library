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
response in text file to import into Anki
"""

if __name__ == '__main__':
    subject = "Kafka - Delivery Semantic"
    content = """
## Delivery semantics

### Producer option to check message write as successful
- **Async**
  - fire-and-forget approach
  - Producer sends a message to Kafka and does not wait for acknowledgment from the server, considered successful the moment the request is sent out.
  - the best performance on writing data without guarantee can be made that the server has received the record

- **Committed to Leader**
  - Waits for an acknowledgment from the leader.
  - Slower than the 'Async' option, as the data has to be written on disk on the leader
  - The leader will respond without waiting for acknowledgments from the followers.
    - the record will be lost if the leader crashes immediately after acknowledging the producer but before the followers have replicated it.

- **Committed to Leader and Quorum**
  - leader will wait for the full set of in-sync replicas to acknowledge the record
  - the slowest write but guarantees that the record will not be lost as long as at least one in-sync replica remains alive

### Consumer delivery options to ensure consistency
- **At-most-once**
  - a message is delivered a maximum of one time only, might be lost
  - Consumer receiving a message, commit (or increment) the offset to the broker.
  - If the consumer crashes before fully consuming the message, that message will be lost
    - when the consumer restarts, it will receive the next message from the last committed offset.

- **At-least-once**
  - a message might be delivered more than once, but no message should be lost
  - Use case: consumer receives a message from Kafka, it does not immediately commit the offset, it waits till it completes the processing
  - if the consumer crashes after processing the message but before committing the offset, it has to reread the message upon restart.
    - the consumer never committed the offset to the broker, the broker will redeliver the same message
  - duplicate message delivery could happen in such a scenario.

- **Exactly-once**
  - each message is delivered once and only once
  - the consumer puts the message processing and the offset increment in one transaction, ensure that the offset increment will happen only if the whole transaction is complete
    - If the consumer crashes while processing, the transaction will be rolled back, the offset will not be incremented
  - This option leads to no data duplication and no data loss but can lead to decreased throughput.

"""
    print(PROMPT.format(content=content, subject=subject))

    with open("temp.txt", "w") as file_io:
        file_io.write(PROMPT.format(content=content, subject=subject))
