**Working on your first Pull Request?** You can learn how from this *free* series [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)

# Welcome and Thank you
Hello and Thank you for dropping by

This project won't get anywhere without your contribution.
Be it reporting an issue, requesting a feature, designing or writing code, documentation, or helping with the graphics design.

This project is mostly written in Python, so some basic knowledge on how to code in Python will be required if you decide to contribute in code.
Anything else, will not require specific technical background.

You can have a look at development progress at [Zube's Sprint Board](https://zube.io/aawadall/pyprojman/w/first-releases/sprintboard?where%5Bsprint_id%5D=18371) of this project.

_We are experimenting with [Code Tree](https://codetree.com/projects/KAo6/issues?show_welcome=true) as well, please vote, which one you prefer_

## Contributions Needed
We need help in the following areas:

### Software Design
This project at its early stages, and we need to design classes, interfaces, methods, etc. to make it fly. You can have a look at the [documents folder][1] to get familiar with the project design, and what it is intended to do.
If you found something that needs change, please log an [issue][2] and label it **design**. Or you can submit a pull request with your proposed changes. I promise to review it ASAP.

### Development
This project is mostly written in Python. You can use [PyCharm][5] to do the required development.
There are two releases (defined as milestones) so far scheduled at [mid September][3] and [Early October][4] 2017, with issues (bugs, or features) assigned to each release. You can read the issue, figure how to implement or fix it, and submit a pull request with the proposed change.

Before you submit the change, __make sure you execute existing unit tests__ for this feature, and __if not present__, please write that unit test. 
After you test your code, you can _commit_ and _push_ your code (including unit tests) into a __new branch__, and submit a __pull request__. This will allow a set of code quality metrics to validate your work. 
We are totally fine with code that might bring code quality down for a while, as long as it adds new features or fixes bugs. 
Code quality can be fixed later with refactoring, when all required features and bug fixes are coded, tested and commited.

We added [Travis](https://travis-ci.org/aawadall/PyProjMan) support for this project, so whnever you add a new unit test file, please include it in the [Travis-CI yaml file](https://github.com/aawadall/PyProjMan/blob/master/.travis.yml) if it was not easy to add, please email me, I'll do it.

Thank you.

### Reporting Issues
You are welcome to play with the application, find bugs, or missing features. Please report any features or bugs in the [issue log][2], and assign it either **bug** or **feature** labels. The more issues we get, the richer the application would be.

### Graphics & UI Design
Currently, this application is entirely text based, but it should not remain this way. If you can propose UI ideas, icons, or even web page design, please contact me via email @ aawadall@ualberta.ca

### Documentation
Clean code requires proper documentation. Pull requests are welcome to different types of documentation:

* Classes and Application Design
* User Guides
* Developer Guides

Thank you 

[1]: https://github.com/aawadall/PyProjMan/tree/master/docs
[2]: https://github.com/aawadall/PyProjMan/issues
[3]: https://github.com/aawadall/PyProjMan/milestone/1
[4]: https://github.com/aawadall/PyProjMan/milestone/2
[5]: https://www.jetbrains.com/pycharm/download/
