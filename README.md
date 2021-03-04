# Bulletin board TCP client


This bulletin board client accepts following commands: (case-sensitive)

+ POST. Send one or more lines of messages to the bulletin server. A single line containing a dot ('.') and a carriage return must be used to terminate messages.

+ READ. This command retrieves all posted messages from the bulletin server. The client will display each message in a new line.

+ QUIT. Quit the bulletin command.

*Note:* Currently, except for the above commands, all other commands are invalid.
