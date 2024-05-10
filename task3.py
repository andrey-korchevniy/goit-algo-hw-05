from kpm_algorithm import kmp_search
from bm_algorithm import boyer_moore_search
from rk_algorithm import rabin_karp_search
import timeit
import matplotlib.pyplot as plt
import numpy as np

def search_text(url, substring):
    single_string = ''
    try:
        with open(url, 'r', encoding='utf-8') as file:
            content = file.read()
            single_string = content.replace('\n', ' ')
    except FileNotFoundError:
        print(f"Файл не знайдено: {url}")
        return None
    except Exception as e:
        print(f"Відбулася помилка: {str(e)}")
        return None

    kmp_time = timeit.timeit(lambda: kmp_search(single_string, substring), number=1)
    bm_time = timeit.timeit(lambda: boyer_moore_search(single_string, substring), number=1)
    rk_time = timeit.timeit(lambda: rabin_karp_search(single_string, substring), number=1)

    return (kmp_time, bm_time, rk_time)

test1_true = search_text('data/article1.txt', 'ізнес-додат')
test1_false = search_text('data/article1.txt', 'ізнесдодат')
test2_true = search_text('data/article2.txt', 'відмінність у часі')
test2_false = search_text('data/article2.txt', 'ізнесдодат')
print(test1_true)
print(test1_false)
print(test2_true)
print(test2_false)

true_data = [td if td is not None else (0, 0, 0) for td in [test1_true, test2_true]]
false_data = [fd if fd is not None else (0, 0, 0) for fd in [test1_false, test2_false]]

labels = ['KMP', 'Boyer-Moore', 'Rabin-Karp']
x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(2, 1, figsize=(10, 10))

# Гарантируем, что данные имеют корректную длину и содержание
for i, data in enumerate([true_data, false_data]):
    for j, datum in enumerate(data):
        if datum is None:
            data[j] = (0, 0, 0)  # Заменяем None на кортеж с нулями

# Теперь строим графики
for idx, (true_times, false_times) in enumerate(zip(true_data, false_data)):
    ax[idx].bar(x - width/2, [time for time in true_times], width, label='Пошукова фраза є в тексті')
    ax[idx].bar(x + width/2, [time for time in false_times], width, label='Пошукової фрази немає в тексті')

    ax[idx].set_ylabel('Час виконання')
    ax[idx].set_title(f'Порівняння алгоритмів пошуку на тесті {idx + 1}')
    ax[idx].set_xticks(x)
    ax[idx].set_xticklabels(labels)
    ax[idx].legend()

fig.tight_layout()
plt.show()