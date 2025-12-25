def apply_template(template: dict, blocks: dict, data: dict):
    result = template.copy()
    for key, fn in blocks.items():
        result[key] = fn(data)
    return result
