from api import get_count_of_pages, get_dict_of_course
import pandas as pd

if __name__ == '__main__':

    # data
    data = []

    # get the count of pages
    count_of_pages = get_count_of_pages()
    print(count_of_pages)

    # get detail
    for i in range(count_of_pages + 1):
        get_dict_of_course(i, data)

    # Store to Excel
    df = pd.DataFrame(data)
    with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    print(data)
