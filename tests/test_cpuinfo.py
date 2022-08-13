import re
from playwright.sync_api import Page, expect


def test_cpuinfo(page: Page):
    page.goto("http://localhost:8000")

    # Find the 'plot' output, and see that Shiny has found it (i.e., .shiny-bound-output)
    plot = page.locator("#plot")
    expect(plot).to_have_class(re.compile(r"\bshiny-bound-output\b"))

    # Check that the plot contains an img tag with a data URI that's >1000 characters long
    img = plot.locator(">img")
    expect(img).to_have_attribute("src", re.compile("^data:image/png;base64,.{1000}"))
