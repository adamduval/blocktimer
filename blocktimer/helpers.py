from ast import Try


def parse_time_block(text):
    """
    Given a time block "Name Time(M)Time(s)" return parsed block {name: 'name', time: 'time(s)'}

    >>> parse_time_block('Run 1m')
    {'name': 'run', 'time': 60}

    >>> parse_time_block('Run 30s')
    {'name': 'run', 'time': 30}

    >>> parse_time_block('Run 1m30s')
    {'name': 'run', 'time': 90}

    """
    units =['m', 's']

    split = text.lower().split()

    # determine if time was entered in minutes or seconds and process
    split_time = split.pop(-1)
    if all(x in split_time for x in units):
        split_m = split_time.split('m')
        time_ms = (int(split_m[0])) * 60
        time_s = int(split_m[1].split('s')[0])
        time = time_ms + time_s
    elif 'm' in split_time:
        time = split_time.strip('m')
        # convert minutes to seconds
        time = int(time) * 60
    else:
        time = int(split_time.strip('s'))
    # concat text
    name = ' '.join(split)

    if not name:
        print('no name') # todo

    return {'name': name, 'time': time}


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
