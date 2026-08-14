def build_menu_message(title, menu_message, *args):
    message = f"""
{title}
{"=" * 20}
{menu_message}
{"=" * 20}
"""

    for text in args:
        message += text

    return message
