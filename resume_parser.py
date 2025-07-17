import language_tool_python

def check_grammar(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(text)
    issues = []

    for match in matches:
        issues.append({
            "message": match.message,
            "error": match.context,
            "suggestion": match.replacements,
            "rule": match.ruleId
        })

    return issues
