from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

class NetwrokModel:
  def __init__(self,preprocessor,model):
    try:
      self.preprocessor=preprocessor
      self.model=model
    except Exception as e:
      raise NetworkSecurityException(e,sys) from e
  
  def predict(self,X):
    try:
      x_transformed=self.preprocessor.transform(X)
      y_hat=self.model.predict(x_transformed)  
      return y_hat
    except Exception as e:
      raise NetworkSecurityException(e,sys) from e