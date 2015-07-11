python ./src/mapper.py
LC_COLLATE=C sort ./tweet_output/mapped.txt -o ./tweet_output/mapped_sorted.txt
python ./src/reducer.py
