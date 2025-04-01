import ckan.plugins.toolkit as tk


def extended_dataset_details_required(value):
    if not value or value is tk.missing:
        raise tk.Invalid(tk._("Required"))
    return value


def get_validators():
    return {
        "extended_dataset_details_required": extended_dataset_details_required,
    }
