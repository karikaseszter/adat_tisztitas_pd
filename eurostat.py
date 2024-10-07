import numpy as np
import pandas as pd
from translate import Translator

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

    def translate_text(self, column_name, target_lang='hu'):
        try:
            if self.transformed_df is not None:
                translator = Translator(to_lang=target_lang)
                self.transformed_df[column_name] = self.transformed_df[column_name].apply(lambda x: translator.translate(x) if pd.notnull(x) else x)

                self.transformed_df[column_name].replace({
                    "France": "Franciaország",
                    "Ireland": "Írország",
                    "Portugal": "Portugália",
                    "European Union (27 countries)": "Európai Unió (27 ország)"

                }, inplace=True)

                print(f"A(z) '{column_name}' oszlop lefordítva {target_lang} nyelvre.")
            else:
                print("Először át kell alakítani az adatokat.")
        except Exception as e:
            print(f"Hiba történt a fordítás során: {e}")

    def save_transformed_data(self):
        if self.transformed_df is not None:
            output_path = self.file_path.replace(".xlsx", "_transformed.xlsx")
            self.transformed_df.to_excel(output_path, index=False)
            print(f"Az átalakított adatok mentése megtörtént: {output_path}")
        else:
            print("Először át kell alakítani az adatokat.")