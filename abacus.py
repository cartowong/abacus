import os
import random

from typing import List

from Core import Problem, Step
from Steps import steps


def main():
    for index, skill in enumerate(steps, start=1):
        print(f"Step {index}: {skill.description()}")
    raw_choices = input("\nChoose step(s) (e.g. 1-3, 5): ")
    choices = parse_choices(raw_choices)
    choices = filter_choices(choices, 1, len(steps))
    response(steps, choices)


def clear_dir(dir: str, extension: str) -> None:
    """
    Delete all files in the given directory with the given extension.
    :param dir: the path of the directory
    :param extension: type of the files to be deleted
    """
    files = [f for f in os.listdir(dir) if f.endswith(extension)]
    for f in files:
        os.remove(os.path.join(dir, f))


def parse_choices(choices_string: str) -> List[int]:
    """
    Parse the raw choices.

    For example, the string "1 - 2, 3,5-7" is parsed into the list [1, 2, 3, 5, 6, 7].

    :param choices_string: the raw choices
    :return: the parsed choices
    """
    ranges = [r.strip() for r in choices_string.split(',')]
    choices = list()
    for r in ranges:
        bounds = [b.strip() for b in r.split('-')]
        if len(bounds) == 0 or len(bounds) > 2:
            raise Exception(f"Invalid range {r}")
        if len(bounds) == 1:
            choices.append(int(bounds[0]))
            continue
        else:
            lower = int(bounds[0])
            upper = int(bounds[1])
            choices = choices + list(range(lower, upper + 1))
    return choices


def filter_choices(choices: List[int], lower: int, upper: int) -> List[int]:
    """
    Filter the choices.

    :param choices: list of integer choices
    :param lower: inclusive lower bound
    :param upper: inclusive upper bound
    :return: the filtered choices with invalid (out of range) and duplicate integers removed
    """
    filtered_choices = [c for c in choices if lower <= c <= upper]
    return list(dict.fromkeys(filtered_choices))


def response(steps: List[Step], choices: List[int]) -> None:
    """
    Produce a response (output) to the console.

    :param steps: the list of all steps
    :param choices: the integer choices that represent the steps from the menu
    """
    print(f"Your choice(s): {','.join([str(x) for x in choices])}\n")

    # Create the output directory and clean up output files from the previous run.
    if not os.path.exists("output"):
        os.mkdir("output")
    clear_dir("output", "html")

    # Output the complete list of steps and update the readme file.
    output_steps(steps, os.path.join("html", "stepsTemplate.html"), os.path.join("output", "steps.html"))
    update_readme(steps, "readmeTemplate.md", "readme.md")
    print("")

    # Output the problem sets as HTML files (one step per file).
    num_problems = 15
    for c in choices:
        step = steps[c-1]
        problems = generate_problems(step, num_problems)
        output_problems(
            problems,
            step.description(),
            os.path.join("html", "problemsTemplate.html"),
            os.path.join("output", f"{c:02d}.html"))


def generate_problems(step: Step, n: int) -> List[Problem]:
    """
    Generate n distinct problems from the given step.

    :param step: the given step
    :param n: the number of problems to generate
    :return: the chosen problems
    """
    problem_set = set()
    while len(problem_set) < n:
        problem_set.add(step.sample())

    return list(problem_set)


def output_problems(problems: List[Problem], step_description: str, template_path: str, output_path: str) -> None:
    """
    Output the given problems to an HTML file.

    :param problems: the problems
    :param step_description: the description of the step
    :param template_path: path of the template file
    :param output_path: path of the output file
    :return: void
    """
    with open(template_path, "r") as fin, open(output_path, "w") as fout:
        text = fin.read()
        for index, problem in enumerate(problems, start=1):
            text = text.replace("{step}", step_description)
            text = text.replace(f"{{a{index}}}", str(problem.a()))
            text = text.replace(f"{{b{index}}}", signed_int(problem.b()))
            text = text.replace(f"{{c{index}}}", signed_int(problem.c()))
        fout.write(text)
    print(f"Output file created: {output_path}")


def output_steps(steps: List[Step], template_path: str, output_path: str) -> None:
    """
    Output the full list of steps to an HTML file.

    :param steps: the steps
    :param template_path: path of the template file
    :param output_path: path of the output file
    """
    with open(template_path, "r") as fin, open(output_path, "w") as fout:
        text = fin.read()
        steps_html = f"<ol><li>{'</li><li>'.join(s.description() for s in steps)}</li></ol>"
        text = text.replace("{steps}", steps_html)
        fout.write(text)
    print(f"The full list of steps has been written into {output_path}.")


def update_readme(steps: List[Step], template_path: str, output_path: str) -> None:
    """
    Update the readme file.

    :param steps: the steps
    :param template_path: path of the template file
    :param output_path: path of the output file
    """
    with open(template_path, "r") as fin, open(output_path, "w") as fout:
        text = fin.read()
        replace_text = "\n".join([f"Step {j+1}: {steps[j].description()}" for j in range(0, len(steps))])
        text = text.replace("{steps}", replace_text)
        fout.write(text)
    print(f"The file {output_path} has been updated.")


def signed_int(x: int) -> str:
    """
    Get the string representation of a signed integer, e.g. "+3" or "-4".
    :param x: the given integer
    :return: the signed integer as a string
    """
    return f"+{x}" if x >= 0 else str(x)


if __name__ == "__main__":
    main()
