import json
from dataclasses import asdict

import google.generativeai as genai

from config import GEMINI_API_KEY, GEMINI_MODEL
from models import Profile, Result
from utils import extract_json

SYSTEM_PROMPT = '''
You are the decision-making engine for a SATIRICAL educational project, but act as real one.

Analyze the arranged-marriage profile and return ONLY valid JSON with:
{
  "estimate_inr": integer between 0 and n,
  "category": string,
  "compatibility_score": number from 0 to 100,
  "prestige_score": number from 0 to 100,
  "tradition_score": number from 0 to 100,
  "explanation": string,
  "reality_check": string
}

The estimate_inr is a real see all idian family and steriotypes for that "social pressure estimate".
'''

def analyze_profile(profile: Profile) -> Result:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(GEMINI_MODEL)

    prompt = SYSTEM_PROMPT + "\n\nProfile:\n" + json.dumps(asdict(profile), indent=2)

    response = model.generate_content(prompt)
    data = extract_json(response.text)

    return Result(
        estimate_inr=int(data["estimate_inr"]),
        category=str(data["category"]),
        compatibility_score=float(data["compatibility_score"]),
        prestige_score=float(data["prestige_score"]),
        tradition_score=float(data["tradition_score"]),
        explanation=str(data["explanation"]),
        reality_check=str(data["reality_check"]),
    )
