# Task 1 - Local setup of `humanize` (Python)

```bash
# 1. the open-source project under test
git clone https://github.com/python-humanize/humanize.git
# 2. this test-automation repo
git clone https://github.com/f243077-cell/Python-Humanize.git
cd Python-Humanize
python -m venv .venv && source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ../humanize                                # install the project from source (needs git for version)
pip install -r requirements-test.txt
python -c "import humanize; print(humanize.intcomma(1234567))"   # -> 1,234,567
python -m pytest                                          # all tests
```
Requires Python >= 3.11. Without the source clone, `pip install -r requirements-test.txt` installs `humanize` from PyPI.
See `docs/Video_Recording_Script.md` for the setup video.
