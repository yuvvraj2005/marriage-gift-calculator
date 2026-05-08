from questionnaire import collect_profile
from gemini_engine import analyze_profile
from utils import format_inr

def main():
    profile = collect_profile()
    print("\nAnalyzing with Gemini...\n")
    result = analyze_profile(profile)

    print("=" * 70)
    print("SHAADI MARKET INDEX REPORT (SATIRICAL)")
    print("=" * 70)
    print(f"Name                : {profile.name}")
    print(f"Profession          : {profile.profession}")
    print(f"Annual Income       : {format_inr(profile.annual_income)}")
    print("-" * 70)
    print(f"Predicted Estimate  : {format_inr(result.estimate_inr)}")
    print(f"Category            : {result.category}")
    print(f"Compatibility Score : {result.compatibility_score:.1f}/100")
    print(f"Prestige Score      : {result.prestige_score:.1f}/100")
    print(f"Tradition Score     : {result.tradition_score:.1f}/100")
    print("-" * 70)
    print("Explanation:")
    print(result.explanation)
    print("-" * 70)
    print("Reality Check:")
    print(result.reality_check)
    print("=" * 70)

if __name__ == "__main__":
    main()
