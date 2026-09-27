from pydantic import BaseModel, Field, field_validator


class ResumeEvaluation(BaseModel):
    match_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Candidate-job match score from 0 to 100"
    )

    top_strengths: list[str] = Field(
        ...,
        description="Strengths explicitly supported by the resume"
    )

    missing_skills: list[str] = Field(
        ...,
        description="Required job skills not demonstrated in the resume"
    )

    summary: str = Field(
        ...,
        description="Concise two-line evaluation summary"
    )

    @field_validator("summary")
    @classmethod
    def validate_summary(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Summary cannot be empty")

        lines = [line for line in value.splitlines() if line.strip()]

        if len(lines) != 2:
            raise ValueError("Summary must contain exactly two lines")

        return value