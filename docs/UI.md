# UI Class
Handles text based user interface operations; all user interactions should be funneled to the system through an instance of this class. 

Future inheritance might take place, where this class, and a GUI class would share common ancestry 

## Dictionary 
My initial design relies on defining a set of keywords, that are hardcoded in the class, and are to be extracted later on as API calls, such that internationalization would augment this class. 

All keywords in this dictionary should be case insensitive to simplify interaction with users

### Keywords

#### Create
Creates a task\
Usage : 

`CREATE TASK` 

or 

`CREATE TASK "Task Name"`

Creates a task, and assigns task name to it if a task name is passed, 
task names should be surrounded by double quotes 

Running this command, creates a task, and returns its UUID

```
TASK CREATED: 
bd95861e-5a0d-4499-8ac1-d76a9c848bc0 : Task Name
0.0 % Completed 

Planned:    
    Start   : None  
    End     : None  
    Duration: None
Actual:     
    Start   : None
    End     : None
    Duration: None
        
Prerequisite Tasks
Dependant Tasks

```
#### Exit
Exits Application \
Usage :

`Exit`
#### Find
Finds tasks by name\
Usage : 

`FIND TASK "Part of Task Name"`

Searches for all tasks with a name containing the string surrounded by double quotes  

Result is a list of UUID and Names
```
Task ID                              : Task Name
bd95861e-5a0d-4499-8ac1-d76a9c848bc0 : Main Task
eca34300-3b84-40e3-80e2-c8aaaa5e43ff : Second Task    

```

#### Help
Displays Help \
Usage :

`Help`

Lists down operations and a quick description of its function 
```
    keyword         Function
    create          Creates new task
    exit            Exits Project Manager Application
    find            Searches for tasks by its name
    report          Displays project statistics
    link            Links two tasks as prerequisite and dependant
    list            Lists all tasks
    show            Shows details of an individual task
```
#### Report 
Displays project statistics \
Usage :
`Report`

#### Link 
Links two tasks as prerequisite and dependant\
Usage :\
`LINK TASK <UUID> AS <PREREQUISITE FOR|DEPENDANT ON> <UUID>`

e.g.\
`Link TASK bd95861e-5a0d-4499-8ac1-d76a9c848bc0 AS PREREQUISITE FOR eca34300-3b84-40e3-80e2-c8aaaa5e43ff`

or

`Link TASK bd95861e-5a0d-4499-8ac1-d76a9c848bc0 AS DEPENDANT ON eca34300-3b84-40e3-80e2-c8aaaa5e43ff`

#### List
Lists all Tasks \
Usage :\
`List`
#### Show 
Shows details of a particular task\
Usage : \
`SHOW TASK <UUID>`
