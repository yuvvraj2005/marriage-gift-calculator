from dataclasses import dataclass


@dataclass
class Profile:
    # Basic Details
    name: str
    gender: str
    religion: str
    caste: str
    age: int
    education: str
    profession: str
    annual_income: float
    work_location: str

    # Assets & Family Background
    family_properties: int
    family_business: str
    owns_house: str
    owns_car: str
    loyalty_importance: int
    joint_family_preference: str
    prior_relationships: str

    # Career & Future Potential
    current_status: str
    expected_income_5_years: float
    government_job: str
    abroad_settlement_interest: str
    entrepreneurship_interest: str

    # Parents & Family
    father_occupation: str
    mother_occupation: str
    family_annual_income: float
    number_of_siblings: int
    siblings_married: int
    family_reputation: str
    political_influence: str

    # Lifestyle
    height_cm: int
    weight_kg: int
    fitness_level: str
    drinking: str
    smoking: str
    diet: str
    travel_frequency: str
    social_media_usage: str

    # Personality & Psychology
    emotional_maturity: int
    anger_management: int
    communication_skills: int
    financial_responsibility: int
    openness_to_counseling: int
    conflict_style: str

    # Marriage Expectations
    preferred_spouse_working: str
    preferred_spouse_income: float
    children_preference: str
    wedding_budget_expectation: float
    joint_finances_preference: str
    house_after_marriage: str

    # Traditional Factors
    horoscope_importance: str
    manglik_status: str
    caste_importance: str
    religious_practice_level: str


@dataclass
class Result:
    estimate_inr: int
    category: str
    compatibility_score: float
    prestige_score: float
    tradition_score: float
    explanation: str
    reality_check: str