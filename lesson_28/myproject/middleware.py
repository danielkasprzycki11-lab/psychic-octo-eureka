class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        metoda = request.method
        print(f"Otrzymano zapytanie metodą {metoda}")
        
        response = self.get_response(request)
        return response
