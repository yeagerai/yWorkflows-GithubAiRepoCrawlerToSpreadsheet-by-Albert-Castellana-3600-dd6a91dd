
import typing
from typing import Optional
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from core.workflows.abstract_workflow import AbstractWorkflow


class GithubAiRepoCrawlerToSpreadsheetIn(BaseModel):
    SearchQuery: str
    GoogleApiCredentials: dict


class GithubAiRepoCrawlerToSpreadsheetOut(BaseModel):
    SpreadsheetURL: str


class GithubAiRepoCrawlerToSpreadsheet(AbstractWorkflow):
    def __init__(self) -> None:
        super().__init__()

    async def transform(
        self, args: GithubAiRepoCrawlerToSpreadsheetIn, callbacks: typing.Any
    ) -> GithubAiRepoCrawlerToSpreadsheetOut:
        results_dict = await super().transform(args=args, callbacks=callbacks)

        SpreadsheetURL = results_dict[list(results_dict.keys())[-1]].SpreadsheetURL

        out = GithubAiRepoCrawlerToSpreadsheetOut(SpreadsheetURL=SpreadsheetURL)
        return out

load_dotenv()
github_ai_repo_crawler_to_spreadsheet_app = FastAPI()


@github_ai_repo_crawler_to_spreadsheet_app.post("/transform/")
async def transform(
    args: GithubAiRepoCrawlerToSpreadsheetIn,
) -> GithubAiRepoCrawlerToSpreadsheetOut:
    github_ai_repo_crawler_to_spreadsheet = GithubAiRepoCrawlerToSpreadsheet()
    return await github_ai_repo_crawler_to_spreadsheet.transform(args, callbacks=None)

