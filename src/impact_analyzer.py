import random

def analyze_impact(report_text):
    """
    Simulates AI analysis of a social impact report.
    In a real scenario, this would use an LLM or BERT-based sentiment/entity analysis.
    """
    impact_keywords = {
        'education': 0.8,
        'sustainability': 0.9,
        'healthcare': 0.85,
        'jobs': 0.7,
        'equality': 0.95
    }
    
    score = 0
    words = report_text.lower().split()
    found_keywords = []
    
    for word, weight in impact_keywords.items():
        if word in words:
            score += weight
            found_keywords.append(word)
            
    normalized_score = min(10.0, (score / (len(words) / 100)) * 10) if words else 0
    
    return {
        "impact_score": round(normalized_score, 2),
        "key_impact_areas": found_keywords,
        "recommendation": "Maintain high focus on " + (found_keywords[0] if found_keywords else "core mission")
    }

if __name__ == "__main__":
    sample_report = "Our initiative on education and sustainability has created 500 jobs and improved equality in rural areas."
    result = analyze_impact(sample_report)
    print(f"Impact Analysis Result: {result}")
