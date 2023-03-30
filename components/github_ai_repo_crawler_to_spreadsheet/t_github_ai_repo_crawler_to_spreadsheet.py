
import pytest
from dotenv import load_dotenv
from core.workflows.github_ai_repo_crawler_to_spreadsheet import (
    GithubAiRepoCrawlerToSpreadsheet,
    GithubAiRepoCrawlerToSpreadsheetIn,
    GithubAiRepoCrawlerToSpreadsheetOut,
)

load_dotenv()

# Test cases with mocked input and expected output data
test_data = [
    (
        GithubAiRepoCrawlerToSpreadsheetIn(
            SearchQuery="test query",
            GoogleApiCredentials={"api_key": "test_key"},
        ),
        GithubAiRepoCrawlerToSpreadsheetOut(
            SpreadsheetURL="https://example.com/spreadsheet"
        ),
    ),
]

# Error and edge cases (if applicable)
error_data = [
    (
        GithubAiRepoCrawlerToSpreadsheetIn(
            SearchQuery="",  # Empty search query
            GoogleApiCredentials={"api_key": "test_key"},
        ),
    ),
]


# Use @pytest.mark.parametrize to create multiple test scenarios
@pytest.mark.parametrize("input_data, expected_output", test_data)
def test_github_ai_repo_crawler_to_spreadsheet(
    input_data: GithubAiRepoCrawlerToSpreadsheetIn,
    expected_output: GithubAiRepoCrawlerToSpreadsheetOut,
):
    # Initialize the component
    component = GithubAiRepoCrawlerToSpreadsheet()

    # Call the component's transform() method
    result = component.transform(input_data, callbacks=None)

    # Assert that the output matches the expected output
    assert result == expected_output


# Edge case/error handling tests
@pytest.mark.parametrize("input_data", error_data)
def test_github_ai_repo_crawler_to_spreadsheet_errors(
    input_data: GithubAiRepoCrawlerToSpreadsheetIn,
):
    component = GithubAiRepoCrawlerToSpreadsheet()

    # Call the component's transform() method with invalid data
    with pytest.raises(Exception):  # Replace 'Exception' with the expected specific exception class
        component.transform(input_data, callbacks=None)
