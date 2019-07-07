import imageio
import argparse
import glob
import natsort

parser = argparse.ArgumentParser(description='Created gif from series of images.')
parser.add_argument('path', type=str, help='glob pattern to select files')
parser.add_argument('output', type=str, nargs='?', default=None, help='optional: output name. if empty only lists files')
parser.add_argument('-d','--duration', type=float, default=0.5, help='duration per single image')

args = parser.parse_args()

images = []
files = natsort.natsorted(glob.glob(args.path))
for f in files:
    if args.output is not None:
	images.append(f)
    else:
        print f

if args.output is not None:
    with imageio.get_writer(args.output, mode='I', duration=args.duration) as writer:
        for filename in images:
	    image = imageio.imread(filename)
	    writer.append_data(image)


#
#for filename in filenames:
#    images.append(imageio.imread(filename))
#imageio.mimsave('/path/to/movie.gif', images)
