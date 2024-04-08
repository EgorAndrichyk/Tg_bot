# parser urls
DEFAULT_URL = "https://fgis.gost.ru/fundmetrology/cm/results?filter_applicability=true&activeYear=%D0%92%D1%81%D0%B5"
PARSING_URL = (
    "https://fgis.gost.ru/fundmetrology/cm/results?"
    "filter_applicability={0}"
    "&filter_mi_mitype={1}"
    "&filter_mi_number={2}"
    "&activeYear=%D0%92%D1%81%D0%B5"
)

# MI types
DN = "ДН-130"
TP = "ТП-140"
GSV = "ГСВ-1"
