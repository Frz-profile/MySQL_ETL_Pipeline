def createCSV():
    # Step 1 Importing pandas
    import pandas as pd

    # Step 2 Prepare your data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [30, 25, 35],
        'Country': ['USA', 'UK', 'Canada']
    }

    # Step 3 Create a DataFrame using DataFrame function
    df = pd.DataFrame(data)

    # Step 4 Specify the file path to save data
    csv_file_path = 'data.csv' #Choose your file path -----------------------------------

    # Step 5 Write the DataFrame to a CSV file using to_csv() function where file path is passed
    df.to_csv(csv_file_path, index=False)

    print(f'CSV file &quot;{csv_file_path}&quot; has been created successfully.')

#Run function
createCSV()