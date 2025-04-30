import json

def extraction_json(filename: str) -> dict[]:
    """
    Extrait les données du fichier json renseigné, et le transforme en dictionnaire.

    Args:
        filename (str):/!\\ BIEN RENSEIGNER EXTENSION /!\\ 

    Returns:
        dict[]: Un dictionnaire ()
    """
    # extrait les données du fichier json
    with open(filename) as json_file:
        return json.load(json_file)