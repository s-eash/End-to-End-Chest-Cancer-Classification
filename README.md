# End-to-End-Chest-Cancer-Classification
import dagshub
dagshub.init(repo_owner='eashwaransridhar', repo_name='End-to-End-Chest-Cancer-Classification', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)
  https://dagshub.com/eashwaransridhar/End-to-End-Chest-Cancer-Classification.mlflow