# Linear Search CI Project

![CI](https://github.com/calindan12/linear-search-ci/actions/workflows/ci.yml/badge.svg)

## Descriere

Acest proiect implementează și testează funcția `linear_search` folosind:
- black box testing
- white box testing
- random testing
- mutation testing

Pipeline-ul CI/CD este realizat folosind GitHub Actions și rulează automat la fiecare push în repository.

---

## Structura proiectului

repo/
├── README.md
├── src/
│ ├── linear_search.py
│ └── oracle.py
├── tests/
│ ├── test_black_box.py
│ ├── test_white_box.py
│ └── test_random.py
├── .github/
│ └── workflows/
│ └── ci.yml
└── requirements.txt

---

## Rulare locală

Instalare dependențe:

```bash
pip install -r requirements.txt
