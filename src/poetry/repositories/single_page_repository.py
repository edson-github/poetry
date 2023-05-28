from __future__ import annotations

from typing import TYPE_CHECKING

from poetry.repositories.exceptions import PackageNotFound
from poetry.repositories.legacy_repository import LegacyRepository
from poetry.repositories.link_sources.html import SimpleRepositoryPage


if TYPE_CHECKING:
    from packaging.utils import NormalizedName


class SinglePageRepository(LegacyRepository):
    def _get_page(self, name: NormalizedName) -> SimpleRepositoryPage:
        """
        Single page repositories only have one page irrespective of endpoint.
        """
        if response := self._get_response(""):
            return SimpleRepositoryPage(response.url, response.text)
        else:
            raise PackageNotFound(f"Package [{name}] not found.")
