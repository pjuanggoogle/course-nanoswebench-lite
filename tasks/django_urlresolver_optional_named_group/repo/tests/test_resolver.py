import pytest
from django_urls.resolver import reverse_pattern

def test_required_and_present_optional():
    pat = r"articles/(?P<slug>\w+)/(?:page/(?P<page>\d+)/)?"
    assert reverse_pattern(pat, slug="news", page=2) == "articles/news/page/2/"

def test_omitted_or_none_optional_group():
    pat = r"articles/(?P<slug>\w+)/(?:page/(?P<page>\d+)/)?"
    assert reverse_pattern(pat, slug="news") == "articles/news/"
    assert reverse_pattern(pat, slug="news", page=None) == "articles/news/"
