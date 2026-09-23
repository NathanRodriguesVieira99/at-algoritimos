import random
import time

def linear_search(arr,target):
  comparisons =0
  for i in range(len(arr)):
    comparisons += 1
    if arr[i] == target:
      return i, comparisons
  return -1, comparisons

print(linear_search([6, 99, 67, 39, 5], 37))


def gen_vector(n, scenary):
    if scenary == "ordenado":
        return list(range(n))
    if scenary == "reverso":
        return list(range(n - 1, -1, -1))
    if scenary == "aleatorio":
        v = list(range(n))
        random.shuffle(v)
        return v
    raise ValueError(f"cenário inválido: {scenary}")

def binary_search(sorted_arr, target):
    comparisons = 0
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        middle = (left + right) // 2
        comparisons += 1
        if sorted_arr[middle] == target:
            return middle, comparisons
        comparisons += 1
        if sorted_arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1, comparisons


print(binary_search([1, 37, 55, 157, 89, 161, 163], 13))
print(binary_search([1, 33, 52, 7, 99, 111, 13], 8))


for c in ["ordenado", "reverso", "aleatorio"]:
    print(c, gen_vector(10, c))

print(f"{'n':>9} | {'cenário':<10} | {'alvo':<11} | {'valor':>7} | {'linear':>8} | {'binária':>7}")
print("-" * 68)


for n in [10**2, 10**3, 10**4, 10**5, 10**6]:
    for scenary in ["ordenado", "reverso", "aleatorio"]:
        vector = gen_vector(n, scenary)
        ord_vector = sorted(vector)
        for t, target in [("sorteado", random.randrange(n)), ("inexistente", -1)]:
            _, comp_linear = linear_search(vector, target)
            _, comp_bin = binary_search(ord_vector, target)
            print(f"{n:>9} | {scenary:<10} | {t:<11} | {target:>7} | {comp_linear:>8} | {comp_bin:>7}")


def is_ordered(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def looks_ordered(arr, samples=32, seed=0):
    n = len(arr)
    if n < 2:
        return True
    rng = random.Random(seed)
    for _ in range(samples):
        i = rng.randrange(n - 1)
        if arr[i] > arr[i + 1]:
            return False
    return arr[0] <= arr[n // 2] <= arr[-1]


def verifyed_binary_search(sorted_arr, target, mode="completo"):
    if mode == "completo":
        ok = is_ordered(sorted_arr)
    elif mode == "amostragem":
        ok = looks_ordered(sorted_arr)
    else:
        raise ValueError(f"modo inválido: {mode}")

    if not ok:
        raise ValueError("binary_search: pré-condição violada, o vetor não está ordenado.")
    return binary_search(sorted_arr, target)

print(verifyed_binary_search([1, 3, 5, 7, 9], 7))

for mode in ["completo", "amostragem"]:
    try:
        verifyed_binary_search([9, 7, 5, 3, 1], 7, mode=mode)
    except ValueError as erro:
        print(f"[{mode}] {erro}")


almost = list(range(100_000))
almost[70_000], almost[70_001] = almost[70_001], almost[70_000]
print("completa detecta?  ", not is_ordered(almost))
print("amostragem detecta?", not looks_ordered(almost))


class No:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        novo = No(value)
        if self.head is None:
            self.head = self.tail = novo
        else:
            self.tail.next = novo
            self.tail = novo


def vector_to_list(vector):
    listt = SinglyLinkedList()
    for value in vector:
        listt.append(value)
    return listt


def list_linear_search(lista, target):
    comparisons = 0
    actual = lista.head
    position = 0
    while actual is not None:
        comparisons += 1
        if actual.value == target:
            return position, comparisons
        actual = actual.next
        position += 1
    return -1, comparisons


listtt = vector_to_list([4, 9, 2, 7, 5])
print(list_linear_search(listtt, 7))
print(list_linear_search(listtt, 8))


def medir(func, structure, target, repetition=3):
    better = float("inf")
    for _ in range(repetition):
        init = time.perf_counter()
        _, comparisons = func(structure, target)
        better = min(better, time.perf_counter() - init)
    return comparisons, better


print(f"{'n':>9} | {'cenário':<10} | {'alvo':<11} | {'comp vetor':>10} | {'comp lista':>10} | "
      f"{'tempo vetor':>11} | {'tempo lista':>11}")
print("-" * 90)

for n in [10**2, 10**3, 10**4, 10**5, 10**6]:
    for scenary in ["ordenado", "reverso", "aleatorio"]:
        vetor = gen_vector(n, scenary)
        lista = vector_to_list(vetor)
        for tipo, alvo in [("sorteado", random.randrange(n)), ("inexistente", -1)]:
            comp_vetor, t_vetor = medir(linear_search, vetor, alvo)
            comp_lista, t_lista = medir(list_linear_search, lista, alvo)
            assert comp_vetor == comp_lista
            print(f"{n:>9} | {scenary:<10} | {tipo:<11} | {comp_vetor:>10} | {comp_lista:>10} | "
                  f"{t_vetor:>10.5f}s | {t_lista:>10.5f}s")
