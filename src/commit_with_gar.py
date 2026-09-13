from google.cloud import aiplatform

# Initialize the aiplatform package
aiplatform.init(
    project="fluent-anagram-326107",
    location='asia-northeast1',
    staging_bucket='gs://mlops_samples/pipelines')

# Alternatively, create a pipeline job using a tag.
job = aiplatform.PipelineJob(
    display_name="mlops_sample_1",
    template_path="https://asia-northeast1-kfp.pkg.dev/fluent-anagram-326107/mlops-kubeflow-sample/pythagorean/v0.0.1",
    enable_caching = False,
    parameter_values={
            'a': 4.5,
            'b': 6.5
        }
    )

job.submit(
    service_account = "vertexai-pipelines-sa@fluent-anagram-326107.iam.gserviceaccount.com"
)
