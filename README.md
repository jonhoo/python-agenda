Simple Python module for pretty task logging.

Exposes the following methods:
 - `section` starts a new section of application processing
 - `task` starts a new high-level task within the section
 - `subtask` starts a new subtask within the task
 - `subfailure` indicates the failure of a subtask of the current task
 - `failure` indicates the failure of a high-level task
 - `subprompt` prints a subtask input prompt
 - `prompt` prints a high-level input prompt

You can see a demo by running `demo.py`:
![Pretty-looking nested console output](/demo.png?raw=true)
