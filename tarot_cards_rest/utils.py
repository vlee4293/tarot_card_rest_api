import re


def snake_slugify(s):
    slug = re.sub(r"(?<=[a-z])(?=[A-Z])|[^a-zA-Z]", " ", s).strip().replace(" ", "_")
    return "".join(slug.lower())
