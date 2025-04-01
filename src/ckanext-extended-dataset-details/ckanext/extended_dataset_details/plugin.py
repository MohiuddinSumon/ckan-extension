# encoding: utf-8
from __future__ import annotations

import logging
import ckan.plugins as p
import ckan.plugins.toolkit as tk
from ckan.types import Schema
from typing import Any, cast

# Set up logging
log = logging.getLogger(__name__)

class ExtendedDatasetDetailsPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)
    p.implements(p.ITemplateHelpers)

    def update_config(self, config: Any) -> None:
        log.info("ExtendedDatasetDetailsPlugin: update_config() called")
        # Add our templates and public directories to CKAN's configuration
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')

    def get_helpers(self) -> dict[str, Any]:
        log.info("ExtendedDatasetDetailsPlugin: get_helpers() called")
        # Expose a helper function to fetch the country code vocabulary
        return {'country_codes': country_codes}

    # -- IDatasetForm methods --
    def is_fallback(self) -> bool:
        log.info("ExtendedDatasetDetailsPlugin: is_fallback() called")
        # Register as the default dataset form handler.
        return True

    def package_types(self) -> list[str]:
        log.info("ExtendedDatasetDetailsPlugin: package_types() called")
        # This plugin is not specific to any package type.
        return []

    def _modify_package_schema(self, schema: Schema) -> Schema:
        log.info("ExtendedDatasetDetailsPlugin: _modify_package_schema() called")
        # Add custom_text field: stored as an extra
        schema.update({
            'custom_text': [
                tk.get_validator('ignore_missing'),
                tk.get_converter('convert_to_extras')
            ]
        })
        # Add country_code field: stored as a tag (using a vocabulary)
        schema.update({
            'country_code': [
                tk.get_validator('ignore_missing'),
                cast("Any", tk.get_converter('convert_to_tags'))('country_codes'),
            ]
        })
        # For resources: add a custom resource field
        if 'resources' in schema:
            cast(Schema, schema['resources']).update({
                'custom_resource_text': [
                    tk.get_validator('ignore_missing')
                ]
            })
        return schema

    def create_package_schema(self) -> Schema:
        log.info("ExtendedDatasetDetailsPlugin: create_package_schema() called")
        schema: Schema = super(ExtendedDatasetDetailsPlugin, self).create_package_schema()
        return self._modify_package_schema(schema)

    def update_package_schema(self) -> Schema:
        log.info("ExtendedDatasetDetailsPlugin: update_package_schema() called")
        schema: Schema = super(ExtendedDatasetDetailsPlugin, self).update_package_schema()
        return self._modify_package_schema(schema)

    def show_package_schema(self) -> Schema:
        log.info("ExtendedDatasetDetailsPlugin: show_package_schema() called")
        schema: Schema = super(ExtendedDatasetDetailsPlugin, self).show_package_schema()
        # For showing, convert the extra back to the field values.
        schema.update({
            'custom_text': [
                tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')
            ]
        })
        schema.update({
            'country_code': [
                cast("Any", tk.get_converter('convert_from_tags'))('country_codes'),
                tk.get_validator('ignore_missing')
            ]
        })
        return schema

# -- Helper functions for tag vocabulary --
def create_country_codes() -> None:
    log.info("ExtendedDatasetDetailsPlugin: create_country_codes() called")
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'country_codes'}
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'country_codes'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in (u'uk', u'ie', u'de', u'fr', u'es'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def country_codes() -> list[str]:
    log.info("ExtendedDatasetDetailsPlugin: country_codes() helper called")
    create_country_codes()
    try:
        tag_list = tk.get_action('tag_list')
        return tag_list({}, {'vocabulary_id': 'country_codes'})
    except tk.ObjectNotFound:
        return []
