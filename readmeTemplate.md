```buildoutcfg
Developer's note:
The file readme.md is program generated. Do not edit it. Edit readmeTemplate.md instead.
```

**Introduction**

The python program *Abacus* generates random practice problems for [abacus](https://en.wikipedia.org/wiki/Abacus). The
main features are:
* a list of well-designed steps (each step corresponds to a set of skills) 
* interactive interface that allows you to choose the step(s) to practice
* printer-friendly HTML output

**Prerequisite**

Install Python 3.7.4 or later. See [Download Python](https://www.python.org/downloads/).


**Usage**

Clone this repository, cd into the repository root directory, and then run the script `abacus.py` (Python 3 required). In the console, you will
see the complete list of steps and will be asked to enter the steps you want to practice. You may enter a range (e.g. 1-3), a number (e.g. 5), or a mix of both separated by commas (e.g. 1-3, 5).

```buildoutcfg
{steps}

Choose steps (e.g. 1-3, 5):
```

**Output**

After you enter the steps, some HTML files will be generated in the output directory. You will find the file
`output/steps.html` which contains the complete list of steps for your reference. For each of the chosen step,
one HTML file will be generated. For example, if you entered "3 - 5, 8", then you will find the following output files.
* output/steps.html
* output/03.html
* output/04.html
* output/05.html
* output/08.html

Here is an example screenshot for `output/08.html`. (Since the problems are randomly generated, you will likely get a
different set of problems if you run `abacus.py`.)

![screenshot](./img/problems.png)