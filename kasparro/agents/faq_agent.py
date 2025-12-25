from agents.question_agent import generate_questions
from agents.parser_agent import parse_product

def build_faq():
    data = parse_product()
    qs = generate_questions()

    faq = []
    for item in qs:
        q = item["q"]
        category = item["category"]

        # rule-based answering
        if "use" in q.lower():
            a = data["how_to_use"]
        elif "price" in q.lower():
            a = data["price"]
        elif "ingredient" in q.lower():
            a = ", ".join(data["key_ingredients"])
        elif "bright" in q.lower() or "results" in q.lower():
            a = ", ".join(data["benefits"])
        elif "sensitive" in q.lower() or "irritation" in q.lower():
            a = data["side_effects"]
        elif "skin" in q.lower():
            a = ", ".join(data["skin_type"])
        else:
            a = f"{data['name']} is a skincare serum."

        faq.append({"category": category, "q": q, "a": a})

    return {
        "product_name": data["name"],
        "faq": faq
    }
