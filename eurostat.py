import numpy as np
import pandas as pd
from googletrans import Translator

class EurostatTransformer:
    def __init__(self, file_path, sheet_name=None, ):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.df = None
        self.transformed_df = None
        self.translator = Translator()  # Fordító példány létrehozása

    def load_data(self):
        try:
            # Adatok betöltése Excel fájlból
            self.df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
            print(f"Adatok betöltve a(z) '{self.sheet_name}' munkalapról.")

            # Unnamed oszlopok eltávolítása
            self.df = self.df.loc[:, ~self.df.columns.str.contains('^Unnamed')]

            # Hiányzó értékek kezelése
            self.df.replace(':', np.nan, inplace=True)

            # Oszlopnevek eltávolítása
            self.df.columns = self.df.columns.str.strip()

        except Exception as e:
            print(f"Hiba történt az adatok betöltésekor: {e}")

    def transform_data_v1(self, idvar, varname, valuename):
        if self.df is not None:
            self.transformed_df = self.df.melt(id_vars=idvar,
                                                var_name=varname,
                                                value_name=valuename)
            self.transformed_df = self.transformed_df.sort_values(by=idvar)
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