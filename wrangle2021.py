import pandas as pd
import pyreadstat as pyr
df, meta  = pyr.read_sav('afrobarometer_nigeria_rd8_2021.sav')

class Wrangler:
    """Methods for wrangling data."""

    def __init__(self, df=df, meta=meta):

        """init

        Parameters
        ----------
        df: The dataframe that is loaded
        meta: Information about the data
        """
        self.df, self.meta  = df, meta

    def wrangle(self, columns, rename):
        """Wrangles the dataframe to have get the required columns.

        Parameters
        ----------
        columns : List
            List of columns that need to be extracted from the DataFrame
        rename: List
            List of new names the columns would have

        Returns
        -------
        DataFrame
            Dataframe with extracted columns.
        """
        # Select columns and replace the code numbers in columns with actual names in metadata
        columns = columns
        df_new = self.df.copy()[columns]
        for i in columns:
            x = meta.variable_value_labels[i]
            df_new[i].replace(x, inplace=True)

        # Rename columns
        df_new.columns = rename

        # Return DataFrame
        return df_new

        # Print df.head
        df_new.head()


    def remove(self, columns, df_new):
        """Removes the values that are unimportant.

        Parameters
        ----------
        columns : List
            List of columns that need to be extracted from the DataFrame

        df_new : DataFrame
            Dataframe that contains the data

        Returns
        -------
        DataFrame
            Dataframe with extracted columns.
        """
        remove = ["Not Applicable","Don't know","Don’t know","Refused","Do not understand question", "The country is not a democracy"]
        columns = columns

        for j in columns:
            for i in remove:
                df_new = df_new.loc[df_new[j] != i]

        # Return DataFrame
        return df_new

    def get_frequency(self, columns, df_new):
        """Gets the normalized frequency of the values in each column.

        Parameters
        ----------
        columns : List
            List of columns that their value frequencies need to be gotten

        Returns
        -------
        Nothing.
        """
        for i in columns:
            print(df_new[i].value_counts(normalize=True))
