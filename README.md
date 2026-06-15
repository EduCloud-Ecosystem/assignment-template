# &lt;HW-NN&gt;: &lt;Assignment Title&gt;

> **Instructors:** this repo is a *template*. The block directly below explains how
> to turn it into a real assignment. **Delete everything from here down to the
> `---` divider before you publish to students** — only the section under the
> divider should reach them.

## 🧑‍🏫 For instructors — customizing this template

This template is the standard layout: students implement functions in `ds.py`,
your tests live in `test_ds.py`, and grading is driven by **`grading.json`** (for
Quad) and, optionally, `.github/workflows/classroom.yml` (for GitHub Classroom).

The example assignment shipped here (`load_rows` / `clean_rows` / `add_field` /
`mean_of`) is **standard-library only**, so it runs and grades on `python:3.12-slim`
with no image to build — useful for confirming your Quad pipeline end to end
before you write the real thing.

### Steps to make a new assignment

1. **Define the work in `ds.py`.** Replace the example functions with your own
   stubs. Keep the house style: a module docstring, type-hinted signatures, a
   docstring per function, `# TODO:` hints, and a `raise NotImplementedError(...)`
   body so an unimplemented submission fails loudly rather than silently passing.

2. **Write `test_ds.py`.** One `test_*` method per function (or per behavior you
   want to award points for). Keep the `setUpClass` synthetic-data pattern so the
   tests don't depend on the real dataset. **The class name and method names are
   what the grader references**, so keep them in sync with `grading.json`.

3. **Set the score in `grading.json`.** One entry per test method, each with its
   `points`, summing to your unit-test total. Update the `name`s and the
   `test_ds.ClassName.test_method` paths in each `run`. (See *How points work*
   below.)

4. **Add packages, if any.** The example needs none. If your assignment uses
   `pandas`, `scikit-learn`, etc., list them in `requirements.txt` **and bake them
   into a grading image** — grading runs offline (`network: none`), so packages
   cannot be installed at grade time. Build the image from `Dockerfile.grader`,
   push it if your grading host is remote, and set its name as `"image"` in
   `grading.json`. (Pure-stdlib assignments keep `"image": "python:3.12-slim"`.)

5. **Add code-style grading (optional, the "10 pts" in the rubric).** Put `pylint`
   in `requirements.txt`, rebuild the image, and add one more entry to
   `grading.json`:

   ```json
   { "name": "code style (pylint >= 8.0)", "run": "pylint ds.py --fail-under=8.0", "points": 10 }
   ```

   Quad scores it pass/fail, so `--fail-under` makes it a threshold gate (see below).

6. **Add your data.** Drop dataset files in `data/` and reference them from the
   student instructions.

7. **Fill in the student sections** below (title, objectives, the function table,
   any required reflection or bonus parts), then **delete this instructor block.**

8. **Publish.** Push to Forgejo, open the repo's **Settings → check "Template
   Repository"**, then create the Quad assignment pointing at this repo
   (`namespace` = the repo owner, `name` = this repo).

### How points work in Quad

Quad scores each `grading.json` entry **all-or-nothing**: full `points` if the
command exits `0`, otherwise `0`. That's why there's one entry per test method
(so a student earns credit for each test they pass) and why the pylint check is a
`--fail-under` *gate* rather than a scaled 0–10 score. The **"clarity &
documentation" points are graded by hand** — Quad won't compute them.

### Tamper-resistance (optional)

Because `test_ds.py` ships inside the student's repo, a student can edit it. If
that matters, uncomment the `COPY test_ds.py` line in `Dockerfile.grader`,
rebuild, and prefix each unit-test command in `grading.json` with
`cp /opt/grader/test_ds.py ./test_ds.py && …` so the grader always uses the
canonical tests from the image. (You then rebuild the image whenever you change
the tests.)

---

# &lt;HW-NN&gt;: &lt;Assignment Title&gt;

## Objectives

By the end of this assignment you will be able to:

1. &lt;objective&gt;
2. &lt;objective&gt;
3. &lt;objective&gt;

## Environment setup

You need Python 3.10+ and the packages in `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Your repository

Your repo was created for you and contains:

- `ds.py` — your code; implement the functions here.
- `test_ds.py` — the unit tests. **Do not modify.**
- `requirements.txt` — required packages.
- `data/` — the dataset(s) for this assignment.

Clone it and work locally:

```bash
git clone <your-repo-url>
cd <your-repo>
```

## What to implement

Implement the following functions in `ds.py`:

| Function | Description |
| --- | --- |
| `load_rows(file_path)` | &lt;what it should do&gt; |
| `clean_rows(rows)` | &lt;what it should do&gt; |
| `add_field(rows, src, dest)` | &lt;what it should do&gt; |
| `mean_of(rows, field)` | &lt;what it should do&gt; |

Each function has a docstring and `# TODO` hints in `ds.py`.

## Testing your work

Run the unit tests:

```bash
python -m unittest -v
```

Check your code style (aim for a high score):

```bash
pylint ds.py
```

## Submitting

```bash
git add ds.py
git commit -m "Complete <HW-NN>"
git push
```

Grading runs automatically after you push, and again at the deadline. Your repo
is locked once the deadline passes.

## Grading

| Component | Points |
| --- | --- |
| Unit tests | 80 |
| Code style (pylint) | 10 |
| Clarity & documentation | 10 |

**Deductions** — −5 points each:

- Modifying `test_ds.py` or other protected files
- Missing or poor documentation
- Failing to commit the required files

<!--
Optional sections to add per assignment:

## Required: <e.g. analysis, model tuning, overfitting mitigation>
## Required reflection (`notes.md`)
## Bonus (optional)
-->
