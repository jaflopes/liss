import random

print("Gerar 5 números inteiros aleatoriamente de 0 a 100")
r1, r2, x1 = 1, 100, 5
randomlist = random.sample(range(r1, r2), x1)
print("Ver a lista de inteiros: " + str(randomlist))


def selection_sort(values):
    for i, item in enumerate(values[:-1]):
        smallest_i = i
        for index_to_compare, item_to_compare in enumerate(values[i::], i):
            if item_to_compare < values[smallest_i]:
                smallest_i = index_to_compare
        values[i], values[smallest_i] = (values[smallest_i], values[i])
    return values


if __name__ == '__main__':
    print("Lista ordenada: ", selection_sort(randomlist))
