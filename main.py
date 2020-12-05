#!/usr/bin/env python3
import csv
import sys

db_file_path = r'./writing_log.csv'
global csv_data

with open(db_file_path, 'r', newline='') as f:
    reader = csv.DictReader(f, delimiter=',', quotechar='"')
    csv_data = [i for i in reader]
        


class blog_bot():
    def __init__(self, name):
        self.name = name
        global csv_data
        for i in csv_data:
            if i['name'] == self.name:
                return

        print("csv_data is broken.")
        sys.exit(1)


    def get_number_of_writing(self):
        global csv_data
        for i in csv_data:
            if i['name'] == self.name:
                return int(i['count'])

    def send_dm(self, data):
        global csv_data
        pass

    def rewrite_number_of_writing(self, num):
        global csv_data
        for i in csv_data:
            if i['name'] == self.name:
                i['count'] = num
                break
        
        with open(db_file_path, 'w', newline='') as f:
            fieldnames = ["name", "count"]
            writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=',', quotechar="")
            writer.writeheader()
            writer.writerows(csv_data)
    

def get_members():
    # return as tuple
    return ('hayao', 'yamad', 't-mart', 'sunset')


def main():
    blog_instances = {}
    members = get_members()
    for i in members:
        blog_instances[i] = blog_bot(i)

    print("Ready to instances.")
    
    

if __name__ == '__main__':
    main()