import pandas as pd


def test_no_missing_values():
    flag = False

    df = pd.read_csv('data/cleaned_dataset.csv')

    if (df.isnull().sum().sum() == 0
       and df[df['cleaned'] == ""].sum().sum() == 0):
        flag = True

    assert flag, "Dataset contains missing values"


if __name__ == '__main__':
    test_no_missing_values()
    print("All data quality tests passed!")
