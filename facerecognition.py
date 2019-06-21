from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from mtcnn.mtcnn import MTCNN
from io import BytesIO
import base64

def draw_boxes(filename, result_list):
	img=plt.imread(filename)
	plt.imshow(img)
	ax=plt.gca()
	for result in result_list:
		x, y, w, h = result['box'] # x-pos, y-pos, width, height
		rect=Rectangle((x, y), w, h, fill=False, color='yellow')
		ax.add_patch(rect)
	figfile = BytesIO()
	plt.savefig(figfile, format='png')
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue()).decode('ascii')
	return figdata_png

def run():
	filename='uploads/sample.jpg'
	img=plt.imread(filename)
	faces=MTCNN().detect_faces(img)
	figdata_png=draw_boxes(filename, faces)
	return figdata_png