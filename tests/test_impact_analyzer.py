from src.impact_analyzer import analyze_impact

def test_analyze_impact_score():
    report = "education sustainability jobs"
    result = analyze_impact(report)
    assert result['impact_score'] > 0
    assert 'education' in result['key_impact_areas']

def test_analyze_impact_empty():
    result = analyze_impact("")
    assert result['impact_score'] == 0
