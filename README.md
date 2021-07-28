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