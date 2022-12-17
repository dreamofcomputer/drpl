def drpllib(text):
    if text=="}end\n":
        return "end"
    if text=="!":
        return ""
    if "ifjump" in text:
        return ""
    if "=if{" in text:
        return "=if"
    if "out{" in text:
        return "out"
    if "in{" in text:
        return "in"
    if "jump" in text:
        return "jump"
