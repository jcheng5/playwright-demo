This repo demonstrates the usage of [Playwright](https://playwright.dev/python/) with [Shiny for Python](https://shiny.rstudio.com/py/).

To initialize (with virtualenv):

```sh
# Create virtualenv
python3 -m venv .venv
# Activate virtualenv
source .venv/bin/activate

# Bootstrap virtualenv
pip install -U pip wheel
pip install -r requirements.txt

# Install playwright browsers
playwright install
```

To test, in a separate Terminal window, start the Shiny app:
```sh
# Activate virtualenv
source .venv/bin/activate

# Run the app
shiny run
```

Back in the original Terminal window:
```sh
pytest
```
