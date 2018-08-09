---
title: Python
class_name: EGR598
bibliography: ../../bibliography.bib
csl: ../../ieee.csl
//overlay_text: DRAFT
//subtitle:
---
One thing I really like about python is that it is based on good programming practice . if you've ever looked at python help tutorials online, you'll see the term "pythonic". The Zen of python by Tim Peters is copied below

> The Zen of Python, by Tim Peters
>
>Beautiful is better than ugly.  
Explicit is better than implicit.  
Simple is better than complex.  
Complex is better than complicated.  
Flat is better than nested.  
Sparse is better than dense.  
Readability counts.  
Special cases aren't special enough to break the rules.  
Although practicality beats purity.  
Errors should never pass silently.  
Unless explicitly silenced.  
In the face of ambiguity, refuse the temptation to guess.  
There should be one-- and preferably only one --obvious way to do it.  
Although that way may not be obvious at first unless you're Dutch.  
Now is better than never.  
Although never is often better than *right* now.  
If the implementation is hard to explain, it's a bad idea.  
If the implementation is easy to explain, it may be a good idea.  
Namespaces are one honking great idea -- let's do more of those!

<http://docs.python-guide.org/en/latest/writing/style/>

Perhaps many of the things I like about python are the things that make it different from other languages. one of the things I don't like about see or C plus plus is how every single line needs to have a semicolon at the end. python make the assumption that because there's a carriage return, that's the end of the statement. Singly, code blocks in Python are indicated by fewer or more tabs. If you are putting code inside a code block that goes in an if statement, see your cplusplus requires beginning and ending characters to indicate where the code black begins and ends. Tabs and spaces are simply window dressing to make the code more readable. Python, on the other hand, uses those window dressing characters as the logic. To me this saves time. Once you get used to it.

One of the more difficult things to learn when you're getting used to python is the fact that functions and classes can take variable numbers and types of inputs when you declare them the first time. The same function can take in a float or an int or another class just as easily; only when you start to use the data inside that variable do errors pop up. This implicit model for how variables are used within code has several results. First, it means that you don't have to think through your code before you write it. This can be good or bad. By not having to declare the type of the variable that you're using, it means that the same function or class can be useful in many different ways as your project involves, but it also means that the same function can break when using it with different variable types. often, this is much later than when you wrote the code first time, meaning that you're dead bugging something that you thought already worked much later. However, on the flip side, this means that you're able to write code that remains flexible for a very long time, even if you wrote it during the prototyping stage when you didn't exactly know what the structure or format of your final data structures would be. This permits rapid creation of code that remains fairly robust through its life. As I use Python for research purposes primarily and less in a production environment with clients or users who depend on reliability, I appreciate this flexibility and the relative long-life of the code that I write.

To me, one of the more controversial design decisions in Python works is that permits access to from wherever you are to wherever you want to look. There are very few restrictions on how to get data from other data types, classes, etc. This makes python very flexible, but for novices who don't know best practice, it permits the same type of mistakes that you see in other scripted languages. Structuring classes and the flow and exchange of data between classes and other object-oriented types has been one of the steepest learning Curves in my learning a python. However, in the words of Peter Parker's uncle, with great power comes great responsibility. python give you the power to make poor design decisions, and through the mistakes that you make while you're learning it, you learn best practice on the Fly. There are many resources out there on the web that will Guide you on _idiomatic python_, or best programming practices

another thing that python does really well is permit access to structured data at a higher level than other low level programming languages. Included in its base data types are things such as lists, two bulls, dictionaries. within it language and syntax are ways of entering data into those data types and extracting data from those data types much more efficiently than other languages that do not assume higher order data.

Just as functions put no restriction on what type of data is used within a variable, neither do higher order data types. unlike arrays in C or C plus plus, the data inside a list can be anything. You can have lists of integers, floats, classes, or a mix of all of those things. The same goes for tuples and dictionaries.

One of the things that I try to practice when I'm writing python code is that my code should be legible without comments. Of course, this is a goal and never truly realized in practice, but I believe that many of the characteristics of python itself permit much more legible code. In terms of variable naming, there are a couple best practices which help identify what the object is that you're working with.

- Functions methods and attributes should use lower case naming conventions with an underscore between words.

- Classes should use camel case

- Constants can be name blank variables or you can use all caps

Some other best practices include:

- Four spaces per indentation. Tab characters should not be used in Python code.  instead use four space characters to represent a tab. I don't know why, but this is most likely due to different conventions between operating systems and how tabs are used between them.  Good python editors will add spaces instead of tab characters when you hit the tab key.

