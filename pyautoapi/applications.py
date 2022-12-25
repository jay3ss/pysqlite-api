from fastapi import FastAPI

import pyautoapi.routing as rt


class PyAutoAPI(FastAPI):
    def __init__(
        self,
        *,
        debug: bool = False,
        routes: list[rt.Route] = None,
        title: str = "PyAutoAPI",
        description: str = "",
        version: str = "0.0.1",
    ) -> None:
        super().__init__(debug, routes, title, description, version)