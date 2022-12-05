from typing import Any, Callable, Type, TypeVar

from .app import _ViewFunc
from .helpers import _PackageBoundObject

_T = TypeVar("_T")
_VT = TypeVar("_VT", bound=_ViewFunc)

class _Sentinel(object): ...

class BlueprintSetupState:
    app: Any = ...
    blueprint: Any = ...
    options: Any = ...
    first_registration: Any = ...
    subdomain: Any = ...
    url_prefix: Any = ...
    url_defaults: Any = ...
    def __init__(self, blueprint: Any, app: Any, options: Any, first_registration: Any) -> None: ...
    def add_url_rule(self, rule: str, endpoint: str | None = ..., view_func: _ViewFunc = ..., **options: Any) -> None: ...

class Blueprint(_PackageBoundObject):
    warn_on_modifications: bool = ...
    json_encoder: Any = ...
    json_decoder: Any = ...
    import_name: str = ...
    template_folder: str | None = ...
    root_path: str = ...
    name: str = ...
    url_prefix: str | None = ...
    subdomain: str | None = ...
    static_folder: str | None = ...
    static_url_path: str | None = ...
    deferred_functions: Any = ...
    url_values_defaults: Any = ...
    cli_group: str | None | _Sentinel = ...
    def __init__(
        self,
        name: str,
        import_name: str,
        static_folder: str | None = ...,
        static_url_path: str | None = ...,
        template_folder: str | None = ...,
        url_prefix: str | None = ...,
        subdomain: str | None = ...,
        url_defaults: Any | None = ...,
        root_path: str | None = ...,
        cli_group: str | None | _Sentinel = ...,
    ) -> None: ...
    def record(self, func: Any) -> None: ...
    def record_once(self, func: Any): ...
    def make_setup_state(self, app: Any, options: Any, first_registration: bool = ...): ...
    def register(self, app: Any, options: Any, first_registration: bool = ...) -> None: ...
    def route(self, rule: str, **options: Any) -> Callable[[_VT], _VT]: ...
    def add_url_rule(self, rule: str, endpoint: str | None = ..., view_func: _ViewFunc = ..., **options: Any) -> None: ...
    def endpoint(self, endpoint: str) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
    def app_template_filter(self, name: Any | None = ...): ...
    def add_app_template_filter(self, f: Any, name: Any | None = ...) -> None: ...
    def app_template_test(self, name: Any | None = ...): ...
    def add_app_template_test(self, f: Any, name: Any | None = ...) -> None: ...
    def app_template_global(self, name: Any | None = ...): ...
    def add_app_template_global(self, f: Any, name: Any | None = ...) -> None: ...
    def before_request(self, f: Any): ...
    def before_app_request(self, f: Any): ...
    def before_app_first_request(self, f: Any): ...
    def after_request(self, f: Any): ...
    def after_app_request(self, f: Any): ...
    def teardown_request(self, f: Any): ...
    def teardown_app_request(self, f: Any): ...
    def context_processor(self, f: Any): ...
    def app_context_processor(self, f: Any): ...
    def app_errorhandler(self, code: Any): ...
    def url_value_preprocessor(self, f: Any): ...
    def url_defaults(self, f: Any): ...
    def app_url_value_preprocessor(self, f: Any): ...
    def app_url_defaults(self, f: Any): ...
    def errorhandler(self, code_or_exception: int | Type[Exception]) -> Callable[[Callable[..., _T]], Callable[..., _T]]: ...
    def register_error_handler(self, code_or_exception: int | Type[Exception], f: Callable[..., Any]) -> None: ...
