import ckan.plugins.toolkit as tk


@tk.auth_allow_anonymous_access
def extended_dataset_details_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "extended_dataset_details_get_sum": extended_dataset_details_get_sum,
    }
