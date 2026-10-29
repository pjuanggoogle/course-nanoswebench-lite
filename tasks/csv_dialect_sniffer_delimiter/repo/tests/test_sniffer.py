import pytest
from csv_sniffer.sniffer import CSVDialectSniffer

def test_clean_comma_separated():
    text = "id,name,age\n1,alice,30\n2,bob,25"
    s = CSVDialectSniffer()
    assert s.sniff(text) == ","

def test_semicolon_with_quoted_commas():
    # Commas inside quotes outnumber delimiter semicolons (6 commas vs 4 semicolons)
    text = 'id;full_name;score\n1;"Doe, Jane, PhD, MD";95\n2;"Smith, Bob, Jr., Esq.";88'
    s = CSVDialectSniffer()
    assert s.sniff(text) == ";"

def test_pipe_delimited_with_tabs():
    # Tabs inside notes outnumber delimiter pipes
    text = 'name|note\nAlpha|"tab1\ttab2\ttab3"\nBeta|"tab4\ttab5\ttab6"'
    s = CSVDialectSniffer()
    assert s.sniff(text) == "|"
