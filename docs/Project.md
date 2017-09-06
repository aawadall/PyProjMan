## Project Description
A simple (for the time-being) project management tool, designed for developers.

_I might need to migrate this document into GitHub issues_

_This document is more of a scrap paper than real project documentation_
## Distinguishing Features
### Rapid project builder wizard
a way to design a project plan, by asking the user about major components of the current step, and continue defining more details until a step is defined by the simplest tasks

### Online Dashboard
Allowing project manager, 
and other users (stakeholders and assignees) to see current progress, 
outstanding tasks, etc. 
and to be able to annotate some tasks or self assign as well. 
similar to GitHub's issues    

### Commandline Interface
Main user can (script) tasks, and possibly program task creation

### Distributed Setup
Multiple agents communicate and update same plan using a local repo, remote repo style

## Features Backlog
1. GANTT Chart support
1. Network diagram support
1. calendar integration
1. List View of Tasks
1. Be able to Edit individual tasks 
    1. in the list
    1. in task details
    1. using commandline 
1. have commandline support 
1. have user interface 
1. have reminders set
    1. integration with email
    1. integration with twitter 
1. be able to generate reports 
1. have one or more of the reports defined as a static web page  
1. Allow a distributed infrastructure, 
where multiple instances of the application on multiple machines, 
would communicate and update each other

    
## Project Tasks
*[ ] Project Management Tool using Python
*[ ] Design Tasks as a recursive tree 
*[ ] A task should have the following attributes
    *[ ] Task ID
    *[ ] Task Description
    *[ ] Completion Status 
    *[ ] Planned Start Date/Time
    *[ ] Planned End Date/Time
    *[ ] Actual Start Time
    *[ ] Actual End Time
*[ ] Design UI for this project, maybe web

## Ideas to research
*[ ] Can we integrate this app with twitter?
*[ ] Shall we store data in XML or in database?
*[ ] Should the UI of this project be web or thick client?
*[ ] Can we implement drag and drop to define tasks?
*[ ] Can we integrate with github issues, projects and milestones?
*[ ] Can we integrate with Google services?
*[ ] Keep track of task changes, and record timestamp and user who changed it 
*[ ] Can we write a timekeeper object?
