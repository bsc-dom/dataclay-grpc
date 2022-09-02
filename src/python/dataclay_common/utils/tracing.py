from opentelemetry import trace


class LoggerEvent:
    def __init__(self, logger):
        super().__setattr__("logger", logger)

    def __getattr__(self, name):
        def wrapper(msg, *args, **kwargs):
            try:
                current_span = trace.get_current_span()
                current_span.add_event(msg % args)
            except NameError:
                pass
            getattr(self.logger, name)(msg, *args, **kwargs)

        return wrapper
