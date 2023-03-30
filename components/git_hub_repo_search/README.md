
# GitHubRepoSearch

Search GitHub repositories using the GitHub API for the given search query. Must provide an API key for authentication.


## Initial generation prompt
description: 'Search GitHub repositories using the GitHub API for the given search

  query. Must provide an API key for authentication.

  Inputs: {query: str, api_key: str}

  Outputs: {repos_data: List[Dict]}

  '
name: GitHubRepoSearch


## Transformer breakdown
- Validate and process the input query and API key
- Call the GitHub API with the provided API key and the search query
- Parse and extract repository data from the API response
- Return the list of repositories as output

## Parameters
[]

        