from dataclasses import dataclass
from typing import Optional, List
from .constants.enums import (
    TextType,
    CodeLanguage
    )


@dataclass()
class ProblemStatementDto:
	question_id: int
	short_title: str
	content_type: TextType
	content: str
















