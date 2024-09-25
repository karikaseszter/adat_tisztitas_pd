from eurostat import EurostatTransformer


def main():
    file_path = "data/Households - level of internet access.xlsx"
    sheet_name = "Sheet 1"

    eurostat = EurostatTransformer(file_path, sheet_name)
    eurostat.load_data()
    eurostat.transform_data()
    eurostat.save_transformed_data()


if __name__ == "__main__":
    main()