import pytest
import simplejson
import singer

from target_bigquery.schema import build_schema, prioritize_one_data_type_from_multiple_ones_in_anyOf, convert_field_type

from tests.schema_old import build_schema_old

from target_bigquery.simplify_json_schema import simplify
from tests import unittestcore

from tests.rsc.input_json_schemas import *

from tests.rsc.input_json_schemas_invalid import *

from tests.utils import convert_list_of_schema_fielts_to_list_of_lists

from target_bigquery.validate_json_schema import validate_schema_completeness


class TestSchemaValidation(unittestcore.BaseUnitTest):

    def setUp(self):
        super(TestSchemaValidation, self).setUp()


    def test_schema_invalid_JSON(self):
        """
        supply invalid json file
        raises JSONDecodeError
        """
        schema_0_input = schema_nested_2_invalid_JSON

        # if you uncomment this line:
        # schema_0_input = schema_nested_2
        # this will fail the test: Failed: DID NOT RAISE <class 'simplejson.scanner.JSONDecodeError'>
        # because this is a valid schema

        with pytest.raises(simplejson.scanner.JSONDecodeError):
            msg = singer.parse_message(schema_0_input)

    def test_schema_validation(self):

        missing_props_error = "JSON schema .* has empty properties"

        missing_type_error = "JSON schema .* has empty type"

        invalid_schema_list = [{invalild_schema_top_field_empty_props: missing_props_error},
                               {invalild_schema_top_field_empty_type: missing_type_error},
                               {invalid_schema_subfield_empty_props: missing_props_error},
                               {invalid_schema_subfield_empty_type: missing_type_error},
                               {invalid_schema_under_anyOf_empty_props_example_1: missing_props_error},
                               {invalid_schema_under_anyOf_empty_props_example_2: missing_props_error},
                               {invalid_schema_under_anyOf_deep_nested_empty_props: missing_props_error},
                               {invalid_schema_under_anyOf_deep_nested_empty_type: missing_type_error}
                               ]

        for invalid_schema in invalid_schema_list:
            for invalid_schema_name, error_message in invalid_schema.items():

                msg = singer.parse_message(invalid_schema_name)

                with pytest.raises(ValueError, match=error_message):
                    validate_schema_completeness(msg.schema)


