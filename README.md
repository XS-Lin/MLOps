# Sample #

## 構築 ##

### GCS ###

gs://mlops_samples/pipelines

gcloud auth configure-docker asia-northeast1-docker.pkg.dev

kfp component build src/components --build-image --push-image

## 参考 ##

- [Vertex AI SDK for Python](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)
  - [PipelineJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PipelineJob)

