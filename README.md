# kts

Scale time series forecasting with Kubernetes.

## Forecast methods deployed as services

1) ARIMA
2) ETS

## Setup

OpenShift instance configured with OpenShift Serverless.

Install [KNative CLI](https://docs.openshift.com/container-platform/4.9/serverless/cli_tools/installing-kn.html#installing-cli-macosx_installing-kn)

```bash
oc delete limitranges kts-core-resource-limits
```

```bash
kn service create arima --port 8080 --limit memory- --limit cpy- --image quay.io/nsayre/kts-arima:latest
kn service create ets --port 8080 --limit memory- --limit cpy- --image quay.io/nsayre/kts-ets:latest
```

Test ARIMA service

```bash
curl -X POST -H "Content-Type: application/json" --data '{"input":[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0,13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0,25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0], "params":{}, "h":4}' http://arima-kts.apps.cluster-kq2s8.kq2s8.sandbox566.opentlc.com
```

Test ETS service

```bash
curl -X POST -H "Content-Type: application/json" --data '{"input":[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0,13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0,25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0], "params":{"auto": "True", "sp":12}, "h":8}' http://ets-kts.apps.cluster-kq2s8.kq2s8.sandbox566.opentlc.com
```

Test locally

Start function on localhost and run above curl

```bash
kn func run
```

```bash
curl -X POST -H "Content-Type: application/json" --data '{"input":[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0,13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0,25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0], "params":{"auto": "True", "sp":12}, "h":8}' http://127.0.0.1:8080
```

## Resources

https://developers.redhat.com/articles/2021/09/02/faster-web-deployment-python-serverless-functions#
