from django import template

register = template.Library()


@register.filter
def pluralize_votes(value):
    try:
        vote = int(value)
    except (TypeError, ValueError):
        return ""

    match vote :
        case 0:
            return "(No votes)"
        case 1:
            return f"Postitive Feedback ({value} vote)"
        case _ :
            return f"Postitive Feedback ({value} votes)"


def show_if_exists(value):
    return value or None

# higher-order function processes the empty fields
def fall_back_or_process(value,response,method=str):
    if value is None or str(value).lower() in ("none",""):
        return response
    return method(value)

# Factory function creates proper filter to pass in to higher function
def register_empty_field(response, method=str):
    def filter_func(value):
        return fall_back_or_process(value, response, method)
    return filter_func

# register.filter("empty_owner",register_empty_field("Unknown"))
register.filter("empty_bio",register_empty_field("No bio has submitted"))
register.filter("empty_headline",register_empty_field(""))
register.filter("empty_location",register_empty_field(""))
register.filter("empty_skill",register_empty_field(""))
register.filter("empty_skill_description",register_empty_field(""))