---
title: Managing Environment with UV
categories:
    - 學習筆記
tags:
    - Python
    - UV
date: 2026-03-15 23:30:58
cover: /img/cover/uv.png
---

This is a note I wrote for my job about managing python environment with UV.

# What is UV?

- Github: https://github.com/astral-sh/uv
- Doc: https://docs.astral.sh/uv/

UV is just like poetry, but with powerful management on python version.
Comparison with poetry: https://blog.kyomind.tw/introducing-uv/.

![](img/post/2026_03/uv-compare.svg)
*Installing [Trio](https://trio.readthedocs.io/)'s dependencies with a warm cache.*

# Installation

```bash
# Installing via pip is possible but not recommended.

# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# Update
uv self update

# Help
uv help
```

# Basic Operations

- Ref: https://dev.to/codemee/shi-yong-uv-guan-li-python-huan-jing-53hg

```bash
# Init a new project (this will create a folder name xxx)
uv init xxx

# Create a new venv (this will create a folder name .venv)
uv venv
uv venv --python 3.xx

# List packages
uv pip list

# Add / install packages 
uv add xxx==x.x.x
uv pip install xxx1,xxx2

# Remove / uninstall packages
uv remove xxx
uv pip uninstall xxx1,xxx2

# Lock exact version of packages
uv lock

# Install (or sync) libraries in lock file to venv
uv sync
```

You can run your script using

```bash
# Run script
uv run xxx.py
# Or
uv run python xxx.py
```

Or you can enter the virtual environment first

```bash
# Activate the venv
source .venv/bin/activate

# After activated it, run script
python xxx.py
```

# Python Version Control

```bash
# List available python versions
uv python list

# Install latest python version
uv python install

# Install specific version of python
uv python install 3.xx

# Uninstall
uv python uninstall 3.xx
```

# Run script fast using —with and cache

```bash
# Run py with given packages
# This will run xxx.py with xxx1 and xxx2
uv run --with xxx1,xxx2 xxx.py

# Check cache dir
uv cache dir

# Clean cache
uv cache clean
```

# Migrate from Poetry / pip

- Ref: https://github.com/mkniewallner/migrate-to-uv
- Ref: https://stackoverflow.com/questions/79118841/how-can-i-migrate-from-poetry-to-uv-package-manager

With existing poetry`pyproject.toml` or pip `requirements.txt`, just run the following command for migration.

```bash
# With uv
uvx migrate-to-uv

# With pipx
pipx run migrate-to-uv
```

You may need to run `uv lock` afterward if there are not `uv.lock`. Run `uv sync` if you want to sync the environment from lock file into your local .venv.

# Using UV on Pytorch

- Ref: https://docs.astral.sh/uv/guides/integration/pytorch/

Take torch==2.4.0 with CUDA 12.4 as example:

```bash
# With given index
uv add torch==2.4.0 --index https://download.pytorch.org/whl/cu124
```

Or add this block in `pyproject.toml`:
```bash
[[tool.uv.index]]
name = "pytorch-cu124"
url = "https://download.pytorch.org/whl/cu124"
explicit = true
```

# Using Jupyter Notebook in VSCode
```bash
uv add ipykernel

# Register kernel
uv run python -m ipykernel install --user --name {name}  --display-name {name}
```

![](img/post/2026_03/uv-meme.png)