#! /anaconda3/envs/tobias_fyi/bin/python

# 100DaysofCode - Day 001
# 001_csv_format.py
# convert text fields to title case + format phone numbers

import os
import csv
import re
import time


def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                  lambda mo: mo.group(0)[0].upper() +
                  mo.group(0)[1:].lower(),
                  s)


def phonecase(p):
    return re.search(r'\W*(\d{3})\W*(\d{3})\W*(\d{4})(\D*)(\d*)', p)


paths = {
    'p_root': '/Users/Tobias/Documents/Projects/10_Challenges',
    'c_root': '01_Code',
    'day_1': '001_Python_CSV',
}

os.chdir(os.path.join(paths['p_root'], paths['c_root'], paths['day_1']))

header = ['CusNo', 'Customer', 'First', 'Last', 'Phone', 'Ext', 'Email']

with open('001_before.csv', 'r') as og:
    csv_dict = csv.DictReader(og)

    with open('001_after.csv', 'w') as tg:
        csv_writer = csv.writer(tg, delimiter=',')

        csv_writer.writerow(header)

        for line in csv_dict:
            mo_phone = phonecase(line['Phone'])
            if mo_phone:
                phone = [
                    mo_phone.group(1),
                    mo_phone.group(2),
                    mo_phone.group(3),
                ]

                phone_ext = mo_phone.group(5)

            # pseudo-insert of extension after phone number
            email = line.pop('Email')
            line['Ext'] = phone_ext
            line['Email'] = email

            line['Phone'] = '-'.join(phone)

            csv_writer.writerow((line['CusNo'], titlecase(line['Customer']),
                                 titlecase(line['First']),
                                 titlecase(line['Last']),
                                 line['Phone'], line['Ext'],
                                 line['Email'].lower()))

# to make it feel like something cool is happening...
print('New csv being created...')
time.sleep(1)
print('...complete.')
