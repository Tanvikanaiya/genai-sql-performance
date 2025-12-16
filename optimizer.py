def rule_based_analysis(query):
    suggestions = []

    if "select *" in query.lower():
        suggestions.append("Avoid SELECT *. Fetch only required columns.")

    if "where" not in query.lower():
        suggestions.append("Missing WHERE clause may cause full table scans.")

    if "join" in query.lower() and "on" not in query.lower():
        suggestions.append("JOIN without ON condition detected.")

    if "order by" in query.lower():
        suggestions.append("Ensure ORDER BY columns are indexed.")

    return suggestions
