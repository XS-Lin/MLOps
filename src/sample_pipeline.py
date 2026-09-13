from kfp import dsl
from components import math_add, math_square_root, math_square

@dsl.pipeline
def pythagorean(a: float, b: float) -> float:
    a_sq_task = math_square.square(x=a)
    b_sq_task = math_square.square(x=b)
    sum_task = math_add.add(x=a_sq_task.output, y=b_sq_task.output)
    return math_square_root.square_root(x=sum_task.output).output

if __name__ == '__main__':
    from kfp import compiler
    from kfp.registry import RegistryClient
    import google.cloud.aiplatform as aip

    pipeline_path = r'.\build\image_classif_pipeline.yaml'
    compiler.Compiler().compile(
        pipeline_func = pythagorean,
        package_path = pipeline_path
    )

    client = RegistryClient(host=f"https://asia-northeast1-kfp.pkg.dev/fluent-anagram-326107/mlops-kubeflow-sample")
    templateName, versionName = client.upload_pipeline(
        file_name = pipeline_path,
        tags = ["v0.0.1"]
    )

    # job = aip.PipelineJob(
    #     project = "fluent-anagram-326107",
    #     location = "asia-northeast1",
    #     display_name = "mlops_sample",
    #     template_path = pipeline_path,
    #     pipeline_root = "gs://mlops_samples/pipelines",
    #     enable_caching = False,
    #     parameter_values={
    #         'a': 4.5,
    #         'b': 6.5
    #     }
    # )
    
    # job.submit(
    #     service_account = "vertexai-pipelines-sa@fluent-anagram-326107.iam.gserviceaccount.com"
    # )



# asia-northeast1.docker.pkg.dev/fluent-anagram-326107/mlops
# asia-northeast1.docker.pkg.dev/fluent-anagram-326107/mlops/data-processor:v1.0
# https://console.cloud.google.com/artifacts/browse/fluent-anagram-326107?hl=ja&inv=1&invt=AbkWrg&project=fluent-anagram-326107
#   mlops-image-sample
#   mlops-kubeflow-sample
# kfp component build src/components --no-build-image --no-push-image