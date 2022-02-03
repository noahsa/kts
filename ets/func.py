from parliament import Context

import json
import logging

import numpy as np
import sktime.forecasting.ets


def main(context: Context):
    """
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """
    data = json.loads(context.request.get_data())

    input = np.array(data['input'])

    model = sktime.forecasting.ets.AutoETS(**data['params'])

    fitted = model.fit(input)

    # List of forecast horizon from 1 to length for sktime API
    fh = list(range(1, (data['h'] + 1)))  # pylint: disable=C0301, C0103

    preds = list(fitted.predict(fh=fh).flatten())

    return { "predictions": preds}, 200
