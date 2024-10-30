SELECT ANIMAL_ID, NAME, if (sex_upon_intake like '%Neutered%' or sex_upon_intake like '%Spayed%', "O", "X") as 중성화
from animal_ins
order by ANIMAL_ID