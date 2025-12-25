from agents.parser_agent import parse_product

def generate_questions():
    data = parse_product()

    questions = [
        ("Informational", f"What is {data['name']}?"),
        ("Usage", "How do I use this serum?"),
        ("Safety", "Is it safe for sensitive skin?"),
        ("Purchase", f"What is the price of {data['name']}?"),
        ("Ingredients", "What ingredients does it contain?"),
        ("Benefits", "What results can I expect?"),
        ("Usage", "Can I use it in the morning?"),
        ("Usage", "Can I use it with moisturizer?"),
        ("Safety", "Can teenagers use it?"),
        ("Storage", "How should I store it?"),
        ("Skin Type", f"Is it suitable for {', '.join(data['skin_type'])}?"),
        ("Side Effects", "Does it cause irritation?"),
        ("Comparison", "How is it different from GlowBoost Lite Serum?"),
        ("Purchase", "Is it refundable?"),
        ("Time", "How long until I see results?")
    ]

    return [{"category": c, "q": q} for c, q in questions]
