# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from typing import Any, Callable, Iterable

from google.firestore_v1.types import document
from google.firestore_v1.types import firestore
from google.firestore_v1.types import query


class ListDocumentsPager:
    """A pager for iterating through ``list_documents`` requests.

    This class thinly wraps an initial
    :class:`~.firestore.ListDocumentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``documents`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDocuments`` requests and continue to iterate
    through the ``documents`` field on the
    corresponding responses.

    All the usual :class:`~.firestore.ListDocumentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[[firestore.ListDocumentsRequest],
                firestore.ListDocumentsResponse],
            request: firestore.ListDocumentsRequest,
            response: firestore.ListDocumentsResponse):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.firestore.ListDocumentsRequest`):
                The initial request object.
            response (:class:`~.firestore.ListDocumentsResponse`):
                The initial response object.
        """
        self._method = method
        self._request = firestore.ListDocumentsRequest(request)
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[firestore.ListDocumentsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request)
            yield self._response

    def __iter__(self) -> Iterable[document.Document]:
        for page in self.pages:
            yield from page.documents

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)


class PartitionQueryPager:
    """A pager for iterating through ``partition_query`` requests.

    This class thinly wraps an initial
    :class:`~.firestore.PartitionQueryResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``partitions`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``PartitionQuery`` requests and continue to iterate
    through the ``partitions`` field on the
    corresponding responses.

    All the usual :class:`~.firestore.PartitionQueryResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """
    def __init__(self,
            method: Callable[[firestore.PartitionQueryRequest],
                firestore.PartitionQueryResponse],
            request: firestore.PartitionQueryRequest,
            response: firestore.PartitionQueryResponse):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (:class:`~.firestore.PartitionQueryRequest`):
                The initial request object.
            response (:class:`~.firestore.PartitionQueryResponse`):
                The initial response object.
        """
        self._method = method
        self._request = firestore.PartitionQueryRequest(request)
        self._response = response

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[firestore.PartitionQueryResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request)
            yield self._response

    def __iter__(self) -> Iterable[query.Cursor]:
        for page in self.pages:
            yield from page.partitions

    def __repr__(self) -> str:
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)