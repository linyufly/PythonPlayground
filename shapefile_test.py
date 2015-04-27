# Author: Mingcheng Chen (linyufly@gmail.com)

import shapefile

def writer_test():
  w = shapefile.Writer(shapefile.POLYGON)
  w.poly(parts = [[[1, 5], [5, 5], [5, 1], [3, 3], [1, 1]]])
  w.field('FIRST_FLD', 'C', '40')
  w.field('SECOND_FLD', 'C', '40')
  w.record('First', 'Polygon')
  w.save('polygon')

  w = shapefile.Writer(shapefile.POLYLINE)
  w.line(parts = [[[1, 10], [5, 10], [5, 6], [3, 8], [1, 6]], [[5, 5], [6,6]]])
  w.field('ID', 'C', '50')
  w.record('line 1')
  w.record('line 2')
  w.save('polyline')

def main():
  writer_test()

if __name__ == "__main__":
  main()
