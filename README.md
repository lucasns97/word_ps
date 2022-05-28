# WORD PS

## A module for word similarity evaluation

**Author**: *Lucas Nunes Sequeira*

### Instalation

**Installing the dependency**

```bash
$ pip install word-ps
```

### Using

**Weighted Similarity**

This method calculates a number between 0 and 1 to measure how to strings are similar to each other. It uses continuous substring matching weighted by the strings lengths.

**Example**
```python
from word_ps.word_similarity import weighted_similarity

string1 = "I love banana"
string2 = "I love pinaple"

score = word_similarity(string1, string2)
```

### Updating package

1. Install twine
    ```bash
    $ pip install twine
    ```
2. Check you are in the root of the project
    ```bash
    ~/.../word_ps$ ls
    dist  LICENCE  pyproject.toml  README.md  requirements.txt  setup.cfg  setup.py  src  tests
    ```
3. Run setup:
    ```bash
    $ python setup.py sdist
    ```
4. Run twine (*check if ```dist/``` has only latest package*):
    ```bash
    $ twine upload dist/*
    ```
5. Update git:
    ```bash
    $ git add . && git commit -m "update dist files" && git push
    ```