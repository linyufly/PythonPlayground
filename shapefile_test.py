# Author: Mingcheng Chen (linyufly@gmail.com)

import shapefile

kTrajectoryFile = '/home/linyufly/GitHub/vfkm/data/atlantic_storms.txt'
kClusterFilePrefix = '/home/linyufly/GitHub/vfkm/output/curves_r_'
kOutputFilePrefix = './output/cluster_'
kNumberOfClusters = 7

def writer_test():
  w = shapefile.Writer(shapefile.POLYGON)
  w.poly(parts = [[[1, 5], [5, 5], [5, 1], [3, 3], [1, 1]]])
  w.field('FIRST_FLD', 'C', '40')
  w.field('SECOND_FLD', 'C', '40')
  w.record('First', 'Polygon')
  w.save('polygon')

  w = shapefile.Writer(shapefile.POLYLINE)
  # w.line(parts = [[[1, 10], [5, 10], [5, 6], [3, 8], [1, 6]], [[5, 5], [6,6]]])

  # w.line(parts = [[[20.5, -67.1], [20.7, -68.0], [20.9, -68.8], [21.1, -69.6]], [[27.5, -78.5], [28.0, -78.9], [28.5, -79.3], [28.9, -79.6], [29.3, -79.9], [29.7, -80.2], [30.0, -80.5], [30.3, -80.7], [30.6, -80.9], [30.9, -80.9], [31.3, -80.6], [31.7, -80.1], [32.1, -79.4], [32.5, -78.5]]])

  w.line(parts = [[[20.5, -67.1], [20.7, -68.0], [20.9, -68.8], [21.1, -69.6], [21.2, -70.6], [21.5, -71.9], [21.7, -73.0], [21.9, -74.0], [22.1, -74.9], [22.2, -76.1], [22.6, -77.1], [22.9, -78.1], [23.2, -79.3], [23.5, -80.1], [23.8, -81.1], [24.2, -82.1], [24.7, -83.1], [25.2, -83.9], [25.7, -84.6], [26.2, -85.3], [26.7, -86.0], [27.2, -86.6], [27.7, -87.1], [28.2, -87.5], [28.6, -87.8], [28.8, -88.0], [29.1, -88.2], [29.4, -88.4], [29.8, -88.6], [30.2, -88.6], [30.6, -88.5], [31.2, -88.1], [31.8, -87.4], [32.3, -86.3], [32.8, -84.8], [33.2, -82.8], [33.5, -80.5], [33.8, -78.2], [34.0, -76.0], [34.4, -74.2], [35.2, -72.8], [36.4, -71.8], [38.0, -70.8], [39.6, -69.6], [41.0, -68.0]]])

  w.line(parts = [[[27.5, -78.5], [28.0, -78.9], [28.5, -79.3], [28.9, -79.6], [29.3, -79.9], [29.7, -80.2], [30.0, -80.5], [30.3, -80.7], [30.6, -80.9], [30.9, -80.9], [31.3, -80.6], [31.7, -80.1], [32.1, -79.4], [32.5, -78.5]]])

  w.field('ID', 'C', '50')
  w.record('line 1')
  w.record('line 2')
  w.save('polyline')

def trajectory_cluster_test():
  reader = open(kTrajectoryFile, 'r')
  [x_min, x_max, y_min, y_max, t_min, t_max] = \
      [float(x) for x in reader.readline().split()]

  print 'x_min: {0}, x_max: {1}', x_min, x_max
  print 'y_min: {0}, y_max: {1}', y_min, y_max
  print 't_min: {0}, t_max: {1}', t_min, t_max

  trajectories = []
  curr_traj = []
  for line in reader:
    [x, y, t] = [float(x) for x in line.split()]
    if x == 0.0 and y == 0.0 and t == 0.0:
      trajectories.append(curr_traj)
      curr_traj = []
    else:
      curr_traj.append([y, x])

  reader.close()

  for index in range(kNumberOfClusters):
    file_name = kClusterFilePrefix + str(index) + '.txt'
    reader = open(file_name, 'r')

    writer = shapefile.Writer(shapefile.POLYLINE)
    writer.field('ID', 'C', '20')

    for line in reader:
      traj_id = int(line.split()[0])
      writer.line(parts = [trajectories[traj_id]])
      writer.record('line {0}', traj_id)

    reader.close()

    writer.save(kOutputFilePrefix + str(index))

def main():
  # writer_test()
  trajectory_cluster_test()

if __name__ == '__main__':
  main()

