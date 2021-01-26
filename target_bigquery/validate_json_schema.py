# TODO: simplify this ugly solution. Improve recursion and iteration

import singer

from tests.rsc.input_json_schemas_invalid import *

schema_0_input = invalid_schema_under_anyOf_deep_nested_empty_type

msg = singer.parse_message(schema_0_input)


def validate_field(field_property):
    if 'type' in field_property:

        if field_property['type'] == []:
            raise ValueError(f'JSON schema of property {field_property} has empty type')

    if 'properties' in field_property:

        if field_property['properties'] == {}:
            raise ValueError(f'JSON schema of property {field_property} has empty properties')

    if 'items' in field_property:

        if 'anyOf' in field_property['items']:

            print('anyOf')

            for i in field_property['items']['anyOf']:
                validate_field(i)

                if 'type' in i:

                    if i['type'] == []:
                        raise ValueError(f'JSON schema of list item {field_property} has empty type')

                    if 'properties' in i:

                        if i['properties'] == {}:
                            raise ValueError(f'JSON schema of list item  {field_property} has empty properties')

    if 'anyOf' in field_property:

        for i in field_property['anyOf']:

            validate_field(i)

            if 'type' in i:

                if i['type'] == []:
                    raise ValueError(f'JSON schema of list item {field_property} has empty type')

            if 'properties' in i:

                if i['properties'] == {}:
                    raise ValueError(f'JSON schema of list item  {field_property} has empty properties')

    if not ("items" in field_property and "properties" in field_property["items"]) and not (
            "properties" in field_property) and not ("anyOf" in field_property):

        pass

    elif ("items" in field_property and "properties" in field_property["items"]) or (
            "properties" in field_property) or ("anyOf" in field_property):

        for subfield_name, subfield_property in field_property.get("properties", field_property.get("items", {}).get(
                "properties")).items():

            print('subfield', subfield_name, subfield_property, '\n')

            validate_field(subfield_property)

            if 'anyOf' in subfield_property:

                for i in subfield_property['anyOf']:

                    validate_field(i)

                    if 'type' in i:

                        if i['type'] == []:
                            raise ValueError(f'JSON schema of list item {field_property} has empty type')

                    if 'properties' in i:

                        if i['properties'] == {}:
                            raise ValueError(f'JSON schema of list item  {field_property} has empty properties')


def validate_schema_completeness(schema):

    for field_name, field_property in schema.get("properties", schema.get("items", {}).get("properties")).items():
        validate_field(field_property)