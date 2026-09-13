from kfp import dsl

@dsl.component(
    base_image='python:3.12',
    target_image='asia-northeast1-docker.pkg.dev/fluent-anagram-326107/mlops-image-sample/components:v0.0.1'
)
def add(x: float, y: float) -> float:
    return x + y

if __name__ == '__main__':
    print(add.python_func(9))