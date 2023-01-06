import sqlite3


connection = sqlite3.connect('test_db')
cursor = connection.cursor()


#creating a made up list of tuples with date and weight
date_and_weight = [('1/1/22', 190), ('1/2/22', 191), ('1/3/22', 188), ('1/4/22', 185), ('1/5/22', 195),
                   ('1/6/22', 191),('1/7/22', 190),('1/8/22', 186),('1/8/22', 197),('1/10/22', 190),
                   ('1/11/22', 189),('1/12/22', 192),('1/13/22', 194),('1/14/22', 188),('1/15/22', 184)]

#create sqlite table to store the data
cursor.execute('''CREATE TABLE IF NOT EXISTS weight_log (
            date STRING,
            weight INT
            )''')

#add data to the table all at once
cursor.executemany("INSERT INTO weight_log VALUES (?,?)", date_and_weight)

#store all the table data in an object and print to make sure everything works
all_data = cursor.execute("SELECT * FROM weight_log").fetchall()
print(all_data)

#find the average weight among the entries
all_weight_vals = cursor.execute("SELECT weight FROM weight_log").fetchall()
total_weight = 0

for weight in all_weight_vals:
    total_weight += weight[0]


print(total_weight / len(all_weight_vals))



connection.commit()
connection.close()
