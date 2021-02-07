def countit(x='aaaabbbcca'):
  res=[]
  con=[]
  for i in x:
    if i in con:
      con.append(i)
    else:
      res.append(con)
      con=[i]
    previous = i
  res.append(con)
  res2 = list(filter(None, res))
  tups = [(x[0], len(x)) for x in res2]
  return tups

if __name__ == '__main__':
  countit()