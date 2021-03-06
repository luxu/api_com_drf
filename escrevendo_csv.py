import csv

with open("fix/estudantes.csv", "w", encoding="utf-8") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(["nome", "data_nascimento", "sexo", "serie"])
    # escrever mais de uma linha com o writerows (plural)
    rows = [
        ["Isabelly Simone Drumond", "12/03/1969", "F", "1ª Série"],
        ["Cecília Sarah Rocha", "25/09/1965", "F", "1ª Série"],
        ["Lorenzo Nicolas Castro", "20/03/1964", "M", "2ª Série"],
        ["Mariane Simone Isadora Ramos", "09/04/1949", "F", "3ª Série"],
        ["Sebastião Noah Vinicius da Silva", "14/06/1981", "M", "1ª Série"],
        ["Roberto Pietro Rodrigues", "27/09/1970", "M", "4ª Série"],
        ["Kamilly Tatiane Galvão", "06/12/1970", "F", "2ª Série"],
        ["Isabelly Ornelas Fortunato", "11/07/1987", "F", "2ª Série"],
        ["Leia Marinho", "11/07/1988", "F", "4ª Série"],
        ["Luís Passarinho Cirne", "20/12/2000", "M", "1ª Série"],
    ]
    csv_writer.writerows(rows)
