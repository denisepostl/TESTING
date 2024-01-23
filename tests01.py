import pytest
import os.path
from main import CSVToXML

obj = CSVToXML('in.csv', 'out.csv')

# tests import_file method


def test_check_file():
    path = "in.csv"
    check_file = os.path.isfile(path)
    assert check_file == True


def test_reading():
    result = obj.import_file()
    expected_content = ['Verkaufspreis,Verkaufsmenge\n', '12,10\n', '1,2']
    assert result == expected_content

# test transform method


@pytest.mark.xfail
def test_transform_empty_data_fail():
    obj.data = []
    result = obj.transform()
    assert result == '<DATA></DATA>\n'


def test_transform_rows():
    obj.data = [[12, 10], [1, 2]]
    obj.headers = ['Verkaufspreis', 'Verkaufsmenge']
    result = obj.transform()
    expected_result = (
        '<DATA>\n'
        ' <ROW>\n'
        '    <Verkaufspreis>12</Verkaufspreis>\n'
        '    <Verkaufsmenge>10</Verkaufsmenge>\n'
        ' </ROW>\n'
        ' <ROW>\n'
        '    <Verkaufspreis>1</Verkaufspreis>\n'
        '    <Verkaufsmenge>2</Verkaufsmenge>\n'
        ' </ROW>\n'
        '</DATA>\n'
    )
    assert result == expected_result

# test export method


@pytest.mark.xfail
def test_check_if_not_empty():
    path = "out.xml"
    assert os.path.exists(path)
    with open(path, 'r') as f:
        cont = f.read()
    assert cont.strip() != ""
