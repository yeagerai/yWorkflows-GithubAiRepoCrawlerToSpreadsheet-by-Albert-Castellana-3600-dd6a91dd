
import os
import requests
from typing import Dict, List, Optional

import yaml
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.abstract_component import AbstractComponent


class GitHubRepoSearchInputDict(BaseModel):
    query: str
    api_key: str


class GitHubRepoSearchOutputDict(BaseModel):
    repos_data: List[Dict]


class GitHubRepoSearch(AbstractComponent):
    def __init__(self) -> None:
        super().__init__()

    def transform(
        self, args: GitHubRepoSearchInputDict
    ) -> GitHubRepoSearchOutputDict:
        print(f"Executing the transform of the {type(self).__name__} component...")

        query = args.query
        api_key = args.api_key
        url = f"https://api.github.com/search/repositories?q={query}"
        headers = {"Authorization": f"token {api_key}"}

        response = requests.get(url, headers=headers).json()

        try:
            repos_data = response["items"]
        except KeyError:
            repos_data = []

        out = GitHubRepoSearchOutputDict(repos_data=repos_data)

        return out


load_dotenv()
gh_repo_search_app = FastAPI()


@gh_repo_search_app.post("/transform/")
async def transform(
    args: GitHubRepoSearchInputDict
) -> GitHubRepoSearchOutputDict:
    gh_repo_search = GitHubRepoSearch()
    return gh_repo_search.transform(args)
