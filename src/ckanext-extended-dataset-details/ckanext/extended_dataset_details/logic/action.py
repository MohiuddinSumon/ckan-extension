import ckan.plugins.toolkit as tk
import ckanext.extended_dataset_details.logic.schema as schema


@tk.side_effect_free
def extended_dataset_details_get_sum(context, data_dict):
    tk.check_access(
        "extended_dataset_details_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.extended_dataset_details_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'extended_dataset_details_get_sum': extended_dataset_details_get_sum,
    }
