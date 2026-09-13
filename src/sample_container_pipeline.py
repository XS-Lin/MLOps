from kfp import dsl

@dsl.container_component
def say_hello(name: str, greeting: dsl.OutputPath(str)):
    """Log a greeting and return it as an output."""

    return dsl.ContainerSpec(
        image='alpine',
        command=[
            'sh', '-c', '''RESPONSE="Hello, $0!"\
                            && echo $RESPONSE\
                            && mkdir -p $(dirname $1)\
                            && echo $RESPONSE > $1
                            '''
        ],
        args=[name, greeting])

@dsl.pipeline
def hello_pipeline(person_to_greet: str) -> str:
    # greeting argument is provided automatically at runtime!
    hello_task = say_hello(name=person_to_greet)
    return hello_task.outputs['greeting']

if __name__ == '__main__':
    from kfp import compiler
    import google.cloud.aiplatform as aip

    pipeline_path = r'.\build\sample_container_pipeline.yaml'

    compiler.Compiler().compile(hello_pipeline, pipeline_path)

    job = aip.PipelineJob(
        project = "fluent-anagram-326107",
        location = "asia-northeast1",
        display_name = "mlops_sample",
        template_path = pipeline_path,
        pipeline_root = "gs://mlops_samples/pipelines",
        enable_caching = False,
        parameter_values={
            'person_to_greet': 'everyone',
        }
    )
    
    job.submit(
        service_account = "vertexai-pipelines-sa@fluent-anagram-326107.iam.gserviceaccount.com"
    )