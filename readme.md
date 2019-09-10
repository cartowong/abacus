```buildoutcfg
Developer's note:
The file readme.md is program generated. Do not edit it. Edit readmeTemplate.md instead.
```

**Introduction**

The python program *Abacus* generates random practice problems for [abacus](https://en.wikipedia.org/wiki/Abacus). The
main features are:
* interactive interface that allows you to customize the problems for a specific set of skills
* printer-friendly HTML output

**Prerequisite**

Install Python 3.7.4 or later. See [Download Python](https://www.python.org/downloads/).


**Usage**

Clone this repository, cd into the repository root folder, and then run `python3 abacus.py`. In the console, you will
see the complete list of steps and will be asked to enter the steps you want to practice.

```buildoutcfg
Step 1: Simple addition or subtraction
Step 2: Simple addition or subtraction (allow upper bead)
Step 3: +1 = -4 + 5
Step 4: -1 = +4 - 5
Step 5: +1 = -4 + 5, -1 = +4 - 5
Step 6: +2 = -3 + 5
Step 7: -2 = +3 - 5
Step 8: +2 = -3 + 5, -2 = +3 - 5
Step 9: +3 = -2 + 5
Step 10: -3 = +2 - 5
Step 11: +3 = -2 + 5, -3 = +2 - 5
Step 12: +4 = -1 + 5
Step 13: -4 = +1 - 5
Step 14: +4 = -1 + 5, -4 = +1 - 5
Step 15: Combo - steps 5, 8, 11, 14
Step 16: No carry or borrow

Choose steps (e.g. 1-3, 5):
```

**Output**

After you enter the steps, two HTML files will be generated.
* output/steps.html
* output/problems.html

The first file contains the complete list of steps for your reference. The second file is a well-formatted HTML
document which you may print out.

![screenshot](./img/problems.png)