import structlog.processors
from structlog.typing import Processor
from typing import Optional

from . import errors, processors


def build_processors(
    service: Optional[str] = None,
    version: Optional[str] = None,
) -> list[Processor]:
    procs = []

    procs.extend(processors.CoreCloudLogging().setup())
    procs.extend(processors.LogSeverity().setup())
    procs.extend(processors.CodeLocation().setup())
    procs.extend(errors.ReportException().setup())
    procs.extend(errors.ReportError(["CRITICAL"]).setup())
    procs.extend(errors.ServiceContext(service, version).setup())
    procs.extend(processors.FormatAsCloudLogging().setup())
    procs.append(structlog.processors.JSONRenderer())
    return procs
