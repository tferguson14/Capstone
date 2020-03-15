from Code import Preprocessing as preprocessing
from Code import Models as model


def main():
    file1 = "Traffic_Crashes_-_Crashes.csv"
    file2 = "Traffic_Crashes_-_People.csv"
    file3 = "Traffic_Crashes_-_Vehicles.csv"
    drop_cols = "drop_cols.csv"
    path = 'C:/Users/Cristina/Documents/GWU/Capstone/EDA_accidents_pycharm2.html'

    crash = preprocessing.ReadData(file1,file2, file3, drop_cols=drop_cols)

    """Read datasets and Join"""
    df_crashes= crash.read_dataset()
    """Download dataset after join"""
    crash.download_preprocessing(df_crashes)
    print("Download is done!")

    """Read complete dataset"""
    df_crashes = crash.read_complete_data()

    """Create EDA using pandas-profiling and download"""
    """it is commented because it takes a long time to run- uncomment if needed"""
    # profile = crash.describe_data(df_crashes)
    # profile.to_file(path)

    """Missing values and encoding - to be able to work with different algorithms"""
    num_features, cat_features = crash.identify_features(df=df_crashes)
    col_transform, df = crash.encode_imputation(num_features=num_features,cat_features=cat_features,df=df_crashes)



if __name__ == '__main__':
    main()