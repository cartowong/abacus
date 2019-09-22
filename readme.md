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
Step 1: Single digit addition or subtraction
Step 2: Single digit addition or subtraction (allow upper bead)
Step 3: Simple addition or subtraction
Step 4: Simple addition or subtraction (allow upper bead)
Step 5: +1 = -4 + 5
Step 6: -1 = +4 - 5
Step 7: +1 = -4 + 5, -1 = +4 - 5
Step 8: +2 = -3 + 5
Step 9: -2 = +3 - 5
Step 10: +2 = -3 + 5, -2 = +3 - 5
Step 11: +3 = -2 + 5
Step 12: -3 = +2 - 5
Step 13: +3 = -2 + 5, -3 = +2 - 5
Step 14: +4 = -1 + 5
Step 15: -4 = +1 - 5
Step 16: +4 = -1 + 5, -4 = +1 - 5
Step 17: Combo - steps 7, 10, 13, 16
Step 18: No carry or borrow
Step 19: +5 = -5 + 10
Step 20: -5 = +5 - 10
Step 21: +5 = -5 + 10, -5 = +5 - 10
Step 22: +6 = -4 + 10
Step 23: -6 = +4 - 10
Step 24: +6 = -4 + 10, -6 = +4 - 10
Step 25: +7 = -3 + 10
Step 26: -7 = +3 - 10
Step 27: +7 = -3 + 10, -7 = +3 - 10
Step 28: +8 = -2 + 10
Step 29: -8 = +2 - 10
Step 30: +8 = -2 + 10, -8 = +2 - 10
Step 31: +9 = -1 + 10
Step 32: -9 = +1 - 10
Step 33: +9 = -1 + 10, -9 = +1 - 10
Step 34: Combo - steps 21, 24, 27, 30, 33
Step 35: +1 = -9 + 10
Step 36: -1 = +9 - 10
Step 37: +1 = -9 + 10, -1 = +9 - 10
Step 38: +2 = -8 + 10
Step 39: -2 = +8 - 10
Step 40: +2 = -8 + 10, -2 = +8 - 10
Step 41: +3 = -7 + 10
Step 42: -3 = +7 - 10
Step 43: +3 = -7 + 10, -3 = +7 - 10
Step 44: +4 = -6 + 10
Step 45: -4 = +6 - 10
Step 46: +4 = -6 + 10, -4 = +6 - 10
Step 47: Combo - steps 37, 40, 43, 46
Step 48: Combo - steps 21, 24, 27, 30, 33, 37, 40, 43, 46

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