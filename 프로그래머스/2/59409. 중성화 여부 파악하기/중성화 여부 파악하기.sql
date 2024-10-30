SELECT ANIMAL_ID, NAME, if (sex_upon_intake like '%Neutered%' or sex_upon_intake like '%Spayed%', "O", "X")
from animal_ins
order by ANIMAL_ID