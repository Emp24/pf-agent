from typing import Literal

from pydantic import BaseModel, Field


class Finding(BaseModel):
    file: str = Field(
        min_length=1, description="Name of the file where the issue happens"
    )
    line: int = Field(ge=1, description="Line number of where the issue happened")
    issue_description: str = Field(
        min_length=1, description="Description of the issue, can contain code snippets"
    )
    suggested_fix: str | None = Field(
        description="Suggested fix for the issue, can contain code snippets",
        default=None,
    )
    severity: Literal["High", "Medium", "Low"] = Field(
        description="Severity of the issue,"
        "can only use one of the types inside the literal"
    )
