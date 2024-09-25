import numpy as np
import pandas as pd


class EurostatTransformer:
    def __init__(self, file_path, sheet_name=None):

        self.file_path = file_path
        self.sheet_name = sheet_name
        self.df = None
        self.transformed_df = None

    def load_data(self):

        try:
            self.df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
            print(f"Adatok betöltve a(z) '{self.sheet_name}' munkalapról.")
            self.df = self.df.loc[:, ~self.df.columns.str.contains('^Unnamed')]
            self.df.replace(':', np.nan, inplace=True)
            self.df.columns = self.df.columns.str.strip()

              #for index, row in self.df.head().iterrows():
              #  print(f"Sor {index + 1}:")
              #  for col_name in self.df.columns:
              #      print(f"  {col_name}: {row[col_name]}")
              #  print("-" * 40)
        except Exception as e:
            print(f"Hiba történt az adatok betöltésekor: {e}")

    def transform_data(self):
        if self.df is not None:
            self.transformed_df = self.df.melt(id_vars=["GEO (Labels)"],
                                               var_name="Évszám",
                                               value_name="Az internet-hozzáférés szintje")
            print("Az adatok átalakítva.")
        else:
            print("Először be kell tölteni az adatokat.")

    def save_transformed_data(self):
        if self.transformed_df is not None:
            output_path = self.file_path.replace(".xlsx", "_transformed.xlsx")
            self.transformed_df.to_excel(output_path, index=False)
            print(f"Az átalakított adatok mentése megtörtént: {output_path}")
        else:
            print("Először át kell alakítani az adatokat.")
