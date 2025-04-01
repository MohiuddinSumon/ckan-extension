import ckan.plugins.toolkit as tk
import ckanext.myext.logic.schema as schema


@tk.side_effect_free
def myext_get_sum(context, data_dict):
    tk.check_access(
        "myext_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.myext_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'myext_get_sum': myext_get_sum,
    }
