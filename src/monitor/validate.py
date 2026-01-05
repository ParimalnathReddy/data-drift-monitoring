import great_expectations as ge
import pandas as pd

CRITICAL_COLS = ["trip_distance", "fare_amount", "passenger_count", "payment_type"]

def run_ge_checks(df: pd.DataFrame) -> dict:
    context = ge.get_context()
    
    # Setup ephemeral datasource
    datasource_name = "runtime_pandas_datasource"
    # Attempt to clean up previous datasource if it exists
    # The list_datasources method returns a list of configs or dicts.
    # We can try to delete just in case.
    try:
        context.delete_datasource(datasource_name)
    except:
        pass
        
    # Use data_sources (Fluent API manager)
    datasource = context.data_sources.add_pandas(datasource_name)
    asset = datasource.add_dataframe_asset("runtime_dataframe")
    
    suite_name = "runtime_suite"
    suite = ge.ExpectationSuite(name=suite_name)
    context.suites.add_or_update(suite)
    
    batch_request = asset.build_batch_request(options={"dataframe": df})
    validator = context.get_validator(batch_request=batch_request, expectation_suite_name=suite_name)
    
    results = []
    # Column existence
    for c in CRITICAL_COLS:
        results.append(validator.expect_column_to_exist(c).success)

    # Null checks
    results.append(validator.expect_column_values_to_not_be_null("trip_distance").success)
    results.append(validator.expect_column_values_to_not_be_null("fare_amount").success)

    # Range checks
    results.append(validator.expect_column_values_to_be_between("trip_distance", 0, 200).success)
    results.append(validator.expect_column_values_to_be_between("passenger_count", 0, 8).success)

    # Fare sanity (allow rare edge cases, but track)
    results.append(validator.expect_column_values_to_be_between("fare_amount", -5, 500).success)

    return {
        "ge_pass": all(results),
        "ge_failed_count": results.count(False),
    }
