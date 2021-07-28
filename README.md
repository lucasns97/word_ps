# WORD PS

## A module for word similarity evaluation

**Author**: *Lucas Nunes Sequeira*

### Instalation

**Installing the dependency**

```bash
$ pip install word_ps
```

### Using

**Weighted Similarity**

This method calculates a number between 0 and 1 to measure how to strings are similar to each other. It uses continuous substring matching weighted by the strings lengths.

*Example*
```python
from word_ps.word_similarity import weighted_similarity

string1 = "I love banana"
string2 = "I love pinaple"

score = word_similarity(string1, string2)
```

### Updating package

0. Install twine
    ```bash
    $ pip install twine
    ```
1. Check you are in the root of the project
    ```bash
    ~/.../word_ps$ ls
    dist  LICENCE  pyproject.toml  README.md  requirements.txt  setup.cfg  setup.py  src  tests
    ```
2. Run setup:
    ```bash
    $ python setup.py sdist
    ```
3. Run twine:
    ```bash
    $ twine upload dist/*
    ```
    *Check if dist/ has only latest package*
4. Update git:
    ```bash
    $ git add . && git commit -m "update dist files" && git push
    ```