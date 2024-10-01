from eurostat import EurostatTransformer


def main():
    eurostat = EurostatTransformer("data/Households - level of internet access.xlsx", "Sheet 1")
    eurostat.load_data()
    eurostat.transform_data_v1("GEO (Labels)","Évek", "Az internet hozzáférés szintje")
    eurostat.save_transformed_data()


    eurostat = EurostatTransformer("data/Individuals - frequency of internet use.xlsx", "Sheet 1")
    eurostat.load_data()
    eurostat.transform_data_v1(["GEO", "INDIC_IS"], "Évek", "Az internet hozzáférés szintje")
    eurostat.save_transformed_data()

    eurostat = EurostatTransformer("data/Individuals - internet activities.xlsx", "Munka1")
    eurostat.load_data()
    eurostat.transform_data_v1(["IND_TYPE", "INDIC_IS"], "Évek", "%")
    eurostat.save_transformed_data()

if __name__== "__main__":
    main()