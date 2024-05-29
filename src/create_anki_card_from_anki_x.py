"""
This prompt help create a file to import into Anki
"""
PROMPT = """
flashcard for 
```
subject: {subject}
{content}

```
Card must start with `[<subject>]`, 
card types: cloze and basic, 
generate cloze import file and basic import file
"""

if __name__ == '__main__':
    subject = "Full Backup with Open Database"
    content = """Full Backup with Open Database
- Reasons why full backup cannot be performed when the database is open
    - Data Consistency
        - A full backup requires a consistent snapshot of the database. When a database is open and in use, ongoing transactions can change the state of the database. This makes it challenging to capture a consistent state across all data files.
        - For instance, in MariaDB, full backups taken without consistency measures can lead to inconsistencies, causing InnoDB to crash upon restoration to protect against data corruption
    - Transaction Logs
        - In databases like PostgreSQL, a full backup must include transaction logs to ensure all changes are recorded. Without these logs, which are actively written during an open database state, the backup might miss critical changes​
- Alternative backup strategies for open databases
    - Online (Hot) Backups
        - Database Tools: Use built-in database tools designed for online backups. Tools like Mariabackup for MariaDB and pg_basebackup for PostgreSQL allow for backups while the database is still running.
        - Procedure: These tools often work by taking a snapshot of the database and copying transaction logs to ensure all transactions are captured up to a certain point in time​ 
    - Point-in-Time Recovery (PITR):
        - PostgreSQL: Use continuous archiving and point-in-time recovery (PITR). This involves setting up WAL (Write-Ahead Logging) archiving and making periodic base backups. This allows for the database to be restored to any point in time by replaying the archived logs​ 
        - Oracle: Similar to PostgreSQL, Oracle databases use the ARCHIVELOG mode, where redo logs are archived. This allows for restoring the database to a specific point in time using the archived redo logs​
    - Incremental Backups
        - MariaDB: Use incremental backups to capture only the changes since the last full or incremental backup. This reduces the backup window and ensures minimal performance impact on the running database
        - SQL Server: Perform differential backups that capture only the data changes since the last full backup, allowing for more frequent backups with less impact on performance​ 
    - Snapshot Technology
        - Storage-Level Snapshots: Utilize storage-level snapshots if the underlying storage supports this feature. This involves taking a snapshot of the storage volume, which can be done quickly and with minimal impact on database performance. These snapshots can then be used to restore the database to a specific point in time."""
    print(PROMPT.format(content=content, subject=subject))

    with open("temp.txt", "w") as file_io:
        file_io.write(PROMPT.format(content=content, subject=subject))
