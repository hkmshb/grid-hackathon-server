from .service import get_models


def add_resources_doc(func):
    models = get_models()
    examples = "\n\t  ".join(
        [f"{resource}: {model.example}" for resource, model in models.items()])
    definitions = "\n\t".join([
f"""{resource}:
type: object
properties:
    type:
        type: string
    id: 
        type: string
    geometry:
        type: object
        properties:
            type:
                type: string
            coordinates:
                type: array
                items: 
                    type: number
    geometry_name:
        type: string
    properties:
        {model.model}""".replace('\n', '\n\t\t\t').expandtabs(4)
                for resource, model in models.items()])
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
      - name: size
        description: Number of items to return.
        in: query
        type: int
        default: 200
      - name: page
        description: The page of items to return.
        in: query
        type: int
        default: 1
      - name: sort_by
        description: Resource field to sort results by.
        in: query
        type: string
        default: global_id
      - name: fields
        description: Comma-separated list of fields to return for each resource.
        in: query
        type: string
    definitions:
        {definitions}
    responses:
      200:
        description: Datasets in resource.
        examples:
          {examples}
    """
    return func
