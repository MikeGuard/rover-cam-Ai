def salvataggio_x(centro : tuple, width : int) -> list:
    x = []
    x.append(centro[0] - (width / 2))
    return x

def x_più_vicina(x : list) -> int:
  x.sort(key=abs)
  x_vicina = x[0]
  return x_vicina