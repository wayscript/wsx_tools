# Here are all the functions to make responses easier to work with
# Edit to whatever format that is needed for your specific project

def clean_response(response):
    return


def clean_columns(response):
    columns = []
    for i in response:
        column = i[0]
        i = str(column)
        columns.append(i)
    return columns
