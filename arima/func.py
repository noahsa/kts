from parliament import Context

import json
import logging

import numpy as np
import pmdarima


def main(context: Context):
    """
    Function template
    The context parameter contains the Flask request object and any
    CloudEvent received with the request.
    """
    data = json.loads(context.request.get_data())

    input = np.array(data['input'])

    arima = pmdarima.AutoARIMA(**data['params'])

    model = arima.fit(y=input)

    preds = list(model.predict(n_periods=data['h']))

    return { "predictions": preds}, 200
