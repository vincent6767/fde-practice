from enum import StrEnum
from pydantic import BaseModel, Field, ConfigDict
from fastapi import FastAPI

class Severity(StrEnum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class IncidentRequest(BaseModel):
    description: str = Field(..., min_length=1, description="A brief description of the incident.")

    model_config = ConfigDict(str_strip_whitespace=True)

class IncidentAnalysisResponse(BaseModel):
    severity: Severity = Field(..., description="The severity level of the incident.")
    summary: str = Field(..., description="A brief summary of the incident.")
    possible_causes: list[str] = Field(..., description="A list of possible causes for the incident.")
    recommended_next_steps: list[str] = Field(..., description="Recommended next steps to resolve the incident.")

def analyze_incident(description: str) -> dict:  
    return {
        "severity": "High",
        "summary": "The incident involves a critical system failure affecting multiple users.",
        "possible_causes": [
            "Hardware failure",
            "Software bug",
            "Network issue"
        ],
        "recommended_next_steps": [
            "Restart the affected systems",]
    }

app = FastAPI()

@app.post("/analyze-incident", response_model=IncidentAnalysisResponse)
def analyze_incident_endpoint(incident_request: IncidentRequest):
    description = incident_request.description
    
    result = analyze_incident(description)
   
    return IncidentAnalysisResponse(**result)