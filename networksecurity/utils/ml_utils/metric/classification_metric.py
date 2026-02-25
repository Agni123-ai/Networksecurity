from networksecurity.entity.artifact_entity import classificationMetricArtifact
from networksecurity.exception.exception import NetworkSecurityException
from sklearn.metrics import f1_score,precision_score,recall_score

def get_classification_score(y_true,y_pred)->classificationMetricArtifact:
  try:
    f1_score_value=f1_score(y_true,y_pred)
    precision_score_value=precision_score(y_true,y_pred)
    recall_score_value=recall_score(y_true,y_pred)
    classification_metric_artifact=classificationMetricArtifact(f1_score=f1_score_value,precision_score=precision_score_value,recall_score=recall_score_value)
    return classification_metric_artifact
  except Exception as e:
    raise NetworkSecurityException(e,sys) from e