для пошуку найщасливішого штату
./happiest_state AFINN-111.txt twitter-stream.txt 
@return %state name%

скрипт створює файл happy_states_scores.txt з оцінками щасливості штатів

для малювання графу, і його збереження в форматах pdf\png (plot.pdf, plot.png)
./plot happy_states_scores.txt 
@return plot.*

