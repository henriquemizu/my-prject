dist=float(input('enter a distance in meters'))

km = dist / 1000
hm = dist / 100
dam = dist / 10
m = dist * 1
dm = dist * 10
cm = dist * 100
mm = dist * 1000

print('the distance {0} is,{1} in km,{2} in hm,{3} in dam,{4} in dm,{5} in cm,and {6} in mm'.format(m,km,hm,dam,dm,cm,mm))
