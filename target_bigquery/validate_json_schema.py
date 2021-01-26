# TODO: simplify this ugly solution. Improve recursion and iteration

def validate_field(field_property):

    if 'type' in field_property:

        if field_property['type'] == []:
            raise ValueError(f'JSON schema of property {field_property} has empty type')

    if 'properties' in field_property:

        if field_property['properties'] == {}:
            raise ValueError(f'JSON schema of property {field_property} has empty properties')

    if 'items' in field_property:

        if 'anyOf' in field_property['items']:

            for i in field_property['items']['anyOf']:
                validate_field(i)

    if 'anyOf' in field_property:

        for i in field_property['anyOf']:

            validate_field(i)

    if ("items" in field_property and "properties" in field_property["items"]) or (
            "properties" in field_property) or ("anyOf" in field_property):

        for subfield_name, subfield_property in field_property.get("properties", field_property.get("items", {}).get(
                "properties")).items():

            validate_field(subfield_property)


def validate_schema_completeness(schema):

    for field_name, field_property in schema.get("properties", schema.get("items", {}).get("properties")).items():
        validate_field(field_property)