- Tabs and spaces shouldn't be mixed

- there should be blank lines separating important chunks of code

- One of the other conventions that I don't like to follow is that code should be no more than 80 characters long. I don't follow this, typically because modern monitors are much larger and fit more text, making the size of the viewable windows that you see today much wider than when this rule was created

- backsplashes, which permit you to run over a single line, can be used but shouldn't be used

Python blends many of the best parts of a scripted language with the speed of compiled languages. Python can load dlls and modules written and compiled other languages, Meaning that you can separate low-level high-speed code from the organizational code surrounding it. I thought was very good for organizing your thoughts and for exchanging data between high-speed lower-level functions in classes.

Let's take a look at why I like Python better than that loud Matlab. while both are supported languages, and both permit rapid creation of code, pythonic cells for a couple specific reasons.

## Reason #1: Free

First, it's free. This accessibility means that anyone can download and run it on almost any computer. the downside is that it is hard to install in operating systems like Windows.

The free nature of python does have some negative implications, many of which are getting better. while help is almost never free, python makes it easy to document your code, and the most highly-regarded code is also the most well-documented. In terms of obtaining distributions of code, modern Python has also built in a set of tools for installing and updating python packages from the pypi repository. this Functionality has grown with the transition from python 2 to 3, and some of the conventions imposed by the PIP tools are making things easier than they used to be.

While the python executable installer is not typically the problem, the problem is in many of the packages that need to be used on Windows machines. solve this problem, I have typically turned two distributions a python. Distributions are compiled sets of packages that are produced typically by a company, who then support their distributions for commercial applications with support and Consulting. There are three distributions that I've used, the Anaconda distribution, a set of compiled packages produced by Christopher Gohlke, and the enthought python distribution.

### Anaconda

I've used Anaconda for only a short time, but at this point it seems to be the easiest way to get python -- and all the scientific package you need for it -- installed on your computer regardless of operating system. Anaconda is a distribution of python with a installer and updater called "conda" which helps keep everything a bit better maintained than the alternatives(pip / pypi / gohlke / homebrew were my previous solutions, for windows and mac). It doesn't have everything, but it plays nice with installers like pip, for example, and gives you a lot of control over how you install your packages for different problems. It also allows you to install multiple versions of python in different environments, creating a nice sandbox to play in to keep projects small and self-contained.

I prefer to install miniconda and then create a custom environment for different projects. Install instructions can be found in the tutorials.

Another nice thing about Anaconda is that it ships with the IPython interpreter, which is the basis for the Jupyter notebook. Jupyter is a much more visual, interactive version of python, which permits web-based development(with all or many of the bells and whistles you have come to expect in other languages, like tab-completion), and rapid visualization of your results. One of the best things is that it permits the use of markdown cells within your code to produce highly-readable examples for, for example, books like this. We will be using Jupyter a lot.

## Reason #2: Licensing

Usability comes in many forms, and because I'm a researcher And because I'm a researcher, I am off and doing my work on the road or away from my desk. Matlab licensing strategies include some which mean that you have to be tied to the network you're using it on, making it infeasible to use on particular days of travel. Python has no such restrictions

## Guis

Similarly there are many GUIs out there, but far and away my longstanding favorite is spyder. Spyder is included in the Anaconda distribution by default. This is one of the reasons why I have selected Anaconda over enthought's more recent distributions. spider Features and environment which would be familiar to Legacy Matlab users. A code window permits the entry of scripts or file based modules, while a command line window permits those scripts or files to be run or executed, and for the user to interact with the data that gets produced at the end. this back and forth between code writing and interacting is critical in the prototyping process that I use when constructing new Python code.

## Reason #3: Object-oriented support

One thing in the great Matlab vs. python debate is the ease with which you can create object-oriented code. Historically Matlab has encouraged scripting, forcing you to create a new file every time you want to write a new reusable function. Classes enforce a file naming convention when you want to use them. While classes are easier to create and use now in Matlab than they have been in the past, python puts no impediments in your way when trying to structure your code the way you want. Again, with the downside that novice python programmers often the wrong Structural decisions initially.

## More Reasons:
Another admittedly small thing that I like about python is that it uses 0-based indexing versus 1-based indexing. For me, this has meant fewer times when I have to add or subtract 1 from an indexing variable, or have indexing errors.  Python's indexing works just as well in the forward direction as it doesn't reverse, meaning that I can start from any index and go to the end of a list or go to any point at the end of a list.

