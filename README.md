# kts

Scale time series forecasting with Kubernetes.

## Forecast methods deployed as services

1) ARIMA
2) ETS

## Tools Required

1) OpenShift instance with the OpenShift Serverless operator.
2) [OpenShift CLI](https://formulae.brew.sh/formula/openshift-cli) - Link for Mac
3) [KNative CLI](https://docs.openshift.com/container-platform/4.9/serverless/cli_tools/installing-kn.html#installing-cli-macosx_installing-kn)
4) [Quay Registry](https://quay.io/)

## Deploy

1. Login to OpenShift. Get command from `Copy login command` in the OpenShift web console.

    ```bash
    oc login --token=token --server=cluster_url
    ```

2. Login to Quay

    ```bash
    docker login quay.io
    ```

3. Create a new OpenShift project

    ```bash
    oc new-project kts
    ```

4. Build the ARIMA & ETS container image.

    ```bash
    arima$ kn func build
    ets$ kn func build
    ```

5. Deploy the ARIMA & ETS service to OpenShift. 

    ```bash
    arima$ kn func deploy
    ets$ kn func deploy
    ```

    If this is the first time deploying, go to the quay.io web UI and make the images public. Then, re-run the above commands.

## Test

Send a request! Get the `service_url` from the `kn service create` output or the OpenShift Web UI.

```bash
curl -X POST -H "Content-Type: application/json" --data '{"input":[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0,13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0,25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0], "params":{}, "h":4}' service_url
```

### Test locally

To test before deploying to OpenShift. Navigate to the arima or ets directory, run:

```bash
kn func run
```

This will deploy your service to `http://127.0.0.1:8080`. Run the above curl request with `http://127.0.0.1:8080` as the service_url

## Resources

https://developers.redhat.com/articles/2021/09/02/faster-web-deployment-python-serverless-functions#
