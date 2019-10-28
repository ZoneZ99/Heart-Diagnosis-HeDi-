def num_or_str(entity):
    try:
        return int(entity)
    except ValueError:
        try:
            return float(entity)
        except ValueError:
            return str(entity).strip()


def parse_csv(csv, delimiter=','):
    lines = [
        line for line in csv.splitlines()
        if line.strip()
    ]
    return [
        list(
            map(
                num_or_str, line.split(delimiter)
            )
        )
        for line in lines
    ]