# Packages

Data access

The most important packages that I use when creating python code are those packages which make a python more Matlab-like.

Numpy

<https://www.scipy.org/getting-started.html>

this package permits one to store and access data in arrays multidimensional arrays as one would do natively in Matlab. While python permits nested lists, the Paradigm of being able to slice multidimensional arrays of data, to index through it, too reshape and analyze it across dimensions in multiple ways is provided by this package

Scipy

<https://docs.scipy.org/doc/scipy/reference/index.html>

Scipy complements numpy in that it permits low-level arrays defined in numpy to be analyzed across a wide array of linear algebra and scientific functions. The most notable packages with inside Pi include modules for integration, interpolation, linear algebra, optimization, nonlinear optimization, sparse matrices, spatial operations such as triangulation convex hole Etc and statistics

Module list: <https://docs.scipy.org/doc/scipy/reference/py-modindex.html>

Matplotlib

Matplotlib is a package which permits the visualization of data, especially Ray base data used in numpy. matplotlib also provides an interface which is similar to Matlab, making it easy to make the transition between Matlab plotting and plotting in Python. Not live also permits object-oriented-style access to its structures in classes, making it possible to embed object-oriented style code and enhance it with plotting functionality. specialty modules within matplotlib start with pi plot, the scripted interface for creating python plots. Other modules which are worth noting are the path modules, which allow you to access complex geometric classes such as lines and polygons, and to program these shapes at a very low level in order to get the exact type of drawing you want. Another module within matplotlib which is worth knowing about is the color map capability, which allows you to specify and generate colors along a spectrum. A variety of Spectra are predefined, permitting you to ship the color of your plots for different uses very easily. Other common modules are the figure and axis modules, which provide access to the axis and figure classes. One of their module to know about is the image module, which allows you to display image data or bitmapdata and to operate on pictures and images within figures and plots.

[_https://matplotlib.org/tutorials/index.html_](https://matplotlib.org/tutorials/index.html)

Other things that you can do in that pot live include animation, simple interactions with data such as clicking and dragging, 3D plotting of all kinds including surfaces contour lines and custom triangulated data. you can do subplots in matplotlib just as you do with Matlab

## Other packages

| package                                             | Description / Use                                                                                                                                                       |
|:----------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [python](https://docs.python.org/3/)                | Get Python 3                                                                                                                                                            |
| [numpy](http://docs.scipy.org/doc/numpy-dev/dev/)   | basic array types and operations                                                                                                                                        |
| [scipy](http://docs.scipy.org/doc/scipy/reference/) | huge, multipurpose numpy-enhancing package, covering many topics including optimization, matrix operations & linear algebra, spatial data, transforms, and integration. |
| [sympy]()                                           | symbolic equation manipulation                                                                                                                                          |
| [shapely]()                                         | 2d constructive solid geometry, based on libgeos                                                                                                                        |
| [matplotlib]()                                      | the definitive plotting tool for python                                                                                                                                 |
| pyqt / pyside                                       | QT GUI development                                                                                                                                                      |
| pyyaml                                              | yaml file type support                                                                                                                                                  |
| spyder                                              | great GUI for python editing / debug                                                                                                                                    |
| jupyter                                             | great web-based editor for ipython                                                                                                                                      |

[]{#_3vxqpgcw467d .anchor}Packages, modules, etc

One of the hardest things to understand once you started scripting in Python is how to get access to all of the good code that is already out there, and how to use it once you've got it installed. At the heart of this issue is the import command, which permits you to load packages of code. packages are term for many different python files, and the folder structure, support files, and data files which support and Surround it. Packages are distributed in a variety of ways, some historically used more and better than others,. once installed, packages typically live within the python distribution folder system itself. A package is a collection of more than just python files, it is the structure of how those files interact. Python packages, when run, can store data inside them, and access files from within their package, and load other modules. Module is a term for a reusable python file that has functions variables and data inside of it.

typically the import statement can be used to load both packages and modules. Import can be used in a variety of ways, which makes it unclear exactly how it's being used except for on a case-by-case basis. the simplest import statement looks like this

import math

what I just done is imported the math package so that I can use it . just from this line of code it is impossible to tell whether the math is a module parentheses file, for a package, folder structure with many files,. Find out I type

type(math)

I do know running or after running this line of code, is that when I want to access functions within math, I will have to access them by typing

math. Math function

the import statement imported
