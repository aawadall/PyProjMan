# Task
Core of the project manager application. An object, capable of referencing multiple dependents (children), and multiple prerequisites (parents) to form a network of those objects.

## Attributes 
The **_Task_** class, has the following attributes \
(_defined based on my personal experience with project management_):
### Task ID
*[x] Defined \
a UUID, automatically generated at object instantiation time. 

### Task Name
*[x] Defined \
User specified task label.

### Task Status (% Completed)
*[x] Defined \
A real number between 0 and1, specified percentage completed of a task; _status_ &in; & _status_ &#8477; &in; [0,1]

### Planned Time frame
*[x] Defined \
Made of the three time keeping components, with one to be derived from the other two
#### Planned Start Date/Time
*[x] Defined \
When this task is planned to start working on.

#### Planned End Date/Time
*[x] Defined \
When this task is expected to finish

#### Planned Duration (Estimated Effort)
*[x] Defined \
How long this task is expected to take

### Actual Time frame
*[x] Defined \
Similar to Planned time frame, but this is the actual time frame. It is to be recorded by the project manager, the resource, or any other project contributor authorized to alter project plan.

#### Actual Start Date/Time
*[x] Defined \
When this task started.

#### Actual End Date/Time
*[x] Defined \
When this task finished

#### Actual Duration (Estimated Effort)
*[x] Defined \
How long did this task take to finish.

### Contributors
*[ ] Defined \
Who is assigned to this task. It can be a single user, no one, or a set of users.

### Notes
*[ ] Defined \
Arbitrary notes associated to the task. It should be a _micro-blog_ style of notes with timestamp and user name, rather than a fixed block of rich text.
 
### Configuration Flags
*[ ] Defined \
A set of flags used by the application used for internal housekeeping tasks, and possibly reporting purposes. \
Example, tasks that are to be planned by its end date, while others planned by its start date. 
or tasks to be defined as milestones, while others defined as issues (bugs) to be fixed.