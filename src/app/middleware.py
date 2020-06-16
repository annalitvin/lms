import time


class LoggingRequestTime:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start = time.time()
        response = self.get_response(request)
        end = time.time()

        print("TOTAL TIME", (end - start))

        return response

