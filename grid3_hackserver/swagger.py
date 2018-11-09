from .service import get_models


def add_resources_doc(func):
    models = get_models()

    examples = "\n".join(
        [f"{resource}: {model.example}" for resource, model in models.items()])
    definitions = "\n".join([f"{model.model}" for model in models.values()])
    resources = list(models.keys())

    func.__doc__ = f"""Endpoint returning data based on requested resource.
    ---
    parameters:
      - name: resource_name
        in: path
        type: string
        enum: {resources}
        required: true
        default: {resources[0]}
    definitions:
        {definitions}
    responses:
      200:
        description: Datasets in resource.
        examples:
          {examples}
    """
    return func
