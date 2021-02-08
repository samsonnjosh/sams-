def convert(from_unit_type, to_unit_type, value):
    from_type_units = types[from_unit_type]
    to_type_units = types[to_unit_type]

    new_value = value * (from_type_units / to_type_units)

    return str(new_value) + to_unit_type