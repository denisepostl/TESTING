import pytest
import os
from main import CSVToXML 

@pytest.fixture
def sample_csv_data():
    """
    Fixture providing sample CSV data as a string.
    """
    return 'Name,Age,Location\nJohn,25,New York\nJane,30,San Francisco\n'

@pytest.fixture
def sample_csv_file(tmp_path, sample_csv_data):
    """
    Fixture creating a temporary CSV file with sample data.
    """
    file_path = tmp_path / "test_input.csv"
    with open(file_path, 'w') as f:
        f.write(sample_csv_data)
    return file_path

@pytest.fixture
def sample_xml_file(tmp_path):
    """
    Fixture providing a temporary XML file path.
    """
    return tmp_path / "test_output.xml"

def test_import_file(sample_csv_file, sample_csv_data):
    """
    Test the import_file method of CSVToXML class.
    """
    csv_to_xml = CSVToXML(str(sample_csv_file), "dummy.xml")
    imported_data = csv_to_xml.import_file()
    assert ''.join(imported_data) == sample_csv_data
    
def test_transform(sample_csv_file, sample_csv_data):
    """
    Test the transform method of CSVToXML class.
    """
    csv_to_xml = CSVToXML(str(sample_csv_file), "dummy.xml")
    xml_content = csv_to_xml.transform()

    expected_xml = '<DATA>\n <ROW>\n    <Name>John</Name>\n    <Age>25</Age>\n    <Location>New York</Location>\n </ROW>\n <ROW>\n    <Name>Jane</Name>\n    <Age>30</Age>\n    <Location>San Francisco</Location>\n </ROW>\n</DATA>\n'

    assert xml_content == expected_xml

def test_export(sample_csv_file, sample_xml_file):
    """
    Test the export method of CSVToXML class.
    """
    csv_to_xml = CSVToXML(str(sample_csv_file), str(sample_xml_file))
    csv_to_xml.export()

    assert sample_xml_file.is_file()

    with open(sample_xml_file, 'r') as f:
        exported_data = f.read()

    expected_xml = '<DATA>\n <ROW>\n    <Name>John</Name>\n    <Age>25</Age>\n    <Location>New York</Location>\n </ROW>\n <ROW>\n    <Name>Jane</Name>\n    <Age>30</Age>\n    <Location>San Francisco</Location>\n </ROW>\n</DATA>\n'

    assert exported_data == expected_xml

def test_integration(sample_csv_file, sample_xml_file):
    """
    Test the integration of CSVToXML class by exporting and checking the output.
    """
    csv_to_xml = CSVToXML(str(sample_csv_file), str(sample_xml_file))
    csv_to_xml.export()

    assert sample_xml_file.is_file()

    with open(sample_xml_file, 'r') as f:
        exported_data = f.read()

    expected_xml = '<DATA>\n <ROW>\n    <Name>John</Name>\n    <Age>25</Age>\n    <Location>New York</Location>\n </ROW>\n <ROW>\n    <Name>Jane</Name>\n    <Age>30</Age>\n    <Location>San Francisco</Location>\n </ROW>\n</DATA>\n'

    assert exported_data == expected_xml

def test_end_to_end(tmp_path):
    """
    Test the end-to-end functionality by creating a CSV file, exporting, and checking the resulting XML file.
    """
    csv_file = tmp_path / "test_input.csv"
    xml_file = tmp_path / "test_output.xml"

    with open(csv_file, 'w') as f:
        f.write('Name,Age,Location\nJohn,25,New York\nJane,30,San Francisco\n')

    CSVToXML(str(csv_file), str(xml_file)).export()

    assert xml_file.is_file()

    with open(xml_file, 'r') as f:
        exported_data = f.read()

    expected_xml = '<DATA>\n <ROW>\n    <Name>John</Name>\n    <Age>25</Age>\n    <Location>New York</Location>\n </ROW>\n <ROW>\n    <Name>Jane</Name>\n    <Age>30</Age>\n    <Location>San Francisco</Location>\n </ROW>\n</DATA>\n'

    assert exported_data == expected_xml
