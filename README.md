# Take Home Project

Challenge: A directory contains multiple files and directories of non-uniform file and directory names. Create a program that traverses a base directory and creates an index file that can be used to quickly lookup files by name, size, and content type.

# Usage
### Prerequisites
- Python 3.9
- pip

### Installation
1. ```git clone git@github.com:sbontop/predictAP.git```
2. ```cd predictAP```
3. ```poetry install```

### Usage
1. ```poetry shell```
2. ```python src/main.py```
- Please note you'll be using either the cached data from `src/index/index.json` or parse data to generate index from `src/test_data/` directory.
- `src/test_data/` looks like this:
```
(predictap-py3.9) ➜  predictAP git:(main) ✗ tree src/test_data -h
[ 192]  src/test_data
├── [ 128]  data
│   ├── [  21]  user1.json
│   └── [  22]  user2.json
├── [ 19K]  linear-regression-plot.jpg
├── [166K]  random-forest.png
└── [6.4K]  sample.pdf

2 directories, 5 files
```

### Testing
1. ```make unit-test```
- You'll find the tests for every module under `tests/unit/` directory.
- Note: Unit and e2e tests weren't added since considered unnecessary. Consider adding your own tests as you may need.

### Extras
- Implemented Git Pre-commit Hooks to encourage developers to write clean code and follow best practices.
- Implemented SOLID principles.
- Implemented a Makefile to write useful commands.
