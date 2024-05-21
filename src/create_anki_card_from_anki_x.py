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
card types must include: cloze and basic, 
response in text file to import into Anki
"""

if __name__ == '__main__':
    subject = "Kafka - Consumer Group"
    content = """
## Kafka workflow for consumer group

1. **Producers**: Publish messages on a topic.
2. **Message Storage**: Kafka stores messages in the topic's partitions.
3. **Single Consumer**: Initially, one consumer subscribes to a topic (e.g., Topic-01) with a specific Group ID (e.g., Group-1), and Kafka handles it like pub-sub messaging.
4. **Multiple Consumers**: When a new consumer with the same Group ID subscribes to the same topic:
   - Kafka switches to share mode.
   - Messages are distributed among the group consumers, with each message being consumed by only one group member.
   - Messages are retained after consumption.
5. **Consumer-Partition Assignment**:
   - Message distribution continues until the number of consumers equals the number of partitions.
   - If consumers exceed partitions, new consumers wait until a partition becomes available.
6. **Operation Mode**: This setup operates similarly to queue-based messaging, but messages are not deleted after consumption.


"""
    print(PROMPT.format(content=content, subject=subject))

    with open("temp.txt", "w") as file_io:
        file_io.write(PROMPT.format(content=content, subject=subject))
