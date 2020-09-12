def function(a, b, c):
  while a < c:
      print(a + b)
      a += b
      if a >= c:
        break
        print(a)

function(10, 6, 25)
function(5, 2, 15)