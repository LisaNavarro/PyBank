import os
import csv

budget_dataCSV = os.path.join('.', 'Desktop', 'budget_data.csv')
# file = 'budget_data.csv'

print(os.getcwd)

 # Open current CSV
with open(budget_dataCSV) as csvFile:

    csvReader = csv.reader(csvFile, delimiter=',')

    # print (csvReader)
        
    # Skip headers

    next(csvReader, None)
    # List of files
    budget_data = ['1']

    #create variables for calculations
    month_counter = 0
    sum_revenue = 0
    sum_revenue_change = 0

    
    
    #budget_data2.csv = os.path.join("PyBank", "budget_data2.csv")
    #budget_data1.csv = os.path.join("PyBank", "budget_data1.csv")


   
    
    # Get data from first line
    line = next(csvReader)
    max_month = line[0]
    min_month = line[0]
    revenue = float(line[1])
    min_revenue = revenue
    max_revenue = revenue
    previous_revenue = revenue
    month_counter = 1
    sum_revenue = float(line[1])
    sum_revenue_change = 0

    # Read one line at a time
    for line in csvReader:

        # Increase counter for number of months in dataset
        month_counter = month_counter + 1

        revenue = float(line[1])

        # Add to sum of revenue for data set
        sum_revenue = sum_revenue + revenue

        # Find change in revenue between this month and last month
        revenue_change = revenue - previous_revenue

        # Add change in revenue to net change in revenue for data set
        sum_revenue_change = sum_revenue_change + revenue_change

        # Determine if change in revenue is a max or min for data set thus far
        if revenue_change > max_revenue:
            max_month = line[0]
            max_revenue = revenue_change

        if revenue_change < min_revenue:
            min_month = line[0]
            min_revenue = revenue_change

        # Set previous revenue 
        previous_revenue = revenue

    # Finish calculations
    average_revenue = sum_revenue/month_counter
    average_revenue_change = sum_revenue_change/(month_counter-1)

    # Round decimal
    sum_revenue = int(sum_revenue)
    average_revenue_change = int(average_revenue_change)
    max_revenue = int(max_revenue)
    min_revenue = int(min_revenue)
    
    # Print analysis
    print(f"Financial Analysis:")
    print("-------------------------------------------------------")
    print(f"Total Months: {month_counter}")
    print(f"Total Revenue: {sum_revenue} USD")
    print(f"Average Revenue Change: {average_revenue_change} USD")
    print(f"Greatest Increase in Revenue: {max_month} {max_revenue} USD")
    print(f"Greatest Decrease in Revenue: {min_month} {min_revenue} USD")
    print("")
    
    # Name white file
    output_file = budget_dataCSV[0:-4]

    write_budget_dataCSV = f"{output_file}_pybank_results.txt"

    # Open write file
    filewriter = open(write_budget_dataCSV, mode = 'w')

    # Print to write file
    
filewriter.close()





