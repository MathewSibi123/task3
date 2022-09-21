def toString(List):


  return ''.join(List)


def permutestring(a, l, r):
  if l == r:
    print(toString(a))

  else:
    for i in range(l, r):
    a[l], a[i] = a[i], a[l]
    permute(a, l + 1, r)
    a[l], a[i] = a[i], a[l]

  sample = "ABC"
  n = len(sample)
  a = list(sample)
  permutestring(a, 0, n)
