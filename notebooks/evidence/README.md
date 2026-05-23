# Notebook Evidence

This folder stores external evidence files referenced by Jupyter notebooks.

Use one subfolder per experiment ID:

```text
notebooks/evidence/EXP-0001/
notebooks/evidence/EXP-0002/
```

Recommended content:

- small command output captures;
- screenshots used by the notebook;
- generated JSON or CSV outputs;
- lightweight logs needed to reproduce analysis.

Avoid committing large videos, ROS bag files, or bulky generated artifacts unless they are
explicitly required as reviewed evidence.
