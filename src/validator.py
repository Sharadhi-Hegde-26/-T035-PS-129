def validate_required_columns(data, required_columns):

    missing_columns = []

    for column in required_columns:

        if column not in data.columns:
            missing_columns.append(column)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    return True