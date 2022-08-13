import re
from playwright.sync_api import Page, expect


def test_cpuinfo(page: Page):
    page.goto("http://localhost:8000")
    plot = page.locator("#plot")
    expect(plot).to_have_class(re.compile(r"\bshiny-bound-output\b"))
    img = plot.locator(">img")
    expect(img).to_have_attribute("src", re.compile(".{1000}"))
