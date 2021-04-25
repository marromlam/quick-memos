# quick-memos



## Motivation

The treatment of physical data should be simple, to devote more time to reasoning the results. S app is born with that intention: to simplify the process of elaboration of laboratory notes.



## Features

S app includes several simple utilities that allow you to perform in just a few clicks the most common tasks in a data processing. These utilities range from an assistant to add data to a csv file (in a suitable system), to the propagation of uncertainties any mathematical expression going through the goodness test of an adjustment or to the possibility of exporting the results to other platforms (ie Mathematica or LaTeX).



## Tutorial

To launch the program we simply need to open the console. We write
```bash
python3 ProjectMaker.py
```
and pressed enter. This will launch a graphical application with a series of tabs that we will explain next.

By default the location is setted in `Desktop/New`, but obviously it can bechanged at the user’s whim. 
It is also necessary to look in ProjectMaker.py and replace the line that have suser written and adapt
them to the final user. Personally I have the application in `Documents/Python/ProjectMaker` and the
new projects I create are placed in `/Desktop`. This line is number 461:
```
self.ProjectNameBox.setText('/Users/suser/Desktop/New')
```



### Add data assistant

You can add data (data + uncertainty) in Add Tab. When Save is pressed S app stores info in a CSV file located in ~/New/Data/Data.csv. If you use macOS I would recommend you to use Table Tool. It is a very simple CSV editor from MIT, but perfect for this purpose.



### Exporter

One of the worst parts you can face is having to translate the data you have taken between different languages. Do not do it again! With S app it is very simple. You can export your data from CSV to LaTeX (in the form of tables) and to Mathematica (to make plots and fits).

Multiple selection is allowed, even if data arrays are not the same length (for LaTeX tables). If you are exporting to Mathematica, then be careful: the first variable you select is X axis one and de second the Y one (you can export only by pairs, in the future single export will be implemented).



### Statistics

Making data averages is super common work. S app makes means of variables of direct measurements (using a t-Student test to calculate the confidence interval); and also of indirect measures, in which case it uses the conventional method of uncertainties propagation  (with partial derivatives).
You can add any coverage factor although some of the most common ones are listed. Nowadays, the two copy buttons do not work, but their function will be implemented soon.



### χ2 –Test

The χ2–test of godness-of-fit is the daily bread in Physics. Here it is trivial to do it, a list of parameters p is presented, to which the value obtained during an adjustment is given. Finally write y = f (x, p) and the program will do the test.



### Propagation of uncertainties

This is one of the most stubborn parts when it comes to analyzing physical data. S app takes the analytic function in function of the symbolic variables that are defined in Data.csv and derives the calculation by calculating the uncertainties of the derived magnitude. That easy!
