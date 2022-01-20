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
    if hasattr(context, "cloud_event") and hasattr(context.cloud_event, "data"):
         data = context.cloud_event.data
    elif hasattr(context, "request"):
         data = json.loads(context.request.get_data())
    else:
         data = context #assume this is from test...
    logging.warning(f'**************  data from request: {data}')
    logging.warning(str(type(data))) # this is a dict

    input = np.array(data['input'])

    arima = pmdarima.AutoARIMA(**data['params'])

    model = arima.fit(y=input)

    preds = list(model.predict(n_periods=data['h']))

    return { "predictions": preds}, 200
