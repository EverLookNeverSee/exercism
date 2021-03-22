def two_fer(name="") -> str:
    if name == "":
        return "One for you, one for me."
    else:
        return f"One for {name}, one for me."
