from models import Profile


def ask_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError
            if max_val is not None and value > max_val:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Try again.")


def ask_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Try again.")


def collect_profile() -> Profile:
    print("=" * 70)
    print("SHAADI MARKET INDEX")
    print("=" * 70)
    print("This is a fictional educational tool.")
    print()

    return Profile(
        # Basic Details
        name=input("Full Name: "),
        gender=input("Gender: "),
        religion=input("Religion: "),
        caste=input("Caste/Community: "),
        age=ask_int("Age: ", 18, 80),
        education=input("Highest Education: "),
        profession=input("Profession: "),
        annual_income=ask_float("Annual Income in INR: "),
        work_location=input("Work Location (India/USA/Europe/etc.): "),

        # Assets & Family Background
        family_properties=ask_int("Number of Family Properties: ", 0, 100),
        family_business=input("Family Business (Yes/No): "),
        owns_house=input("Own House (Yes/No): "),
        owns_car=input("Own Car (Yes/No): "),
        loyalty_importance=ask_int("Importance of Loyalty (1-5): ", 1, 5),
        joint_family_preference=input("Joint Family Preference (Yes/No/Flexible): "),
        prior_relationships=input(
            "Prior Relationships (None/Few/Multiple/Prefer not to say): "
        ),

        # Career & Future Potential
        current_status=input("Current Status (Student/Job/Business): "),
        expected_income_5_years=ask_float(
            "Expected Annual Income After 5 Years (INR): "
        ),
        government_job=input("Government Job (Yes/No): "),
        abroad_settlement_interest=input(
            "Interested in Settling Abroad (Yes/No/Maybe): "
        ),
        entrepreneurship_interest=input(
            "Interested in Entrepreneurship (Yes/No/Already Running): "
        ),

        # Parents & Family
        father_occupation=input("Father's Occupation: "),
        mother_occupation=input("Mother's Occupation: "),
        family_annual_income=ask_float("Total Family Annual Income (INR): "),
        number_of_siblings=ask_int("Number of Siblings: ", 0, 20),
        siblings_married=ask_int("Number of Married Siblings: ", 0, 20),
        family_reputation=input("Family Reputation (Excellent/Good/Average): "),
        political_influence=input(
            "Political Influence (None/Local/Strong): "
        ),

        # Lifestyle
        height_cm=ask_int("Height (cm): ", 100, 250),
        weight_kg=ask_int("Weight (kg): ", 30, 200),
        fitness_level=input("Fitness Level (Low/Moderate/High): "),
        drinking=input("Drinking (Never/Occasionally/Frequently): "),
        smoking=input("Smoking (Never/Occasionally/Frequently): "),
        diet=input("Diet (Vegetarian/Eggetarian/Non-Vegetarian): "),
        travel_frequency=input(
            "Travel Frequency (Rarely/Sometimes/Frequently): "
        ),
        social_media_usage=input(
            "Social Media Usage (Low/Moderate/High): "
        ),

        # Personality & Psychology
        emotional_maturity=ask_int("Emotional Maturity (1-10): ", 1, 10),
        anger_management=ask_int("Anger Management (1-10): ", 1, 10),
        communication_skills=ask_int("Communication Skills (1-10): ", 1, 10),
        financial_responsibility=ask_int(
            "Financial Responsibility (1-10): ", 1, 10
        ),
        openness_to_counseling=ask_int(
            "Openness to Counseling (1-10): ", 1, 10
        ),
        conflict_style=input(
            "Conflict Style (Calm/Avoidant/Aggressive): "
        ),

        # Marriage Expectations
        preferred_spouse_working=input(
            "Preferred Spouse Working (Yes/No/Flexible): "
        ),
        preferred_spouse_income=ask_float(
            "Preferred Spouse Income (INR, 0 if no preference): "
        ),
        children_preference=input(
            "Children Preference (Yes/No/Maybe): "
        ),
        wedding_budget_expectation=ask_float(
            "Expected Wedding Budget (INR): "
        ),
        joint_finances_preference=input(
            "Joint Finances Preference (Separate/Joint/Hybrid): "
        ),
        house_after_marriage=input(
            "Living Arrangement After Marriage "
            "(Own House/Rented/With Parents/Separate): "
        ),

        # Traditional Factors
        horoscope_importance=input(
            "Horoscope Importance (High/Medium/Low/None): "
        ),
        manglik_status=input(
            "Manglik Status (Yes/No/Don't Know): "
        ),
        caste_importance=input(
            "Caste Importance (High/Medium/Low/None): "
        ),
        religious_practice_level=input(
            "Religious Practice Level (High/Medium/Low): "
        ),
    )