import pandas as pd
import random

data = {
        'Name': ['John', 'Bob', 'Valentyn', 'Karl', 'Marks'],
        'Age': [17, 18, 21, 55, 60],
        'City': ['Los Angeles', 'Miami', 'Kyiv', 'Kyiv', 'Miami'],
    }

def work_with_dict():
    df = pd.DataFrame(data)

    print(df)

def add_delete_new_column_test():
    columns = ['Name', 'Age', 'City']
    df = pd.DataFrame(data, columns=columns)
    new_row = {'Name': 'Alice', 'Age': 40, 'City': 'Odesa'}
    df.loc[len(df)] = new_row

    print(df)

    print()
    print("Після видалення")
    new_df = df.drop(columns=['City',])
    new_df = new_df.drop([0, 1])
    print(new_df)

    print()
    print("Після зміни")
    new_df.at[2, 'Age'] = 100

    print(new_df)

def test_filtration():
    df = pd.DataFrame(data)

    print("Стартовий df")
    print(df)
    filter_by_age = df[(df['Age'] > 25) & (df.Name.str.contains('a'))]
    print()
    print("Фільтр по віку df")
    print(filter_by_age)

    index_change_df = df.set_index('Name')
    print()
    print("зміна індексування df")
    print(index_change_df)

    row_valentyn = index_change_df.loc['Valentyn']
    print()
    print("знаходження за новим індексом")
    print(row_valentyn)

def test_smth():
    df = pd.DataFrame(data)
    avg_age = df['Age'].mean()
    print(f"Avg age {avg_age}")

    test_ser = pd.Series([random.random() for _ in range(1000)])
    print(test_ser.max())
    print(test_ser.min())
    print(test_ser.mean())
    print(test_ser)
    print(test_ser.loc[3])

    print(test_ser[test_ser > 0.5])
    # test_ser.to_csv('testcsv.csv')

# work_with_dict()
# add_delete_new_column_test()
# test_filtration()
test_smth()
