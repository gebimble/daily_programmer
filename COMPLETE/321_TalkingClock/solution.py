#! /usr/bin/env python

import re


def talking_clock(time):

    h, m = map(int, time.split(':'))

    gt12, h = divmod(h, 12)

    meridian = ['am', 'pm'][gt12]

    tens_and_teens = ['', 'one', 'two', 'three', 'four', 'five', 'six',
                      'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
                      'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventee',
                      'eighteen', 'nineteen']

    twenty_plus = ['twenty', 'thirty', 'fourty', 'fifty']

    t, o = divmod(m, 10)

    if t == 0:
        if o == 0:
            minutes = ''
        else:
            minutes = ' '.join(['oh', tens_and_teens[o]])

    if t == 1:
        minutes = tens_and_teens[o]

    if t >= 2:
        if o != 0:
            minutes = ' '.join([twenty_plus[t-2], tens_and_teens[o]])
        else:
            minutes = twenty_plus[t-2]

    if h == 0:
        hours = 'twelve'
    else:
        hours = tens_and_teens[h]

    time = ' '.join(["It's", hours, minutes, meridian])

    time = re.sub(' +', ' ', time)

    print(time)


times = ['00:00', '01:30', '12:05', '14:01', '20:29', '21:00']

for time in times:
    talking_clock(time)
