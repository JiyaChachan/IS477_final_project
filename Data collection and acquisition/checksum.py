import hashlib

def sha256_checksum(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)
    return sha256.hexdigest()

print("Airbnb checksum:", sha256_checksum("data/raw/airbnb_listings_los-angeles_2025-09-01.csv.gz"))
print("Zillow checksum:", sha256_checksum("data/raw/zillow_zip_zhvi_2025.csv"))
print("ZCTA checksum:", sha256_checksum("data/raw/zcta2025/tl_2025_us_zcta520.shp"))
