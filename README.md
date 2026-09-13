# Sample #

## 構築 ##

### GCS ###

gs://mlops_samples/pipelines

gcloud auth configure-docker asia-northeast1-docker.pkg.dev

kfp component build src/components --build-image --push-image





## 参考 ##

- [Vertex AI SDK for Python](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest)
  - [PipelineJob](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.PipelineJob)
  - [kfp-component-build](https://kubeflow-pipelines.readthedocs.io/en/stable/source/cli.html#kfp-component-build)
  - [Containerized Python Components](https://www.kubeflow.org/docs/components/pipelines/user-guides/components/containerized-python-components/)
  - [パイプライン テンプレートの作成、アップロード、使用](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/create-pipeline-template?hl=ja)
