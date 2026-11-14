from src.input_reader import read_csv_file


def test_read_csv_file(tmp_path):

    # Create a temporary CSV file
    file = tmp_path / "demo.csv"

    file.write_text(
        "team_id,team_name\nT01,Alpha\nT02,Beta"
    )

    # Read the CSV
    data = read_csv_file(file)

    # Check the results
    assert len(data) == 2
    assert "team_id" in data.columns
    assert "team_name" in data.columns


def test_missing_file():

    try:
        read_csv_file("nonexistent.csv")
        assert False

    except FileNotFoundError:
        assert True