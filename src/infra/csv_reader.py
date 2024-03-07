import pandas as pd


class CSVHelper:
    """ a class used for handling with csv files"""

    def __init__(self, file_path):
        """
        Constructor for CSVHelper.

        :param file_path: Path to the CSV file.
        :type file_path: str
        """
        self.file_path = file_path

    def read_csv_to_dataframe(self):
        """
        Read logs from CSV file into a DataFrame.

        :return: DataFrame containing the logs from the CSV file.
        :rtype: pandas.DataFrame
        """
        try:
            df = pd.read_csv(self.file_path)
            return df
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return None

    def save_dataframe_to_csv(self, dataframe):
        """
        Save DataFrame to a CSV file.

        :param dataframe: DataFrame to be saved.
        :type dataframe: pandas.DataFrame
        """
        try:
            dataframe.to_csv(self.file_path, index=False)
            print(f"DataFrame successfully saved to '{self.file_path}'.")
        except Exception as e:
            print(f"Error occurred while saving DataFrame to '{self.file_path}': {e}")
