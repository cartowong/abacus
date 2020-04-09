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
Step 15: Combo - steps 11, 14 (+/- 1, 2)
Step 16: +3 = -2 + 5
Step 17: -3 = +2 - 5
Step 18: +3 = -2 + 5, -3 = +2 - 5
Step 19: +4 = -1 + 5
Step 20: -4 = +1 - 5
Step 21: +4 = -1 + 5, -4 = +1 - 5
Step 22: Combo - steps 18, 21 (+/- 3, 4)
Step 23: Combo - steps 11, 14, 18, 21 (+/- 1, 2, 3, 4)
Step 24: No carry or borrow
Step 25: +5 = -5 + 10
Step 26: -5 = +5 - 10
Step 27: +5 = -5 + 10, -5 = +5 - 10
Step 28: +6 = -4 + 10
Step 29: -6 = +4 - 10
Step 30: +6 = -4 + 10, -6 = +4 - 10
Step 31: +7 = -3 + 10
Step 32: -7 = +3 - 10
Step 33: +7 = -3 + 10, -7 = +3 - 10
Step 34: Combo - steps 27, 30, 33 (+/- 5, 6, 7)
Step 35: +8 = -2 + 10
Step 36: -8 = +2 - 10
Step 37: +8 = -2 + 10, -8 = +2 - 10
Step 38: +9 = -1 + 10
Step 39: -9 = +1 - 10
Step 40: +9 = -1 + 10, -9 = +1 - 10
Step 41: Combo - steps 37, 40 (+/- 8, 9)
Step 42: Combo - steps 27, 30, 33, 37, 40 (+/- 5, 6, 7, 8, 9)
Step 43: +1 = -9 + 10
Step 44: -1 = +9 - 10
Step 45: +1 = -9 + 10, -1 = +9 - 10
Step 46: +2 = -8 + 10
Step 47: -2 = +8 - 10
Step 48: +2 = -8 + 10, -2 = +8 - 10
Step 49: Combo - steps 45, 48 (+/- 1, 2)
Step 50: +3 = -7 + 10
Step 51: -3 = +7 - 10
Step 52: +3 = -7 + 10, -3 = +7 - 10
Step 53: +4 = -6 + 10
Step 54: -4 = +6 - 10
Step 55: +4 = -6 + 10, -4 = +6 - 10
Step 56: Combo - steps 52, 55 (+/- 3, 4)
Step 57: Combo - steps 45, 48, 52, 55 (+/- 1, 2, 3, 4)
Step 58: Combo - steps 42, 57 (+/- 1, 2, ..., 9)
Step 59: +6 = +1 - 5 + 10
Step 60: -6 = -1 + 5 - 10
Step 61: +6 = +1 - 5 + 10, -6 = -1 + 5 - 10
Step 62: +7 = +2 - 5 + 10
Step 63: -7 = -2 + 5 - 10
Step 64: +7 = +2 - 5 + 10, -7 = -2 + 5 - 10
Step 65: Combo - steps 61, 64 (+/- 6, 7)
Step 66: +8 = +3 - 5 + 10
Step 67: -8 = -3 + 5 - 10
Step 68: +8 = +3 - 5 + 10, -8 = -3 + 5 - 10
Step 69: +9 = +4 - 5 + 10
Step 70: -9 = -4 + 5 - 10
Step 71: +9 = +4 - 5 + 10, -9 = -4 + 5 - 10
Step 72: Combo - steps 68, 71 (+/- 8, 9)
Step 73: Combo - steps 61, 64, 68, 71 (+/- 6, 7, 8, 9)
Step 74: From 4x to 5x
Step 75: From 5x to 4x
Step 76: Combo - steps 74, 75 (from 4x to 5x or 5x to 4x)
Step 77: From 9x to 10x
Step 78: From 10x to 9x
Step 79: Combo - steps 77, 78 (from 9x to 10x or 10x to 9x)
Step 80: Combo - steps 74, 75, 77, 78

Choose steps (e.g. 1-3, 5):
```

**Output**

After you enter the steps, some HTML files will be generated in the output directory. You will find the file
`output/steps.html` which contains the complete list of steps for your reference. For each of the chosen step,
one HTML file will be generated. For example, if you entered "3 - 5, 14", then you will find the following output files.
* output/steps.html
* output/03.html
* output/04.html
* output/05.html
* output/14.html

Here is a screenshot for `output/14.html`. (Since the problems are randomly generated, you will likely get a
different set of problems if you run `abacus.py`.)

![screenshot](./img/problems.png)