def drpllib(text):
    if text=="}end\n":
        return "end"
    if "out{" in text:
        return "out"
    if "in{" in text:
        return "in"