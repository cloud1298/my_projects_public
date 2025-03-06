import json

from kivy.network.urlrequest import UrlRequest


class HttpClient:
    def get_pizzas(self, on_complete, on_error):
        url = "http://127.0.0.1:8000/api/GetPizzas"

        def data_received(req, result):
            data = json.loads(result)
            pizzas_dict = [pizza["fields"] for pizza in data]
            print("Data received")

            if on_complete:
                on_complete(pizzas_dict)

        def data_error(req, error):
            print("Data error")

            if on_error:
                on_error(error.verify_message)

        def data_failure(req, result):
            print("Data failure")

            if on_error:
                on_error(f"Server error: {req.resp_status}")

        req = UrlRequest(
            url,
            on_success=data_received,
            on_error=data_error,
            on_failure=data_failure,
        )
