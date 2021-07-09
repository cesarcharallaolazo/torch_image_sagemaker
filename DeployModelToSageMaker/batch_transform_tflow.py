from PIL import Image
import io
import numpy as np
import tensorflow as tf
import logging
from tensorflow.python.saved_model import loader

def __init__(self, sess, result):
    self.sess=tf.Session()
    self.result = []

def input_fn(self,request_body):
    logging.info('An input_fn that loads an image tensor’)
    img_arr = np.array(Image.open(io.BytesIO(request_body)))
    (im_width, im_height) = img.size
    img_np=np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)
    img_np_expanded = np.expand_dims(img_np, axis=0)
    return img_np_expanded

def model_fn(self, model_dir):
    logging.info('A model fn that loads a model’)
    frozen_graph_exists = glob.glob(os.path.join(model_dir, “*.pb”))

if (len(frozen_graph_exists) > 0):
    with tf.Graph().as_default() as graph:
        self.sess = tf.Session(graph=graph)
        loader.load(self.sess, [tf.saved_model.tag_constants.SERVING],
        os.path.join(model_dir))

def predict_fn(self, input_data):
    logging.info('Entering the predict_fn function’)
    preds = self.sess.run(['detection_classes:0’], feed_dict={'image_tensor:0’: input_data})
    return preds

def output_fn(self, prediction_output, accept=JSON_CONTENT_TYPE):
    logging.info('Entering the output_fn function’)
    return json.dumps(prediction_output), accept