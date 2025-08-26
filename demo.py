from data_protector import mask_data

if __name__ == "__main__":
    print("--- Scenario 1: Email ---")
    print(mask_data({"email": "john.doe@example.com"}, ttl=3600))

    print("--- Scenario 2: Téléphone ---")
    print(mask_data({"phone": "+33612345678"}, ttl=600))

    print("--- Scenario 3: Carte bancaire ---")
    print(mask_data({"card": "1234567812345678"}, ttl=60))
