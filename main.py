import argparse
import datetime
import sys

MIN_YEAR = 2000
MAX_YEAR = 2999


def main(value):
    """
    :param value: string containing 3 integers separated by "/"
        there are no extra spaces around the "/"
        years may be truncated to two digits and may in that case also omit the leading 0
        months and days may be zero-padded
        year, when given with four digits, is between 2000 and 2999
    :return: string with the earliest legal date possible given the above constraints,
        formatted as year-month-day, where year has four digits, and
        month and day have two digits each (zero padding)
        If there is no legal date then outputs a single line with
        the original string followed by the words "is illegal".
    """

    inputs = value.split('/')
    if not len(inputs) == 3:
        return '"{}" is illegal'.format(value)

    timestamp = None
    formats = ['{0:0>3}/{1}/{2}', '{1:0>3}/{2}/{0}', '{2:0>3}/{1}/{0}', '{0:0>3}/{2}/{1}', '{1:0>3}/{0}/{2}']
    for _format in formats:
        _str = '{0:2>4}/{1}/{2}'.format(*_format.format(*inputs).split('/'))
        try:
            _date = datetime.datetime.strptime(_str, '%Y/%m/%d')
            if _date.year < MIN_YEAR or _date.year > MAX_YEAR:
                continue

            if not timestamp or timestamp and timestamp > _date:
                timestamp = _date
        except ValueError:
            pass

    if timestamp:
        return datetime.datetime.strftime(timestamp, '%Y-%m-%d')
    return '"{}" is illegal'.format(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Parse date in the "A/B/C" format.')
    parser.add_argument('value', type=str, help='date string in the "A/B/C" format.')
    args = parser.parse_args()
    if args.value:
        sys.stdout.write('{}\n'.format(
            main(args.value)
        ))
