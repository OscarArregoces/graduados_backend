from rest_framework.routers import Route, SimpleRouter
from src.factory.eventos_interactor import BaseViewSetFactory
from src.interfaces.routes.eventos.eventos_route import router
from src.application.eventos.models import Eventos


class Router(SimpleRouter):
    router_base = router
    name_base = "eventos"
    model = Eventos

    routes = [
        Route(
            url=router_base.get_url(f"{name_base}_get"),
            mapping=router_base.map(f"{name_base}_get"),
            initkwargs={
                "viewset_factory": BaseViewSetFactory,
                "http_method_names": ["get"],
                "model": model,
            },
            name="{basename}-list",
            detail=True,
        ),
        # Route(
        #     url=router_base.get_url(f"{name_base}_post"),
        #     mapping=router_base.map(f"{name_base}_post"),
        #     initkwargs={
        #         "viewset_factory": BaseViewSetFactory,
        #         "http_method_names": ["post"],
        #         "model": model,
        #     },
        #     name="{basename}-create",
        #     detail=True,
        # ),
        Route(
            url=router_base.get_url(f"{name_base}_put"),
            mapping=router_base.map(f"{name_base}_put"),
            initkwargs={
                "viewset_factory": BaseViewSetFactory,
                "http_method_names": ["put"],
                "model": model,
            },
            name="{basename}-update",
            detail=True,
        ),
        Route(
            url=router_base.get_url(f"{name_base}_delete"),
            mapping=router_base.map(f"{name_base}_delete"),
            initkwargs={
                "viewset_factory": BaseViewSetFactory,
                "http_method_names": ["delete"],
                "model": model,
            },
            name="{basename}-delete",
            detail=True,
        )
    ]
