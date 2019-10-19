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
Step 1: One-digit simple addition
Step 2: One-digit simple subtraction
Step 3: One-digit simple addition or subtraction (lower bead only)
Step 4: One-digit simple addition or subtraction (allow upper bead)
Step 5: Simple addition
Step 6: Simple subtraction
Step 7: Simple addition or subtraction (lower bead only)
Step 8: Simple addition or subtraction (allow upper bead)
Step 9: +1 = -4 + 5
Step 10: -1 = +4 - 5
Step 11: +1 = -4 + 5, -1 = +4 - 5
Step 12: +2 = -3 + 5
Step 13: -2 = +3 - 5
Step 14: +2 = -3 + 5, -2 = +3 - 5
Step 15: +3 = -2 + 5
Step 16: -3 = +2 - 5
Step 17: +3 = -2 + 5, -3 = +2 - 5
Step 18: +4 = -1 + 5
Step 19: -4 = +1 - 5
Step 20: +4 = -1 + 5, -4 = +1 - 5
Step 21: Combo - steps 11, 14, 17, 20
Step 22: No carry or borrow
Step 23: +5 = -5 + 10
Step 24: -5 = +5 - 10
Step 25: +5 = -5 + 10, -5 = +5 - 10
Step 26: +6 = -4 + 10
Step 27: -6 = +4 - 10
Step 28: +6 = -4 + 10, -6 = +4 - 10
Step 29: +7 = -3 + 10
Step 30: -7 = +3 - 10
Step 31: +7 = -3 + 10, -7 = +3 - 10
Step 32: +8 = -2 + 10
Step 33: -8 = +2 - 10
Step 34: +8 = -2 + 10, -8 = +2 - 10
Step 35: +9 = -1 + 10
Step 36: -9 = +1 - 10
Step 37: +9 = -1 + 10, -9 = +1 - 10
Step 38: Combo - steps 25, 28, 31, 34, 37
Step 39: +1 = -9 + 10
Step 40: -1 = +9 - 10
Step 41: +1 = -9 + 10, -1 = +9 - 10
Step 42: +2 = -8 + 10
Step 43: -2 = +8 - 10
Step 44: +2 = -8 + 10, -2 = +8 - 10
Step 45: +3 = -7 + 10
Step 46: -3 = +7 - 10
Step 47: +3 = -7 + 10, -3 = +7 - 10
Step 48: +4 = -6 + 10
Step 49: -4 = +6 - 10
Step 50: +4 = -6 + 10, -4 = +6 - 10
Step 51: Combo - steps 41, 44, 47, 50
Step 52: Combo - steps 25, 28, 31, 34, 37, 41, 44, 47, 50

Choose steps (e.g. 1-3, 5):
```

**Output**

After you enter the steps, some HTML files will be generated in the output directory. You will find the file
`output/steps.html` which contains the complete list of steps for your reference. For each of the chosen step,
one HTML file will be generated. For example, if you entered "3 - 5, 12", then you will find the following output files.
* output/steps.html
* output/03.html
* output/04.html
* output/05.html
* output/12.html

Here is a screenshot for `output/12.html`. (Since the problems are randomly generated, you will likely get a
different set of problems if you run `abacus.py`.)

![screenshot](./img/problems.png)