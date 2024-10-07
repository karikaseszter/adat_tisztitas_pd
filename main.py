from eurostat import EurostatTransformer
from translate import Translator

def translate_text(text, dest_lang='hu'):  # Example translating to Spanish (es)
    try:
        translated = Translator.translate(text, dest=dest_lang)
        return translated.text
    except Exception as e:
        return str(e)

def main():
    eurostat = EurostatTransformer("data/Households - level of internet access.xlsx", "Munka1")
    eurostat.load_data()
    eurostat.transform_data_v1("GEO (Labels)","Évek", "Internet hozzáférés szintje")
    eurostat.translate_text("GEO (Labels)")
    eurostat.save_transformed_data()

    eurostat = EurostatTransformer("data/Individuals - frequency of internet use.xlsx", "Munka1")
    eurostat.load_data()
    eurostat.transform_data_v1(["GEO (Labels)", "INDIC_IS (Labels)"], "Évek", "Internet használat gyakorisága")
    eurostat.translate_text("GEO (Labels)")
    eurostat.translate_text("INDIC_IS (Labels)")
    eurostat.save_transformed_data()

    eurostat = EurostatTransformer("data/Individuals - internet activities.xlsx", "Munka1")
    eurostat.load_data()
    eurostat.transform_data_v1(["IND_TYPE (Labels)", "INDIC_IS (Labels)"], "Évek", "%")
    eurostat.translate_text("IND_TYPE (Labels)")
    eurostat.translate_text("INDIC_IS (Labels)")
    eurostat.save_transformed_data()

    eurostat = EurostatTransformer("data/Individuals - devices used to access the internet.xlsx", "Munka1")
    eurostat.load_data()
    eurostat.transform_data_v1(["IND_TYPE (Labels)", "INDIC_IS (Labels)"], "Évek", "%")
    eurostat.translate_text("IND_TYPE (Labels)")
    eurostat.translate_text("INDIC_IS (Labels)")
    eurostat.save_transformed_data()

if __name__== "__main__":
    main()