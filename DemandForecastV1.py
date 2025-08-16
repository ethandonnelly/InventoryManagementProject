# In this, I worked on the data handling needed for my forecasting algorithm to work


import csv
import datetime
import random
import matplotlib.pyplot as plt

def create_test_data(starting_year, starting_month, starting_day, duration, file_name):

    start = datetime.date(starting_year, starting_month, starting_day)

    with open(file_name, 'w') as new_file:
        writer = csv.writer(new_file)
        for row in range(duration):
            sales = random.randint(10, 250)
            date = start + datetime.timedelta(days=1)

            could do a while loop here

def read_csv(file_name):
    with open(f'{file_name}', 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            print(row)


def visualise_csv(file_name):
    sales = []
    dates = []

    with open(f'{file_name}', 'r') as csv_file:
        reader = csv.reader(csv_file)

        for row in reader:
            sales.append
