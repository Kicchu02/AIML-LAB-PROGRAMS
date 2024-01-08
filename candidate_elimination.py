import csv

with open("testdata.csv") as f:
    # open csv file using csv.reader()
    csv_file = csv.reader(f)
    # convert into 2d array and put it as data 
    data = list(csv_file)

    # specific hypothesis is the 1st line of data
    specific = data[1][:-1]
    # generic hypothesis is 2d array of '?'
    general = [['?' for i in range(len(specific))] for j in range(len(specific))]

    # iterate the every line of data
    for i in data:
        # if the last column is yes
        if i[-1] == "Yes":
            # iterate through every attribute of the example
            for j in range(len(specific)):
                # if data is mismatched with specefic hypothesis, then put both specific and generic to '?'
                if i[j] != specific[j]:
                    specific[j] = "?"
                    general[j][j] = "?"

        # if the last column is no
        else:
            # iterate through every attribute of the example
            for j in range(len(specific)):
                # if attr is mismatched with specific hypothesis, then put generic as specific
                if i[j] != specific[j]:
                    general[j][j] = specific[j]
                # else put generic to '?'
                else:
                    general[j][j] = "?"

        # print each step
        print("\nStep " + str(data.index(i)+1) + " of Candidate Elimination Algorithm")
        print('specific:', specific)
        print('general:', general)

    gh = [] # gh = general Hypothesis
    for i in general:
        # if a generic hypothesis consists of only '?', then dont append, else append to gh
        for j in i:
            if j != '?':
                gh.append(i)
                break
            
    # print the final version space
    print("\nFinal Specific hypothesis:\n", specific)
    print("\nFinal General hypothesis:\n", gh)